from django.db import models
from django.utils import  timezone
from colorfield.fields import ColorField
from datetime import datetime, timedelta
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
import pandas as pd
import re
now = timezone.now

