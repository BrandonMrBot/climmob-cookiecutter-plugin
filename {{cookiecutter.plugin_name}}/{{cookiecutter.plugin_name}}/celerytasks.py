{% if cookiecutter.plugin_hasCeleryTasks == 'Y' or cookiecutter.plugin_hasCeleryTasks == 'y' -%}
from formshare.config.celery_app import celeryApp
from formshare.config.celery_class import CeleryTask
import time


@celeryApp.task(base=CeleryTask)
def plugin_task():
    time.sleep(
        30
    )  # Just to test that such sleep is handled by celery and does not hang FormShare
    print("Plugin task finished")
{%- endif %}
