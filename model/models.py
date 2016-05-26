from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    realname = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    waistlineProfile = models.CharField(max_length=50)
    weightProfile = models.CharField(max_length=50)
    heightProfile = models.CharField(max_length=50)
    bmiProfile = models.CharField(max_length=50)
    relativesSituation = models.CharField(max_length=50)
    meatSituation = models.CharField(max_length=50)
    fruitSituation = models.CharField(max_length=50)
    bloodPressure = models.CharField(max_length=50)
    cholesterol = models.CharField(max_length=50)
    triglyceride = models.CharField(max_length=50)

class EvaluateResults(models.Model):
    owner = models.ForeignKey(User)
    evaluateResults = models.CharField(max_length=1000)

class MedicineReminder(models.Model):
    owner = models.ForeignKey(User)
    medicineReminder = models.CharField(max_length=1000)

class SportsReminder(models.Model):
    owner = models.ForeignKey(User)
    sportsRemainder = models.CharField(max_length=1000)

class MeasurementReminder(models.Model):
    owner = models.ForeignKey(User)
    measurementReminder = models.CharField(max_length=1000)

class DiabeteRecords(models.Model):
    owner = models.ForeignKey(User)
    diabeteRecords = models.CharField(max_length=1000)

class BmiRecords(models.Model):
    owner = models.ForeignKey(User)
    bmiRecords = models.CharField(max_length=1000)

class DietRecords(models.Model):
    owner = models.ForeignKey(User)
    dietRecords = models.CharField(max_length=1000)
