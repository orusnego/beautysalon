from django.urls import path
from . import views
from .models import Beauty

urlpatterns = [
    path('brows', views.brows, name='brows'),
    path('brows/<int:procedure_id>', views.procedures_detail, name='brows.detail'),
    path('lashes', views.lashes, name='lashes'),
    path('lashes/<int:procedure_id>', views.procedures_detail, name='lashes.detail'),
    path('nails', views.nails, name='nails'),
    path('nails/<int:procedure_id>', views.procedures_detail, name='nails.detail'),
    path('hair', views.hair, name='hair'),
    path('hair/<int:procedure_id>', views.procedures_detail, name='hair.detail'),
]

