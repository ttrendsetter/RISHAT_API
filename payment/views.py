from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, DetailView

from .models import Item
from .context import context as ctx
from .main import *


# Create your views here.
def get_session_view(request, pk):
    session = get_session(pk)
    return HttpResponse(session)


class ItemDetailView(DetailView):
    model = Item
    model.public_key = ctx.pk
    template_name = 'item_detail.html'
    context_object_name = 'item'


class ItemsView(ListView):
    model = Item
    template_name = 'items.html'
    context_object_name = 'items'


class CreateItemView(CreateView):
    model = Item
    fields = ['name', 'description', 'price']
    template_name = 'create_item.html'
