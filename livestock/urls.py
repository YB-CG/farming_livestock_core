from .views import CreateLivestockView, RetrieveUpdateDeleteLivestockView
from django.urls import path


urlpatterns = [
    path("livestock/", CreateLivestockView.as_view(), name="register_Livestock"),
    path("livestock/<pk>/",RetrieveUpdateDeleteLivestockView.as_view(), name="livestock"),
]