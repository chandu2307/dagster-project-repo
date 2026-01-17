from dagster import Definitions
from jobs.hello_job_example import hello_job_example
from resources.dummy_resource import dummy_resource

defs = Definitions(
    jobs=[hello_job_example],
    resources={
        "dummy_resource": dummy_resource
    }
)
