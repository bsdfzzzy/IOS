from django.contrib import admin
from models import *
# Register your models here.

admin.site.register(User)
admin.site.register(EvaluateResults)
admin.site.register(MedicineReminder)
admin.site.register(SportsReminder)
admin.site.register(MeasurementReminder)
admin.site.register(DiabeteRecords)
admin.site.register(BmiRecords)
admin.site.register(DietRecords)
