from model.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def message_response(status):
    response = {}
    response['status'] = status
    return response

@csrf_exempt # skip the csrf confirmation in django
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        try:
            user = User.objects.get(username = username)
            '''if user.password != '' or user.realname != '':
                return JsonResponse(message_response(2)) # 2 already exists an account with the same username
            if username != '':
                user.username = username
            if password != '':
                user.password = password
            user.save()'''
            response = {'status': 0}  #0 catch something error
        except Exception as e:
            print e
	    user = User(username=username,password=password)
	    user.save()
            response = message_response(1)  # success
        return JsonResponse(response)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        if username == '' or password == '':
            return JsonResponse(message_response(0)) # login failed

        try:
            user = User.objects.get(username = username)
            if user.password != password:
                return JsonResponse(message_response(0)) #login failed
            #request.session['user_id'] = user.id
        except Exception:
            return JsonResponse(message_response(0)) #login failed

        response = {'status' : 1}
	user = User.objects.get(username=username)
	request.session['user_id'] = user.id
        return JsonResponse(response)
