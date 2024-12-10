from django.urls import path
from .views import CriarMetaView

urlpatterns = [
    path('', CriarMetaView.as_view(), name='criar_meta'),
]
