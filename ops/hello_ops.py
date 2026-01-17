from dagster import op

@op
def say_hellow()->str:
    return "Hello world from Dagster:)"
@op
def say_bye(message : str)->str:
    return f"Bye from Dagster:) | Received : {message}"