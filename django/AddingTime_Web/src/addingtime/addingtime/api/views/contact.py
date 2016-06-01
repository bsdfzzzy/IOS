from model.models import *
from utils import *

from datetime import datetime
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger('API.app')

@csrf_exempt
def contact_create(request):
    user_id = request.session.get('user_id', 0)
    result, data = post_json_session_check(request, user_id)
    if result != Status.OK:
        return JsonResponse(result)

    source_id = data.get('source_id', 1)
    contacts, contact_ids = data.get('contacts', []), []
    if len(contacts) > LIST_LIMIT:
        return JsonResponse(message_response(Status.LIST_LIMIT_ERROR))

    try:
        for elem in contacts:
            contact = Contact(owner_id = user_id, source_id = source_id)
            contact = data_to_contact(contact, elem)
            contact.save()
            contact_ids.append(contact.id)

        # Build the response
        response = {}
        response['status'] = Status.OK
        response['ids'] = contact_ids
    except Exception as e:
        logger.error(e)
        response = message_response(Status.FAIL)

    return JsonResponse(response)

@csrf_exempt
def contact_delete(request):
    user_id = request.session.get('user_id', 0)
    result, data = post_json_session_check(request, user_id)
    if result != Status.OK:
        return JsonResponse(result)

    ids = data.get('ids', [])
    try:
        Contact.objects.filter(pk__in = ids, owner_id = user_id)\
            .update(is_delete = True)
        response = message_response(Status.OK)
    except Exception as e:
        logger.error(e)
        response = message_response(Status.FAIL)

    return JsonResponse(response)

@csrf_exempt
def contact_get_all(request, offset):
    user_id = request.session.get('user_id', 0)
    if user_id == 0:
        return JsonResponse(message_response(Status.SESSION_EXPN))

    try:
        contacts = Contact.objects.filter(owner_id = user_id,
            is_delete = False)[int(offset) : int(offset) + LIST_LIMIT]

        response = {}
        response['status'] = Status.OK
        response['contacts'] = []
        for contact in contacts:
            response['contacts'].append(contact_to_data(contact))
    except Exception as e:
        logger.error(e)
        response = message_response(Status.FAIL)

    return JsonResponse(response)

@csrf_exempt
def contact_update(request):
    user_id = request.session.get('user_id', 0)
    result, data = post_json_session_check(request, user_id)
    if result != Status.OK:
        return JsonResponse(result)

    contact_id = data.get('id', 0)
    try:
        contact = Contact.objects.get(pk = contact_id, owner_id = user_id,
            is_delete = False)
        contact = data_to_contact(contact, data.get('contact', {}))
        contact.save()
        response = message_response(Status.OK)
    except Exception as e:
        logger.error(e)
        response = message_response(Status.FAIL)

    return JsonResponse(response)

###############################################################################
#                                Help Function                                #
###############################################################################
def data_to_contact(contact, data):
    if not data:
        return contact

    contact.name = data.get('name', '')
    contact.email = data.get('email', '')
    contact.phone = data.get('phone', '')
    return contact

def contact_to_data(contact):
    return {
        'id': contact.id,
        'name': contact.name,
        'email': contact.email,
        'phone': contact.phone
    }
