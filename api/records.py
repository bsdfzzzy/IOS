from model.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def medicineReminder(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        results = {'data': user.evaluateresults_set.all()}
        return JsonResponse(results)

    if request.method == 'POST':
        data = request.body
        new_result = EvaluateResults(evaluateResults=data.value)
        new_result.save()
        return JsonResponse({'status': 1}) # save success