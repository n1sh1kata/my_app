from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
    'name': 'Giervan Melendres Sabalbero',
    }
    return render(request, "pages/index.html", context=context)
def portfolio(request):
    
    return render(request, "pages/portfolio.html")