import datetime

import requests
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from catdog.forms import PetFilterForm
from catdog.models import AnimalImage
from src.settings import URL_FOR_CATS, URL_FOR_DOGS, EMAIL_HOST_USER


def catdog_view(request):
    if request.method == 'GET':
        data = {'form': PetFilterForm()}
        return render(request, 'catdog.html', data)
    if request.method == 'POST':
        request.session.set_expiry(30)
        if 'cat' in request.POST:
            response = requests.get(URL_FOR_CATS)
            recponse_dict = response.json()
            url = recponse_dict[0]['url']
            type_image = url.split('.')[::-1]
            content = {'url': url}
            data_for_session = {'url': url,
                                'speicies': AnimalImage.CHOICES_SP[0][0],
                                'type': type_image
                                }
            request.session['data_for_session'] = data_for_session

            # AnimalImage.objects.create(url=url, speicies=AnimalImage.CHOICES_SP[0][0],
            #                            create_at=datetime.datetime.now(), type=type_image)

        elif 'dog' in request.POST:
            response = requests.get(URL_FOR_DOGS)
            response_dict = response.json()
            url = response_dict['message']
            content = {'url': url}
            type_image = url.split('.')[::-1]
            data_for_session = {'url': url,
                                'speicies': AnimalImage.CHOICES_SP[1][0],
                                'type': type_image
                                }
            request.session['data_for_session'] = data_for_session
            # AnimalImage.objects.create(url=url, speicies=AnimalImage.CHOICES_SP[1][0],
            #                            create_at=datetime.datetime.now(), type=type_image)
        else:
            raise AttributeError(' at home')

        return render(request, 'pet.html', context=content)


def save_gatdog(request):
    if request.method == "POST":
        data_for_write = request.session['data_for_session']
        AnimalImage.objects.create(url=data_for_write['url'], speicies=data_for_write['speicies'],
                                   type=data_for_write['type'],
                                   )
        data = {'url': data_for_write['url']}
        return render(request, 'pet_saved.html', context=data)


def send_image_to_email(request):
    url = request.POST.get('url_for_image')
    send_mail(
        "Subject here",
        f"Here is the message - {url}.",
        EMAIL_HOST_USER,
        [mail_for_send],
        fail_silently=False,
    )
    return render(request, 'pet_saved.html', { 'url' : url})


def pet_filter(request):
    if request.method == 'POST':
        form = PetFilterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pets = AnimalImage.objects.filter(speicies=data.get('pet'))
            return render(request, 'pet_filter.html', context={'pets': pets})
