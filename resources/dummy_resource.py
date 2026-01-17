from dagster import resource

@resource
def dummy_resource()->str:
    return "This is a dummy resource"