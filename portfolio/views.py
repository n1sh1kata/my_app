from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
    'name': 'Giervan Melendres Sabalbero',
    }
    return render(request, "pages/index.html", context=context)
def portfolio(request):
    return render(request, "pages/portfolio.html")

#     Context Data:
# a. In views.py, create an array of dictionaries containing sample data to be
# displayed
# data = [
# {"title": "Users", "count": 150},
# {"title": "Orders", "count": 320},
# {"title": "Revenue", "count": "12450"},
# ]

def dashboard(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
        ]
    return render(request, "pages/dashboard.html", context={"data": data})