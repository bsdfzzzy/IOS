from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    def __unicode__(self):
        return self.username

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    realname = models.CharField(max_length=50, blank=True)
    phoneNum = models.CharField(max_length=50, blank=True)
    age = models.CharField(max_length=50,blank=True)
    waistlineProfile = models.CharField(max_length=50, blank=True)
    weightProfile = models.CharField(max_length=50, blank=True)
    heightProfile = models.CharField(max_length=50, blank=True)
    bmiProfile = models.CharField(max_length=50, blank=True)
    relativesSituation = models.CharField(max_length=50, blank=True)
    meatSituation = models.CharField(max_length=50, blank=True)
    fruitSituation = models.CharField(max_length=50, blank=True)
    bloodPressure = models.CharField(max_length=50, blank=True)
    cholesterol = models.CharField(max_length=50, blank=True)
    triglyceride = models.CharField(max_length=50, blank=True)

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
