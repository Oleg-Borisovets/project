from . import models

def harvest_data(cbv_obj):
    current_cart_pk = cbv_obj.request.session.get('current_cart_pk')
    cart_items = cbv_obj.request.GET
    return current_cart_pk, cart_items


def update_items_in_cart(cart_items_from_form, current_cart_pk):
    action = None
    cart = models.Cart.objects.filter(pk=current_cart_pk).first()
    if not cart:
        return
    goods = cart.book.all()   
    for name, quantity in cart_items_from_form.items():
        if name == 'btn':
            action = quantity
            continue
        good = goods.filter(pk=name.split("_")[-1]).first()
        if good and int(quantity) > 0:
            good.quantity=quantity
            good.save()
        else:
            good.delete()    
    return action        