from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


from django.http import HttpResponse
import datetime
from .forms import CheckinnForm, CheckoutForm, DashboardForm
from .models import Attendance


def entry(request):
    user = request.user
    if request.method == "POST":

        form = CheckinnForm(request.POST)
        today_date = datetime.date.today()
        print "inside"
        print ("form")
        print form.is_valid()
        if form.is_valid():
            date1 = form.cleaned_data['date']
            checkinn1 = form.cleaned_data['checkinn']
            print (date1)
            print (checkinn1)

            checking = Attendance.objects.filter(date=date1)
            if (checking):

                return render(request, 'exception.html', {})
            else:
                profile = Attendance()
                profile.date = date1
                profile.checkinn = checkinn1
                profile.created_by = user
                profile.created_date = today_date
                profile.checkout="00:00:00"
                profile.early = "00:00:00"
                profile.extended1 = "00:00:00"
                profile.user = user
                profile.save()
            return redirect(entry)
            # except:
            # return HttpResponse('Make sure all fields are entered and
            # valid.')
    else:
        form = CheckinnForm()
    return render(request, 'tracker.html', {'form': form})


def details(request):
    return render(request, 'profile.html', {})


import datetime


def exit_out(request):
    user = request.user
    if request.method == "POST":

        form = CheckoutForm(request.POST)

        print "inside"
        print ("form")
        print form.is_valid()
        if form.is_valid():
            date1 = form.cleaned_data['date']
            checkout = form.cleaned_data['checkout']

            print (date1)
            print (checkout)
            print "hello"
            checking = Attendance.objects.get(date=date1)
            print ("checking", checking)
            if (checking):
                print "hi"
                checking.checkout = checkout
                checkinn = checking.checkinn
                a = str(checkout)
                b = str(checkinn)
                print a
                c = datetime.datetime.strptime(b, '%H:%M:%S')
                print c
                d = datetime.datetime.strptime(a, '%H:%M:%S')
                print "d", d
                f = d - c
                print "f", f
                checking.worked_for = f
                x = str(f)
                m = datetime.datetime.strptime(x, '%H:%M:%S')
                g = "08:30:00"
                h = datetime.datetime.strptime(g, '%H:%M:%S')
                print h

                l = m - h
                print l
                q = str(l)
                o = l.total_seconds()
                print "o", o
                k = str(l)
                if(o > 0):

                    z = str(datetime.timedelta(seconds=o))
                    print z
                    print type(z)
                    q = datetime.datetime.strptime(z, '%H:%M:%S')
                    print "q", q
                    checking.extended1 = z
                    checking.early = "00:00:00"
                    checking.save()
                elif(o < 0):
                    k = abs(o)
                    q = str(datetime.timedelta(seconds=k))
                    checking.extended1 = "00:00:00"
                    checking.early = q
                    checking.save()
                elif(o == 0):
                    checking.extended1 = "00:00:00"
                    checking.early = "00:00:00"
                    checking.save()

            return redirect(exit_out)

    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})


import datetime as dt
import datetime


def dashboard(request):
    user = request.user
    print ("user",user)
    if request.method == "POST":

        form = DashboardForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            fdate = form.cleaned_data['fdate']
            tdate = form.cleaned_data['tdate']
            print fdate
            print tdate
            attendance = Attendance.objects.filter(date__range=[fdate, tdate],user=user)
            b = "00:00:00"
            t2 = dt.datetime.strptime(b, '%H:%M:%S')

            t3 = dt.datetime.strptime(b, '%H:%M:%S')
            for items in attendance:

                a = str(items.extended1)
                print a, "a"
                print type(a)
                t1 = dt.datetime.strptime(a, '%H:%M:%S')
                time_zero = dt.datetime.strptime('00:00:00', '%H:%M:%S')
                t2 = (t1 - time_zero + t2)
                t5 = t2.strftime('%H:%M:%S')
                b = str((items.early))
                t4 = dt.datetime.strptime(b, '%H:%M:%S')
                time_one = dt.datetime.strptime('00:00:00', '%H:%M:%S')
                t3 = (t4 - time_zero + t3)

                t6 = t3.strftime('%H:%M:%S')
            print ("t6", t6)
            print ("t5", t5)
            t7 = datetime.datetime.strptime(t5, '%H:%M:%S')
            t8 = datetime.datetime.strptime(t6, '%H:%M:%S')
            total1 = t7 - t8
            print (total1.total_seconds())
            if (total1.total_seconds()) < 0:
                print "negative value"
                tot = abs(total1.total_seconds())
                print tot, "tot"
                total2 = str(datetime.timedelta(seconds=tot))
                print "total", total2
                total = "-" + total2

            else:
                print "positive value"
                total = total1
            return render(
                request, 'details.html', {
                    'posts': attendance, 'plus': t5, 'minus': t6, "status": total})
    else:
        form = DashboardForm()
    return render(request, 'dashboard.html', {'form': form})


def post_list(request):
    return render(request, 'home.html')

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
