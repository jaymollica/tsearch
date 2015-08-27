from fabric.api import env, task

from deployo.tasks import environment
from deployo.contrib.deployment.gunicorn import *