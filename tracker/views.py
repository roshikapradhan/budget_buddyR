from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
from django.shortcuts import render


def bill_split(request):
    # This view just renders the page where the JS handles the math
    return render(request, 'index.html')
def notifications(request):
    return render(request, 'index.html')