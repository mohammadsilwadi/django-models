from .views import SnackListView,SnackListDetail
from django.urls import path

urlpatterns = [
    path("", SnackListView.as_view(), name="snack_list"),
    path("<int:pk>/", SnackListDetail.as_view(), name="snack_detail"),
]