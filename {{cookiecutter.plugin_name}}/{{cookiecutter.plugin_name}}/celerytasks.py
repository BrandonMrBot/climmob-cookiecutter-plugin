{% if cookiecutter.plugin_hasCeleryTasks == 'Y' or cookiecutter.plugin_hasCeleryTasks == 'y' -%}
from climmob.config.celery_app import celeryApp
from climmob.plugins.utilities import climmobCeleryTask
import time


@celeryApp.task(
    bind=True, base=climmobCeleryTask, soft_time_limit=7200, time_limit=7200
)
def plugin_task():
    time.sleep(
        30
    )  # Just to test that such sleep is handled by celery and does not hang ClimMob
    print("Plugin task finished")
{%- endif %}
