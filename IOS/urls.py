"""IOS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from api.login_regist import *
from api.records import *
from api.reminders import *
from api.results import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login', login),
    url(r'^register', register),
    url(r'^diabeteRecords_get', diabeteRecords_get),
    url(r'^diabeteRecords_add', diabeteRecords_add),
    url(r'^diabeteRecords_update', diabeteRecords_update),
    url(r'^dietRecords_get', dietRecords_get),
    url(r'^dietRecords_get', dietRecords_add),
    url(r'^dietRecords_get', dietRecords_update),
    url(r'^bmiRecords_get', bmiRecords_get),
    url(r'^bmiRecords_add', bmiRecords_add),
    url(r'^bmiRecords_update', bmiRecords_update),
    url(r'^medicineReminder_get', medicineReminder_get),
    url(r'^medicineReminder_get', medicineReminder_add),
    url(r'^medicineReminder_get', medicineReminder_update),
    url(r'^medicineReminder_get', medicineReminder_delete),
    url(r'^sportsReminder_get', sportsReminder_get),
    url(r'^sportsReminder_get', sportsReminder_add),
    url(r'^sportsReminder_get', sportsReminder_update),
    url(r'^sportsReminder_get', sportsReminder_delete),
    url(r'^measurementReminder_get', measurementReminder_get),
    url(r'^measurementReminder_get', measurementReminder_add),
    url(r'^measurementReminder_get', measurementReminder_update),
    url(r'^measurementReminder_get', measurementReminder_delete),
    url(r'^evaluateResults', evaluateResults)
]
