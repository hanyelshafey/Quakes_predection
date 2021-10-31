from django.contrib import admin

from datetime import datetime
from inspect import Parameter
from django.contrib import admin


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from  sklearn.metrics import accuracy_score, confusion_matrix , recall_score , precision_score , f1_score ,classification_report,plot_confusion_matrix



import django_heroku
from .models import Quake, Quake_Predections
#import models.Quake


# Register your models here.
admin.site.register(Quake)
admin.site.register(Quake_Predections)