from django.urls import path
from . import views

urlpatterns = [
    path('<int:procedure_id>', views.chooseUslugi, name='uslugi'),
    path('master/<int:procedure_id>', views.chooseMaster, name='master'),
    path('master/booking/<int:master_id>/<int:procedure_id>', views.chooseTime, name='booking'),
    path('master/booking/finish/<int:master_id>/<int:procedure_id>/<int:time_id>', views.finishBooking, name='finish'),
]