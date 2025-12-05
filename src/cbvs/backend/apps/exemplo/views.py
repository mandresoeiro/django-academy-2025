from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = "exemplo/lista.html"
    context_object_name = "itens"


class ItemDetailView(DetailView):
    model = Item
    template_name = "exemplo/detalhe.html"
    context_object_name = "item"


class ItemCreateView(CreateView):
    model = Item
    fields = ["nome", "descricao"]
    template_name = "exemplo/form.html"
    success_url = reverse_lazy("exemplo:lista")


class ItemUpdateView(UpdateView):
    model = Item
    fields = ["nome", "descricao"]
    template_name = "exemplo/form.html"
    success_url = reverse_lazy("exemplo:lista")


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "exemplo/delete.html"
    success_url = reverse_lazy("exemplo:lista")
