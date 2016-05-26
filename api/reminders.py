from model.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def medicineReminder_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        results = {'data': user.medicinereminder_set.all()}
        return JsonResponse(results)

@csrf_exempt
def medicineReminder_update(request):
    if request.method == 'POST':
        data = request.body
        product_id = data.get('product_id')
        medicine_reminder = MedicineReminder.objects.get(id=product_id)
        medicine_reminder.medicineReminder = data.value
        medicine_reminder.save()
        return JsonResponse({'status': 1})

@csrf_exempt
def medicineReminder_add(request):  
    if request.method == 'POST':
        data = request.body 
        user = User.objects.get(id=request.session['user_id'])
        new_result = EvaluateResults(owner=user, evaluateResults=data.value)
        new_result.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def medicineReminder_delete(request):
    if request.method == 'POST':
        data = request.body
        product_id = data.get('product_id')
        medicine_reminder = MedicineReminder.objects.get(id=product_id)
        medicine_reminder.delete()
        return JsonResponse({'status': 1})

@csrf_exempt
def sportsReminder_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        results = {'data': user.sportsreminder_set.all()}
        return JsonResponse(results)

@csrf_exempt
def sportsReminder_add(request):
    if request.method == 'POST':
        data = request.body
        user = User.objects.get(id=request.session['user_id'])
        new_result = EvaluateResults(owner=user, evaluateResults=data.value)
        new_result.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def sportsReminder_update(request):
    if request.method == "POST":
        data = request.body
        product_id = data.get('product_id')
        sports_reminder = SportsReminder.objects.get(id=product_id)
        sports_reminder.sportsReminder = data.value
        sports_reminder.save()
        return JsonResponse({'status': 1})

@csrf_exempt
def sportsReminder_delete(request):
    if request.method == "POST":
        data = request.body
        product_id = data.get('product_id')
        sports_reminder = SportsReminder.objects.get(id=product_id)
        sports_reminder.delete()
        return JsonResponse({'status': 1})

@csrf_exempt
def measurementReminder_get(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        results = {'data': user.measurementreminder_set.all()}
        return JsonResponse(results)

@csrf_exempt
def measurementReminder_add(request):
    if request.method == 'POST':
        data = request.body
        user = User.objects.get(id=request.session['user_id'])
        new_result = EvaluateResults(owner=user, evaluateResults=data.value)
        new_result.save()
        return JsonResponse({'status': 1}) # save success

@csrf_exempt
def measurementReminder_update(request):
    if request.method == "POST":
        data = request.body
        product_id = data.get('product_id')
        measurement_reminder = MeasurementReminder.objects.get(id=product_id)
        measurement_reminder.measurementReminder = data.value
        measurement_reminder.save()
        return JsonResponse({'status': 1})

@csrf_exempt
def measurementReminder_delete(request):
    if request.method == "POST":
        data = request.body
        product_id = data.get('product_id')
        measurement_reminder = MeasurementReminder.objects.get(id=product_id)
        measurement_reminder.delete()
        return JsonResponse({'status': 1})