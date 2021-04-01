from django.shortcuts import render


def home(request):
    """
    ホームページ用のView
    """
    return render(request, 'home.html')
