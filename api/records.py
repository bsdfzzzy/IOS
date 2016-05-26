from model.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def diabeteRecords_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        results = {'data': user.diabeterecords_set.all()}
        return JsonResponse(results)

@csrf_exempt
def diabeteRecords_add(request):
    if request.method == 'POST':
        data = request.body
        user = User.objects.get(id=request.session['user_id'])
        new_record = DiabeteRecords(owner=user, evaluateResults=data.value)
        new_record.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def diabeteRecords_update(request):
    if request.method == 'POST':
        data = request.body
        product_id = data.get('product_id')
        diabete_record = DiabeteRecords.objects.get(id=product_id)
        diabete_record.diabeteRecords = data.value
        diabete_record.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def dietRecords_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        results = {'data': user.dietrecords_set.all()}
        return JsonResponse(results)

@csrf_exempt
def dietRecords_add(request):
    if request.method == 'POST':
        data = request.body
        user = User.objects.get(id=request.session['user_id'])
        new_record = DietRecords(owner=user, evaluateResults=data.value)
        new_record.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def dietRecords_update(request):
    if request.method == 'POST':
        data = request.body
        product_id = data.get('product_id')
        diet_record = DietRecords.objects.get(id=product_id)
        diet_record.dietRecords = data.value
        diet_record.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def bmiRecords_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        results = {'data': user.bmirecords_set.all()}
        return JsonResponse(results)

@csrf_exempt
def bmiRecords_add(request):
    if request.method == 'POST':
        data = request.body
        user = User.objects.get(id=request.session['user_id'])
        new_record = BmiRecords(owner=user, evaluateResults=data.value)
        new_record.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def bmiRecords_update(request):
    if request.method == 'POST':
        data = request.body
        product_id = data.get('product_id')
        bmi_record = BmiRecords.objects.get(id=product_id)
        bmi_record.bmiRecords = data.value
        bmi_record.save()
        return JsonResponse({'status': 1}) # save success