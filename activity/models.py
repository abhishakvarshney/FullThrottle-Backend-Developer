import sys
sys.path.append("..")
import os
import uuid
import json
from django.db import models
from utility.log import log
from utility.Exceptions import *
from utility.utils import GeneralUtils as GU
from django.http import JsonResponse
from django.core import serializers


# Create your models here.
__all__ = ["User", "UserActivity"]

GENDER_MALE = "Male"
GENDER_FEMALE = "Female"

GENDER_CHOICES = (
    (GENDER_MALE, "Male"),
    (GENDER_FEMALE, "Female"),
)


class User(models.Model):
    """
    @return:
    """

    class Meta:
        """
        @return:
        """
        db_table = "User"

    user_id = models.CharField(max_length=255, primary_key=True, default=uuid.uuid4, editable=False)
    realname = models.TextField(null=True, blank=True)
    tz_info = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Male")
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{}".format(self.realname)

    @staticmethod
    def get_user():
        """
        @return:
        """
        response_dict = User.objects.all()
        user_data_list = []
        for data in response_dict:
            user_data = {}
            user_data['user_id'] = data.user_id
            user_data['realname'] = GU.decryptData(data.realname)
            user_data['tz'] = data.tz_info
            user_data['activity_periods'] = UserActivity.get_activity(data.user_id)
            user_data_list.append(user_data)
        return user_data_list

    @staticmethod
    def add_user(data):
        """

        @param data:
        @return:
        """
        user = User()
        user.realname = GU.encryptData(data.get("realname", ""))
        user.tz_info = data.get("tz_info", "")
        user.gender = data.get("gender", "Male")
        user.isActive = True
        user_exist = User.check_user(user.realname)
        if  user_exist is None:
            user.user_id = data.get("user_id", uuid.uuid4())
            user.save()
            return user, True
        return user_exist, False

    @staticmethod
    def check_user(realname):
        """

        @param realname:
        @return:
        """
        userData = User.objects.filter(realname=realname)
        if userData is None or len(userData) == 0:
            return None
        return userData[0]


class UserActivity(models.Model):

    """

    @return:
    """

    class Meta:
        """
        @return:
        """

        db_table = "UserActivity"

    user_activity_id = models.CharField(max_length=255, primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False, db_column='user_id')
    start_time = models.TextField(null=True, blank=True)
    end_time = models.TextField(null=True, blank=True)

    def __repr__(self):
        return "{}".format(self.user_id)

    @staticmethod
    def get_activity(user_id):
        """

        @return:
        """
        response_dict = UserActivity.objects.filter(user_id=user_id)
        activity_data_list = []
        for data in response_dict:
            activity_data = {}
            activity_data['start_time'] = data.start_time
            activity_data['end_time'] = data.end_time
            activity_data_list.append(activity_data)
        return activity_data_list

    @staticmethod
    def check_activity(user_activity_id):
        """

        @param user_activity_id:
        @return:
        """
        userData = UserActivity.objects.filter(user_activity_id__exact=user_activity_id)
        if userData is None or len(userData) == 0:
            return None
        return userData[0]

    @staticmethod
    def add_activity(data):
        """

        @param data:
        @return:
        """
        user_details = User.objects.get(user_id=data.get("user_id", ''))
        user = UserActivity()
        user.user_activity_id = data.get("user_activity_id", uuid.uuid4())
        user.user_id = user_details
        user.start_time = data.get("start_time", "")
        user.end_time = data.get("end_time", "")
        user.save()
        return user, True
