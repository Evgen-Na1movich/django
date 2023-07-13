import requests
from django.shortcuts import render


def catdog_view(request):
    if request.method == 'GET':
        return render(request, 'catdog.html')
    if request.method == 'POST':
        if 'cat' in request.POST:
            responce = requests.get('https://api.thecatapi.com/v1/images/search')
            content = {'url': responce.json()[0]['url']}
        elif 'dog' in request.POST:
            responce = requests.get('https://dog.ceo/api/breeds/image/random')
            content = {'url': responce.json()['message']}
        else:
            raise AttributeError(' at home')

    return render(request, 'pet.html', context=content)
