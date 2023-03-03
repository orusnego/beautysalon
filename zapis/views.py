from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from masters.models import Master, Review, Work
from beauty.models import typeBeauty, Beauty
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, BookingTime, BookingDays, BookingSlots
from .forms import AppointmentForm
import datetime
import pytz
from datetimerange import DateTimeRange
from django.db import IntegrityError

from .telegrambot import send_message




def chooseType(request):
    types = typeBeauty.objects.all()
    return render(request, 'type.zapis.html', {'types':types})

def chooseUslugi(request, procedure_id):
    uslugi = Beauty.objects.filter(procedures=procedure_id)
    return render(request, 'usluga.zapis.html',
    {'uslugi':uslugi})

def chooseMaster(request, procedure_id):
    procedure = get_object_or_404(Beauty, pk=procedure_id)
    masters = Master.objects.filter(profession__type = procedure.procedures)
    return render(request, 'master.zapis.html',
    {'procedure': procedure,
    'masters': masters})

def chooseTime(request, procedure_id, master_id):
    master = get_object_or_404(Master,pk=master_id)
    procedure = get_object_or_404(Beauty,pk=procedure_id)
    booking_days = BookingDays.objects.all()
    appointments = Appointment.objects.all()
    times = BookingTime.objects.all()
    sorted_times = []
    for time in times:
        sorted_times.append(time)
        for app in appointments:
            if time == app.time:
                try:
                    sorted_times.remove(time)
                    continue
                except ValueError:
                    continue

    return render(request, 'createform.html',
        {'procedure':procedure,
        'master':master,
        'booking_days':booking_days,
        'times':times,
        'sorted_times':sorted_times,
        'appointments':appointments
        })

def finishBooking(request, procedure_id, master_id, time_id):
    master = get_object_or_404(Master,pk=master_id)
    procedure = get_object_or_404(Beauty,pk=procedure_id)
    time = get_object_or_404(BookingTime,pk=time_id)
    if request.method == 'GET':
        return render(request, 'finishbooking.html',
            {'form': AppointmentForm,
            'master': master,
            'procedure': procedure,
            'time': time})
    else:
        try:
            appointment = Appointment.objects.create(
            procedure = procedure,
            master = master,
            time=time,
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            phone = request.POST['phone'])
            appointment.save()
            send_message(chat_id='197670320', text=f'Новая запись от {appointment.first_name} {appointment.last_name}\nМастер: {appointment.master.name}\nПроцедура: {appointment.procedure}\nВремя и дата: {appointment.time.days} {appointment.time.start_time}\nНомер телефона: +7{appointment.phone}')
            return render(request, 'congrat.model.html',
                {'master': master,
                 'procedure': procedure,
                 'time': time}
            )
        except IntegrityError:
            return render(request,
                'finishbooking.html',
            {'form':AppointmentForm, 'error':'Ошибка.'})

