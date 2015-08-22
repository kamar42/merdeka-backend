import json
from django.apps import apps
from django.db import IntegrityError
from django.shortcuts import HttpResponse

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def make_response():
    return dict(
        status='success',
        message='',
        data='',
        errors='',
        fields=''
        )

def find_model(app_label, model):
    try:
        return apps.get_model(app_label=app_label, model_name=model)
    except LookupError:
        return None

def jsonify(data):
    return json.dumps(data)

def json_response(data):
    return HttpResponse(jsonify(data), content_type='application/json')

def set_status(resp, data):
    resp.update({'status': data})

def set_message(resp, data):
    resp.update({'message': data})

def set_data(resp, data):
    resp.update({'data': data})

def set_errors(resp, data):
    resp.update({'errors': data})

def set_fields(resp, data):
    resp.update({'fields': data})
