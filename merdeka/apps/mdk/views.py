from django.shortcuts import render
from merdeka.apps.utils.func import find_model, make_response, json_response, jsonify, set_data, set_status, set_message, set_child
from .models import GoodsChilds

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

    # filtering goods and goodschild
    if _model == 'Goods':
        g = request.GET.get('goods', None)
        if g:
            records = model.objects.filter(commodity_id=g)
            # c = GoodsChilds.objects.filter(goods=records)
            # set_child(resp, [dict(
            #     id=_c.pk,
            #     name=_c.name,
            #     slug=_c.unique_name
            #     ) for _c in c])
    elif _model == 'GoodsChilds':
        g = request.GET.get('goods', None)
        if g:
            records = model.objects.filter(goods_id=g)

    set_message(resp, 'We found '+str(records.count())+' records.')

    if _model == 'Data':
        set_data(resp, [dict(
            id=r.pk,
            commodity=r.commodity.name,
            goods=r.goods.name,
            goods_child=r.goods_child.name,
            price=str(r.price),
            unit=r.unit.name,
            venue=r.venue.name,
            province=r.province.name,
            city=r.city.name
            ) for r in records])
    else:
        set_data(resp, [dict(
            id=r.pk,
            name=r.name,
            slug=r.unique_name
            ) for r in records])

    return json_response(resp)
