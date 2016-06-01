#!/usr/bin/python
# -*- coding: utf8 -*-
from django.db import models

###############################################################################
#                           Basic models                                      #
###############################################################################
class Category(models.Model):
    name = models.CharField(max_length = 255)
    #categoty_id = models.CharField(max_length = 8)

class Source(models.Model):
    name = models.CharField(max_length = 255)

###############################################################################
#                           User and Contact                                 #
###############################################################################
class User(models.Model):
    name = models.CharField(max_length = 255)
    password = models.CharField(max_length = 32)
    email = models.EmailField(max_length = 255)
    phone = models.CharField(max_length = 15)
    birthday = models.DateField(null = True)
    profile_url = models.CharField(max_length = 255,
        default = 'static/profile/default.png')
    device_token = models.CharField(max_length = 32)
    access_token = models.CharField(max_length = 32)
    token_expiration = models.DateTimeField()
    verification_code = models.CharField(max_length = 8)
    code_expiration = models.DateTimeField(auto_now_add = True)
    create_time = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now = True)

class Admin(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    admin_ip = models.CharField(max_length=255)
    admin_type = models.CharField(max_length=8)
    check_num = models.CharField(max_length=32)
    publish_num = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Admindaily(models.Model):
    author = models.ForeignKey(Admin)
    content = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255,)
    phone = models.CharField(max_length = 15)
    source = models.ForeignKey(Source)
    is_delete = models.BooleanField(default = False)
    create_time = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now = True)

###############################################################################
#                          Personal and Group Event                           #
###############################################################################
class Event(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length = 255)
    content = models.TextField(default = '')
    address = models.CharField(max_length = 255)
    comment = models.CharField(max_length = 255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    remind_time = models.DateTimeField()
    is_memo = models.BooleanField(default = False)
    category = models.ForeignKey(Category)
    source = models.ForeignKey(Source)
    is_delete = models.BooleanField(default = False)
    create_time = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now = True)

class Cron(models.Model):
    event = models.ForeignKey(Event)
    expression = models.CharField(max_length = 255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class GroupMember(models.Model):
    event = models.ForeignKey(Event)
    member = models.ForeignKey(User)
    member_name = models.CharField(max_length = 255)
    comment = models.CharField(max_length = 255)
    STATUS_CHOICES = (('Y', 'Yes'),
                      ('M', 'Maybe'),
                      ('N', 'No'))
    accept_status = models.CharField(max_length = 1,
                                     choices = STATUS_CHOICES,
                                     default = 'M')
    is_delete = models.BooleanField(default = False)
    last_update = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = (("event", "member"),)

###############################################################################
#                          Recommend Event                                    #
###############################################################################
class RecommendEvent(models.Model):
    author = models.ForeignKey(Admin)        #new
    title = models.CharField(max_length = 255)
    content = models.TextField()
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 20)
    pic_url = models.CharField(max_length = 255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    category = models.ForeignKey(Category)
    source = models.ForeignKey(Source)
    original_id = models.CharField(max_length = 15)
    original_category = models.CharField(max_length = 10)
    last_update = models.DateTimeField(auto_now = True)
    create_time = models.DateTimeField(auto_now_add=True)        #new
    publish_state = models.CharField(max_length=8)        #new
    publish_time = models.DateTimeField()        #new
    publish_admin_id = models.CharField(max_length=8)        #new
    check_state = models.CharField(max_length=8)        #new
    check_time = models.DateTimeField()        #new
    check_admin_id = models.CharField(max_length=8)        #new

