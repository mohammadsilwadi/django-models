from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snack


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
# Create your views here.
class SnackListDetail(DetailView):
    template_name = "snack_detail.html"
    context_object_name="snack_object"
    model=Snack