from django.shortcuts import render


def index(request):
    context = {
        'title': 'Recipes',
    }
    return render(request, 'main_page/index.html', context)