import os
import json
import ast
import base64

from django.http import JsonResponse, HttpResponse
from activity import models
from rest_framework.decorators import api_view, parser_classes
from django.shortcuts import render
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response
from utility.log import log
from utility.Exceptions import *
from utility.utils import GeneralUtils as GU
from .validation import *


# Create your views here.
@api_view(["GET"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def get_user(request):
    """
        list all user

        #### url
            http://localhost:8000/get/user/

        #### Method
            GET

        #### Headers
            {
                "Content-Type": "application/json"
            }

        #### Payload

        #### Return
            {
                "status_code": 200,
                "message": "Success",
                "result": True
            }
        """
    if request.method == "GET":
        user_list = models.User.get_user()
        response_dict = {}
        if response_dict is None or len(user_list) == 0:
            response_dict["status_code"] = 200
            response_dict["message"] = "No User Available"
            response_dict["result"] = False
            response_dict["response"] = {'ok':False, 'members':None}
        else:
            response_dict["status_code"] = 200
            response_dict["message"] = "Success"
            response_dict["result"] = True
            response_dict["response"] = {'ok':True, 'members':user_list}
        log.d("list user response = " + str(response_dict))
        return Response(response_dict, status=201)


@api_view(["POST"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def add_user(request):
    data = json.loads(request.body.decode("utf-8"))
    response_dict = {}
    validate_request, error_msg = validate_add_user(request)
    if not validate_request:
        log.error(error_msg)
        return JsonResponse(error_msg)
    user_exist = models.User.check_user(GU.encryptData(data.get("realname", "")))
    log.error("UserCreation Status{}".format(user_exist))
    if not user_exist:
        user_data, is_created = models.User.add_user(data)
        response_dict["user_id"] = user_data.user_id
        response_dict["status_code"] = 200
        return Response(response_dict, status=201)
    else:
        return Response(
            {"status_code": 200, "message": "User Already Exists.", "user_id":user_exist.user_id},
            status=201,
        )


@api_view(["GET"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def get_user_activity(request):
    if request.method == "GET":
        user_id = request.GET.get('user_id', '')
        user_activity_list = models.UserActivity.get_activity(user_id)
        response_dict = {}
        if response_dict is None or len(user_activity_list) == 0:
            response_dict["status_code"] = 200
            response_dict["message"] = "No User Activity Available"
            response_dict["result"] = False
            response_dict["response"] = None
        else:
            response_dict["status_code"] = 200
            response_dict["message"] = "Success"
            response_dict["result"] = True
            response_dict["response"] = user_activity_list
        log.d("get user_activity response = " + str(response_dict))
        return Response(response_dict, status=201)


@api_view(["POST"])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def add_user_activity(request):
    data = json.loads(request.body.decode("utf-8"))
    response_dict = {}
    validate_request, error_msg = validate_add_user_activity(request)
    if not validate_request:
        log.error(error_msg)
        return JsonResponse(error_msg)
    user_data, is_created = models.UserActivity.add_activity(data)
    response_dict["user_id"] = user_data.user_id.user_id
    response_dict["status_code"] = 200
    return Response(response_dict, status=201)
