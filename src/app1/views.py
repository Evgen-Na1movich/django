import csv
import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect


def get_data(request):
    data = datetime.datetime.now()
    return HttpResponse(data)


def two_pow(request, number):
    result = 2 ** int(number)
    return HttpResponse(f'2 ** {number} = {result} ')


def google_redirect(request):
    return redirect('http://google.com')


def hello_admin(request):
    return HttpResponse("Hello, Admin!")


def hello_guest(request, guest):
    return HttpResponse(f"Hello, {guest}!")


def hello_user(request, name):
    if name == 'admin':
        return redirect('admin')
    else:
        return redirect('hello_guest', guest=name)


def my_word(request, word):
    if len(word) % 2:
        # endpoin 'get_time' берется из urls.py
        # path('', get_data, name='get_time')
        # из 'переменной' name
        return redirect('get_time')
    else:
        return HttpResponse(f"{word[::2]}")


def login(request):
    if request.POST.get == 'POST':
        pass
    else:
        name2 = request.GET.get('name')
        return redirect('fun_success', name_success=name2)


def success(request, name_success):
    return HttpResponse(f"Hello {name_success}")


def add_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        if not os.path.exists('django_04.csv'):
            with open('django_04.csv', 'w') as file:
                fildnames = ['name', 'lastname', 'age']
                csvwriter = csv.DictWriter(file, fieldnames=fildnames)
                csvwriter.writeheader()
        with open('django_04.csv', 'a') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow([name, lastname, age])
        return HttpResponse(f'Data saved: Name - {name}, '
                            f'Lastname - {lastname}, '
                            f' age- {age}')
    else:
        pass
