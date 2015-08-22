from django.shortcuts import render
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
    model = find_model('mdk', _model)

    # drop if model was not Found
    if model is None:
        set_status(resp, 'failed')
        set_message(resp, 'Model Not Found')
        return json_response(resp)

    q = request.GET.get('slug', None)
    records = model.objects.all()
    if q:
        records = model.objects.filter(unique_name=q)
    set_message(resp, 'We found '+str(records.count())+' records.')
    set_data(resp, [dict(
        id=r.pk,
        name=r.name,
        slug=r.unique_name
        ) for r in records])

    return json_response(resp)
