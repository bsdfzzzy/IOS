from model.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt # skip the csrf confirmation in django
def register(request):
    if request.method == 'GET':

    if request.method == 'POST':
        data = request.body
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(username = username)
            if user.password != '' or user.realname != '':
                return JsonResponse(message_response(2)) # 2 already exists an account with the same username
            if username != '':
                user.username = username
            if password != '':
                user.password = password
            user.save()
            response = {'status': 1}  #1 register success
        except Exception as e:
            logger.error(e)
            response = message_response(0)  # catch something error

        logger.info("Status: {}".format(response['status']))  # print the status
        return JsonResponse(response)

@csrf_exempt
def login(request):
    if method == 'GET':

    if method == 'POST':
        data = request.body
        username = data.get('username')
        password = data.get('password')

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
        return JsonResponse(response)