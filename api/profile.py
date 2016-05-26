from model.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def profile_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        results = {'data': user}
        return JsonResponse(user)

@csrf_exempt
def profile_update(request):
    if request.method == 'POST':
        data = request.body
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        user.username = data.username
        user.password = data.password
        user.realname = data.realname
        user.phoneNum = data.phoneNum
        user.age = data.age
        user.waistlineProfile = data.waistlineProfile
        user.weightProfile = data.weightProfile
        user.heightProfile = data.heightProfile
        user.bmiProfile = data.bmiProfile
        user.relativesSituation = data.relativesSituation
        user.meatSituation = data.meatSituation
        user.fruitSituation = data.fruitSituation
        user.bloodPressure = data.bloodPressure
        user.cholesterol = data.cholesterol
        user.triglyceride = data.triglyceride
        user.save()
        return JsonResponse({'status': 1}) # save success