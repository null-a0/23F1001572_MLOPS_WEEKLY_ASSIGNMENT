from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource, Project
from feast.types import Float32

# Define the Feast project
project = Project(
    name="feature_repo",
    description="IRIS Feature Store",
)

# Define the entity (primary key)
iris = Entity(
    name="iris",
    join_keys=["sample_id"],
)

iris_source = FileSource(
    name="iris_source",
    path="../../data/iris_feast.parquet",
    timestamp_field="event_timestamp",
)

# Define the Feature View
iris_features = FeatureView(
    name="iris_features",
    entities=[iris],
    ttl=timedelta(days=365),
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
    ],
    source=iris_source,
    online=True,
)