import stripe
from django.urls import reverse
from .models import Item


def get_session(pk: int) -> str:
    """ Function to create a new session """
    item = Item.objects.get(pk=pk)
    session = stripe.checkout.Session.create(
        mode='payment',
        cancel_url=f"http://127.0.0.1:8000/payment/{reverse('items')}",
        success_url=f"http://127.0.0.1:8000/payment/{reverse('get_item', kwargs={'pk': pk})}",
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': item.price,
                    'product_data': {
                        'name': item.name,
                    },
                },
                'quantity': 1
            }
        ]
    )
    return session['id']
