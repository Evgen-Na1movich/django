import datetime

import requests
from django.shortcuts import render

from catdog.models import AnimalImage
from src.settings import URL_FOR_CATS, URL_FOR_DOGS


def catdog_view(request):
    if request.method == 'GET':
        return render(request, 'catdog.html')
    if request.method == 'POST':
        request.session.set_expiry(30)
        if 'cat' in request.POST:
            responce = requests.get(URL_FOR_CATS)
            recponce_dict = responce.json()
            url = recponce_dict[0]['url']
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
            responce = requests.get(URL_FOR_DOGS)
            respone_dict = responce.json()
            url = respone_dict['message']
            content = {'url': url}
            type_image = url.split('.')[::-1]
            data_for_session = {'url': url,
                                'speicies': AnimalImage.CHOICES_SP[0][0],
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

def send_email(request):
    pass
