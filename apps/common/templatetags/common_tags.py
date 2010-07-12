import re
from django import template
from django.db import models

from common import utils

register = template.Library()

@register.filter
def cdate(date):
    return utils.clever_date(date)

