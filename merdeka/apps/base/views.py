from django.shortcuts import redirect, render
from merdeka.apps.utils.func import find_model, make_response, json_response, jsonify, set_data, set_status, set_message

def api_view(request, **kwargs):
    resp = make_response()
    m = kwargs.get('model', None)

    # drop if model is empty
    if m is None:
        set_status(resp, 'failed')
        set_message(resp, 'Model Not Found')
        return json_response(resp)

    if '_' in m:
        _model = ''
        for _m in m.split('_'):
            _model += _m[:1].upper() + _m[1:].lower()
    else:
        _model = m[:1].upper() + m[1:].lower()
    model = find_model('merdeka.apps.base', _model)

    # drop if model was not found
    if model is None:
        set_status(resp, 'failed')
        set_message(resp, 'Model Not Found')
        q = request.GET
        for _q in q:
            print q[_q]
        return json_response(resp)

    return json_response(resp)

def merdeka_view(request):
    return render(request, 'base/merdeka.html', locals())
