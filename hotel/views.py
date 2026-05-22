from datetime import datetime

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import Booking
from django.contrib.auth import logout


def home(request):

    rooms = [

        {
            'name': 'Deluxe Room',
            'price': 2500,
            'status': 'Available'
        },

        {
            'name': 'Premium Room',
            'price': 4500,
            'status': 'Only 2 Left'
        },

        {
            'name': 'Suite Room',
            'price': 7000,
            'status': 'Fully Booked'
        }

    ]

    return render(request, 'home.html', {'rooms': rooms})


def rooms(request):

    return render(request, 'rooms.html')


def booking(request):

    if request.method == 'POST':

        room = request.POST['room']

        check_in = request.POST['check_in']

        check_out = request.POST['check_out']

        in_date = datetime.strptime(check_in, '%Y-%m-%d')

        out_date = datetime.strptime(check_out, '%Y-%m-%d')

        days = (out_date - in_date).days

        room_prices = {

            'Deluxe Room': 2500,
            'Premium Room': 4500,
            'Suite Room': 7000,

        }

        total_bill = room_prices[room] * days

        Booking.objects.create(

            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            room=room,
            check_in=check_in,
            check_out=check_out,
            total_bill=total_bill

        )

        context = {

            'name': request.POST['name'],
            'room': room,
            'days': days,
            'bill': total_bill,

        }

        return render(request, 'bill.html', context)

    return render(request, 'booking.html')


@login_required(login_url='/login/')
def dashboard(request):

    total_bookings = Booking.objects.count()

    total_rooms = 120

    booked_rooms = total_bookings

    available_rooms = total_rooms - booked_rooms

    context = {

        'total_rooms': total_rooms,
        'booked_rooms': booked_rooms,
        'available_rooms': available_rooms,
        'total_customers': total_bookings,

    }

    return render(request, 'dashboard.html', context)


@login_required(login_url='/login/')
def records(request):

    bookings = Booking.objects.all()

    return render(request, 'records.html', {'bookings': bookings})


def admin_login(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

    return render(request, 'login.html')


def admin_logout(request):

    logout(request)

    return redirect('/login/')


def admin_logout(request):

    logout(request)

    return redirect('/login/')