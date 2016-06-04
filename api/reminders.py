from model.models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def medicineReminder_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        datas = user.medicinereminder_set.all()
        results = {}
        for data in datas:
            product_id = data.id
            product_value = data.medicineReminder
            results[product_id] = product_value
        return JsonResponse(results)

@csrf_exempt
def medicineReminder_update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['product_id']
        medicine_reminder = MedicineReminder.objects.get(id=product_id)
        medicine_reminder.medicineReminder = data['value']
        medicine_reminder.save()
        return JsonResponse({'status': 1})

@csrf_exempt
def medicineReminder_add(request):  
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=request.session['user_id'])
        new_result = MedicineReminder(owner=user, medicineReminder=data['value'])
        new_result.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def medicineReminder_delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['product_id']
        medicine_reminder = MedicineReminder.objects.get(id=product_id)
        medicine_reminder.delete()
        return JsonResponse({'status': 1})

@csrf_exempt
def sportsReminder_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        datas = user.sportsreminder_set.all()
        results = {}
        for data in datas:
            product_id = data.id
            product_value = data.sportsRemainder
            results[product_id] = product_value
        return JsonResponse(results)

@csrf_exempt
def sportsReminder_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=request.session['user_id'])
        new_result = SportsReminder(owner=user, sportsRemainder=data['value'])
        new_result.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def sportsReminder_update(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data['product_id']
        sports_reminder = SportsReminder.objects.get(id=product_id)
        sports_reminder.sportsRemainder = data['value']
        sports_reminder.save()
        return JsonResponse({'status': 1})

@csrf_exempt
def sportsReminder_delete(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get('product_id')
        sports_reminder = SportsReminder.objects.get(id=product_id)
        sports_reminder.delete()
        return JsonResponse({'status': 1})

@csrf_exempt
def measurementReminder_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        datas = user.measurementreminder_set.all()
        results = {}
        for data in datas:
            product_id = data.id
            product_value = data.measurementReminder
            results[product_id] = product_value
        return JsonResponse(results)

@csrf_exempt
def measurementReminder_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=request.session['user_id'])
        new_result = MeasurementReminder(owner=user, measurementReminder=data['value'])
        new_result.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def measurementReminder_update(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data['product_id']
        measurement_reminder = MeasurementReminder.objects.get(id=product_id)
        measurement_reminder.measurementReminder = data['value']
        measurement_reminder.save()
        return JsonResponse({'status': 1})

@csrf_exempt
def measurementReminder_delete(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data['product_id']
        measurement_reminder = MeasurementReminder.objects.get(id=product_id)
        measurement_reminder.delete()
        return JsonResponse({'status': 1})
