# dagster-project-repo
Repository for writing dagster codes

# Steps for setting up dagster

1) install all the required dependencies
   ```
    pip install requirements.txt
    ```
   optional : 
    after installing if you want to freeze the version use the command
    ```
     pip freeze > requirements.txt
    ```
2) scanfold dagster project
   command : 
   ```
   dagster project scaffold --name my_dagster_project
   ```
3) Setup postgres for dagster metadata
   ```
   CREATE DATABASE dagster_metadata;
   ```

4) Configure dagster to use postgres
    dagster.yaml
   ```
     run_storage:
       module: dagster_postgres.run_storage
       class: PostgresRunStorage
     config:
       postgres_db:
       username:
         env: DAGSTER_DB_USER
       password:
         env: DAGSTER_DB_PASSWORD
       hostname:
         env: DAGSTER_DB_HOST
       db_name:
         env: DAGSTER_DB_NAME
       port:
         env: DAGSTER_DB_PORT

      event_log_storage:
       module: dagster_postgres.event_log
       class: PostgresEventLogStorage
       config:
        postgres_db:
        username:
         env: DAGSTER_DB_USER
        password:
         env: DAGSTER_DB_PASSWORD
        hostname:
         env: DAGSTER_DB_HOST
        db_name:
          env: DAGSTER_DB_NAME
        port:
         env: DAGSTER_DB_PORT

     schedule_storage:
      module: dagster_postgres.schedule_storage
      class: PostgresScheduleStorage
      config:
       postgres_db:
        username:
         env: DAGSTER_DB_USER
        password:
         env: DAGSTER_DB_PASSWORD
        hostname:
         env: DAGSTER_DB_HOST
        db_name:
         env: DAGSTER_DB_NAME
        port:
         env: DAGSTER_DB_PORT
      ```
      
          

5) run dagster
    command : 
    ```
    dagster dev
    ```
   

# dagster_dev

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/guides/build/projects/creating-a-new-project).

## Getting started

First, install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```

Open http://localhost:3000 with your browser to see the project.

You can start writing assets in `dagster_dev/assets.py`. The assets are automatically loaded into the Dagster code location as you define them.

## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `dagster_dev_tests` directory and you can run tests using `pytest`:

```bash
pytest dagster_dev_tests
```

### Schedules and sensors

If you want to enable Dagster [Schedules](https://docs.dagster.io/guides/automate/schedules/) or [Sensors](https://docs.dagster.io/guides/automate/sensors/) for your jobs, the [Dagster Daemon](https://docs.dagster.io/guides/deploy/execution/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.

## Deploy on Dagster+

The easiest way to deploy your Dagster project is to use Dagster+.

Check out the [Dagster+ documentation](https://docs.dagster.io/dagster-plus/) to learn more.
