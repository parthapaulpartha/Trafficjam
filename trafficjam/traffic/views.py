from django.shortcuts import render,HttpResponseRedirect, redirect
from django.http import JsonResponse
from django.db.models import Q

from traffic.forms import (
            SignupForm,
            SigninForm,
            Editprofile,
            createform,
            CityForm,
            ContactForm,
            CommentForm
        )
from django.contrib.auth.forms import (
            UserCreationForm,
            AuthenticationForm,
            UserChangeForm,
            PasswordChangeForm
        )
from django.contrib.auth import (
            authenticate,
            login,
            logout,
            update_session_auth_hash
        )
from django.contrib import messages
from .models import postcreate,City,Comment
import requests


def traffic_jam(request):
    return render(request, 'traffic/trafficjam.html')

# ------ For Sign up ---------
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, 'Success! Your account signup successfully')
           return redirect ('/trafficjam/signup')

    else:
        form = SignupForm()
        args = {'form': form}
    return render(request,'traffic/signup_form.html',args)

# ------ For Sign in ---------
def signin_view(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/trafficjam/home')

        else:
            messages.error(request, 'Username and Password did not matched')
            return redirect('trafficjam/signin/')
    else:
        form = SigninForm()
        args = {'form': form}
    return render(request, 'traffic/signin.html', args)

# ------ For Sign Out ---------
def signout_view(request):
    logout(request)
    return redirect('/trafficjam/signin/')


# ------ For view profile ---------
def profile(request):
    args = { 'user' : request.user }
    return render(request, 'traffic/profile.html', args)

# ------ For Edit profile ---------
def edit_profile(request):
    if request.method == 'POST':
        form = Editprofile(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update successfully')
            return redirect('/trafficjam/profile')
    else:
        form = Editprofile(instance=request.user)
        args = {'form': form}
        return render(request,'traffic/edit_profile.html', args)

# ------ For Change Password ---------
def Change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Change Successfully')
            return redirect('/trafficjam/profile')
        else:
            return redirect('/traffic/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request,'traffic/change_password.html', args)

# ---------- Create post -------
def create_post(request):
    if request.method == 'POST':
        form = createform(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.save()
            messages.success(request, "You successfully create the post")
            #return redirect('/trafficjam/post')

    form = createform()
    return render(request,'traffic/post.html', {'form':form})

# ---------- view post -------
def home(request):
    all_post = postcreate.objects.all()
    return render(request, 'traffic/home.html',{'all_post': all_post})

# ---------- Edit post -------
def edit_post(request, id=id):
    post = postcreate.objects.get(id=id)
    form = createform(request.POST or None, instance=post)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        #messages.success(request, "You successfully updated the post")
        return redirect('/trafficjam/home')

    else:
        context = {'form': form}
        return render(request, 'traffic/edit_post.html', context)

# ---------- Delete post -------
def delete_post(request,id):
    posts = postcreate.objects.get(id=id)
    posts.delete()
    return HttpResponseRedirect('/trafficjam/home')

# ---------- search post -------
def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = postcreate.objects.filter( Q(place_name__icontains = search) |
                                                Q(date_and_time__icontains = search))

            if match:
                return render(request,'traffic/search.html', {'sr':match})
            else:
                messages.error(request, 'No result found')
        else:
            return redirect('/trafficjam/search')

    return render(request,'traffic/search.html')

# ---------- Current Location -------
def current_location(request):
    return render(request,'traffic/map_location.html')

# ---------- Traffic map & Current Location -------
def trafficmap_location(request):
    return render(request,'traffic/trafficmap_location.html')

#---------- Satellite map & Current Location -------
def satellitemap_location(request):
    return render(request,'traffic/satellitemap_location.html')

# ---------- Current celsius weather -------
def weather_c(request):

    # for  Units = Fahrenheit
    #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=916a536da17fd879650a527bbcb93e5d'

    # for Units = Celsius
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=916a536da17fd879650a527bbcb93e5d'

    # for Units = Kelvin
    #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=916a536da17fd879650a527bbcb93e5d'

    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = City.objects.filter(name__icontains = search)

            if match:
                weather_data = []

                for city in match:
                    r = requests.get(url.format(city)).json()

                    city_weather = {
                        'city': city.name,
                        'temperature': r['main']['temp'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon'],
                    }
                    weather_data.append(city_weather)

                    # Its use for fixed city 1
                    city = 'Dhaka, BD'
                    r = requests.get(url.format(city)).json()

                    city_weather1 = {
                        'city': city,
                        'temperature': r['main']['temp'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon'],
                    }
                    # here end fixed city 1

                    # Its use for fixed city 2
                    city = 'Mymensingh, BD'
                    r = requests.get(url.format(city)).json()

                    city_weather2 = {
                        'city': city,
                        'temperature': r['main']['temp'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon'],
                    }
                    # here end fixed city 2

                    context = {'city_weather1': city_weather1, 'city_weather2': city_weather2,'weather_data': weather_data,}

                return render(request,'traffic/weather_c.html', context, {'sr':match},)

            else:
                messages.error(request, 'No result found')
        else:
            return redirect('/trafficjam/weather_c')

    #return render(request, 'traffic/weather_f.html')

    # Its use for fixed city 1
    city = 'Dhaka, BD'
    r = requests.get(url.format(city)).json()

    city_weather1 = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    # here end fixed city 1

    # Its use for fixed city 2
    city = 'Mymensingh, BD'
    r = requests.get(url.format(city)).json()

    city_weather2 = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    # here end fixed city 2

    context = {'city_weather1': city_weather1, 'city_weather2': city_weather2,}
    return render(request, 'traffic/weather_c.html', context)


# ---------- Current Fahrenheit weather -------
def weather_f(request):
    # for  Units = Fahrenheit
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=916a536da17fd879650a527bbcb93e5d'

    # for Units = Celsius
    #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=916a536da17fd879650a527bbcb93e5d'

    # for Units = Kelvin
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=916a536da17fd879650a527bbcb93e5d'


    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = City.objects.filter(name__icontains = search)

            if match:
                weather_data = []

                for city in match:
                    r = requests.get(url.format(city)).json()

                    city_weather = {
                        'city': city.name,
                        'temperature': r['main']['temp'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon'],
                    }
                    weather_data.append(city_weather)

                    # Its use for fixed city 1
                    city = 'Dhaka, BD'
                    r = requests.get(url.format(city)).json()

                    city_weather1 = {
                        'city': city,
                        'temperature': r['main']['temp'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon'],
                    }
                    # here end fixed city 1

                    # Its use for fixed city 2
                    city = 'Mymensingh, BD'
                    r = requests.get(url.format(city)).json()

                    city_weather2 = {
                        'city': city,
                        'temperature': r['main']['temp'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon'],
                    }
                    # here end fixed city 2

                    context = {'city_weather1': city_weather1, 'city_weather2': city_weather2,'weather_data': weather_data,}

                return render(request,'traffic/weather_f.html', context, {'sr':match},)

            else:
                messages.error(request, 'No result found')
        else:
            return redirect('/trafficjam/weather_f',)

    #return render(request, 'traffic/weather_f.html')

    # Its use for fixed city 1
    city = 'Dhaka, BD'
    r = requests.get(url.format(city)).json()

    city_weather1 = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    # here end fixed city 1

    # Its use for fixed city 2
    city = 'Mymensingh, BD'
    r = requests.get(url.format(city)).json()

    city_weather2 = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    # here end fixed city 2

    context = {'city_weather1': city_weather1, 'city_weather2': city_weather2,}
    return render(request, 'traffic/weather_f.html', context)


# ---------- About us -------
def about_us(request):
    return render(request,'traffic/about_us.html')

# ---------- Contact us -------
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.save()

    form = ContactForm()
    return render(request,'traffic/contact_us.html', {'form':form})

# ---------- Comment -------
def comment(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.save()

    form = CommentForm()
    #comments = Comment.objects.all()
    return render(request,'traffic/comment.html', {'form':form})

# ---------- view Comment -------
def comment_view(request):
    comments = Comment.objects.all()
    return render(request, 'traffic/comments_view.html',{'comments': comments})
