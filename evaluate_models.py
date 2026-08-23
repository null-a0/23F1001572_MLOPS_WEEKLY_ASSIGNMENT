import json
import sys

from google import genai
from sklearn.metrics import accuracy_score, precision_score, recall_score


# ============================================================
# CONFIGURATION
# ============================================================

PROJECT_ID = "project-0a6400db-0297-4323-a8f"
LOCATION = "us-central1"

V1_ENDPOINT = (
    "projects/938959281806/locations/us-central1/"
    "endpoints/6507952699957313536"
)

V2_ENDPOINT = (
    "projects/938959281806/locations/us-central1/"
    "endpoints/3166281776448405504"
)

V1_TEST_FILE = "data/iris_v1_test.jsonl"
V2_TEST_FILE = "data/iris_v2_test.jsonl"

# CI regression threshold
MIN_ACCURACY = 0.20

VALID_CLASSES = {
    "setosa",
    "versicolor",
    "virginica",
}


# ============================================================
# VERTEX AI CLIENT
# ============================================================

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)


# ============================================================
# LOAD JSONL
# ============================================================

def load_jsonl(path):
    records = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line:
                records.append(json.loads(line))

    return records


# ============================================================
# EXTRACT INPUT / TARGET
# ============================================================

def extract_record(record):
    """
    Supports the input_text/output_text JSONL format
    used by the Week 10 datasets.
    """

    if "input_text" in record and "output_text" in record:
        return record["input_text"], record["output_text"]

    raise ValueError(
        f"Unexpected JSONL format. Keys found: {list(record.keys())}"
    )


# ============================================================
# NORMALIZE TARGET
# ============================================================

def normalize_target(text):
    """
    Convert the expected output into the canonical class name.
    """

    text = text.strip().lower()

    for class_name in VALID_CLASSES:
        if class_name in text:
            return class_name

    return text


# ============================================================
# PROMPTS
# ============================================================

def v1_prompt(text):
    return (
        "Classify the flower based on its measurements into exactly "
        "one of these species: setosa, versicolor, virginica.\n"
        "Return only the species name and nothing else.\n\n"
        f"{text}"
    )


def v2_prompt(text):
    return (
        "Identify the iris species from the following description.\n"
        "Return only one of these exact responses:\n"
        "This is Iris setosa.\n"
        "This is Iris versicolor.\n"
        "This is Iris virginica.\n\n"
        f"{text}"
    )


# ============================================================
# MODEL PREDICTION
# ============================================================

def generate_prediction(endpoint, prompt):
    response = client.models.generate_content(
        model=endpoint,
        contents=prompt,
    )

    if response.text is None:
        return ""

    return response.text.strip()


# ============================================================
# PARSE PREDICTION
# ============================================================

def parse_prediction(text, version):
    """
    Extract the predicted species while preserving
    the original response for format-compliance checking.
    """

    raw = text.strip()

    lower = raw.lower()

    for class_name in VALID_CLASSES:
        if class_name in lower:
            return class_name

    return ""


# ============================================================
# FORMAT COMPLIANCE
# ============================================================

def is_format_compliant(text, version):

    text = text.strip()

    if version == "V1":
        return text in {
            "setosa",
            "versicolor",
            "virginica",
        }

    if version == "V2":
        return text in {
            "This is Iris setosa.",
            "This is Iris versicolor.",
            "This is Iris virginica.",
        }

    return False


# ============================================================
# EVALUATION
# ============================================================

def evaluate(version, endpoint, test_file):

    records = load_jsonl(test_file)

    y_true = []
    y_pred = []

    compliant_count = 0

    print()
    print("=" * 70)
    print(f"{version} EVALUATION")
    print("=" * 70)
    print(f"Test samples: {len(records)}")

    for i, record in enumerate(records):

        input_text, expected_text = extract_record(record)

        expected = normalize_target(expected_text)

        if version == "V1":
            prompt = v1_prompt(input_text)
        else:
            prompt = v2_prompt(input_text)

        prediction_text = generate_prediction(
            endpoint,
            prompt,
        )

        predicted = parse_prediction(
            prediction_text,
            version,
        )

        if is_format_compliant(
            prediction_text,
            version,
        ):
            compliant_count += 1

        y_true.append(expected)
        y_pred.append(predicted)

        print(
            f"{i + 1:02d}. "
            f"Expected: {expected:<10} "
            f"Predicted: {predicted:<10} "
            f"Raw: {prediction_text[:100]}"
        )

    accuracy = accuracy_score(
        y_true,
        y_pred,
    )

    precision = precision_score(
        y_true,
        y_pred,
        labels=[
            "setosa",
            "versicolor",
            "virginica",
        ],
        average=None,
        zero_division=0,
    )

    recall = recall_score(
        y_true,
        y_pred,
        labels=[
            "setosa",
            "versicolor",
            "virginica",
        ],
        average=None,
        zero_division=0,
    )

    format_compliance = (
        compliant_count / len(records)
        if records
        else 0.0
    )

    print()
    print("-" * 70)
    print(f"{version} RESULTS")
    print("-" * 70)

    print(f"Accuracy:          {accuracy:.4f}")
    print(f"Format Compliance: {format_compliance:.4f}")

    print()
    print("Per-Class Metrics:")

    classes = [
        "setosa",
        "versicolor",
        "virginica",
    ]

    for cls, p, r in zip(
        classes,
        precision,
        recall,
    ):
        print(
            f"{cls:<12} "
            f"Precision: {p:.4f} | "
            f"Recall: {r:.4f}"
        )

    return {
        "version": version,
        "accuracy": accuracy,
        "format_compliance": format_compliance,
        "precision": precision,
        "recall": recall,
    }


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 70)
    print("TASK 5 — CI LLM EVALUATION")
    print("=" * 70)

    v1_results = evaluate(
        "V1",
        V1_ENDPOINT,
        V1_TEST_FILE,
    )

    v2_results = evaluate(
        "V2",
        V2_ENDPOINT,
        V2_TEST_FILE,
    )

    print()
    print("=" * 70)
    print("V1 vs V2")
    print("=" * 70)

    print(
        f"V1 Accuracy: {v1_results['accuracy']:.4f}"
    )

    print(
        f"V2 Accuracy: {v2_results['accuracy']:.4f}"
    )

    print(
        f"Required Minimum Accuracy: {MIN_ACCURACY:.4f}"
    )

    v1_pass = (
        v1_results["accuracy"] >= MIN_ACCURACY
    )

    v2_pass = (
        v2_results["accuracy"] >= MIN_ACCURACY
    )

    print()
    print(f"V1 Regression Check: {'PASS' if v1_pass else 'FAIL'}")
    print(f"V2 Regression Check: {'PASS' if v2_pass else 'FAIL'}")

    # GitHub Actions / CI exit code
    if not v1_pass or not v2_pass:
        print()
        print("CI CHECK FAILED")
        print(
            "At least one model is below the minimum "
            "accuracy threshold."
        )
        sys.exit(1)

    print()
    print("CI CHECK PASSED")
    print(
        "Both models satisfy the minimum accuracy threshold."
    )


if __name__ == "__main__":
    main()