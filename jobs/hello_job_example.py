from dagster import job
import ops.hello_ops as runner

@job
def hello_job_example():
    msg = runner.say_hellow()
    runner.say_bye(msg)