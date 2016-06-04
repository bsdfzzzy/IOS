from model.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def evaluateResults(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        datas = user.evaluateresults_set.all()
        results = {}
        for data in datas:
            product_id = data.id
            product_value = data.evaluateResults
            results[product_id] = product_value
        return JsonResponse(results)

    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=request.session['user_id'])
        new_result = EvaluateResults(owner=user, evaluateResults=data['value'])
        new_result.save()
        return JsonResponse({'status': 1}) # save success
