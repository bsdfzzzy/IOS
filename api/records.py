from model.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def diabeteRecords_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        datas = user.diabeterecords_set.all()
        results = {}
        for data in datas:
            product_id = data.id
            product_value = data.diabeteRecords
            results[product_id] = product_value
        return JsonResponse(results)

@csrf_exempt
def diabeteRecords_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=request.session['user_id'])
        new_record = DiabeteRecords(owner=user, diabeteRecords=data['value'])
        new_record.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def diabeteRecords_update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['product_id']
        diabete_record = DiabeteRecords.objects.get(id=product_id)
        diabete_record.diabeteRecords = data['value']
        diabete_record.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def dietRecords_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
	datas = user.dietrecords_set.all()
        results = {}
        for data in datas:
            product_id = data.id
            product_value = data.dietRecords
            results[product_id] = product_value
        return JsonResponse(results)

@csrf_exempt
def dietRecords_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=request.session['user_id'])
        new_record = DietRecords(owner=user, dietRecords=data['value'])
        new_record.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def dietRecords_update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['product_id']
        diet_record = DietRecords.objects.get(id=product_id)
        diet_record.dietRecords = data['value']
        diet_record.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def bmiRecords_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        datas = user.bmirecords_set.all()
        results = {}
        for data in datas:
            product_id = data.id
            product_value = data.bmiRecords
            results[product_id] = product_value
        return JsonResponse(results)

@csrf_exempt
def bmiRecords_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=request.session['user_id'])
        new_record = BmiRecords(owner=user, bmiRecords=data['value'])
        new_record.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def bmiRecords_update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['product_id']
        bmi_record = BmiRecords.objects.get(id=product_id)
        bmi_record.bmiRecords = data['value']
        bmi_record.save()
        return JsonResponse({'status': 1}) # save success
