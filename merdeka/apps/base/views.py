from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from merdeka.apps.utils.func import find_model, make_response, json_response, jsonify, set_data, set_status, set_message
from .forms import LoginForm, RegisterForm

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

def user_login(request):
    resp = make_response()
    if not request.is_ajax() or request.method != 'POST':
    # if request.method != 'POST':
        set_status(resp, 'failed')
        set_message(resp, 'Request Not Found.')
        resp.pop('data')
        resp.pop('errors')
        resp.pop('fields')
        return json_response(resp)

    if request.user.is_authenticated():
        set_status(resp, 'failed')
        set_message(resp, 'You have been already logged in.')
        return json_response(resp)

    f = LoginForm(request.POST)
    if f.is_valid():
        _r = auth(request, f)
        set_status(resp, _r['status'])
        set_message(resp, _r['message'])
        if _r['status'] == 'failed':
            resp.pop('data')
            resp.pop('errors')
            resp.pop('fields')
    else:
        set_status(resp, 'failed')
        set_message(resp, 'Invalid Data.')
        set_errors(resp, f.errors)
        resp.pop('data')
        resp.pop('fields')
    return json_response(resp)

def auth(request, form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(username=username, password=password)
    resp = dict(
        status='error',
        message='Somethings wrong, please contact the administrator or try again.'
        )
    if user is not None and user.is_active:
        login(request, user)
        resp.update({'status': 'success', 'message': 'Login Successfull.'})

    return resp

def user_register(request):
    resp = make_response()
    if not request.is_ajax() or request.method != 'POST':
    # if request.method != 'POST':
        set_status(resp, 'failed')
        set_message(resp, 'Request Not Found.')
        resp.pop('data')
        resp.pop('errors')
        resp.pop('fields')
        return json_response(resp)

    if request.user.is_authenticated():
        set_status(resp, 'failed')
        set_message(resp, 'You have been already logged in.')
        return json_response(resp)

    f = RegisterForm(request.POST)
    if f.is_valid():
        f.save()
        auth(request, f)
    else:
        set_status(resp, 'failed')
        set_message(resp, 'Registration Failed, Please check your form and try again.')
        resp.pop('data')
        resp.pop('errors')
        resp.pop('fields')
    return json_response(resp)
