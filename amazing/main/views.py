from django.shortcuts import render

def contact(request):
    return render(request, 'main/contact.html')
def gallery(request):
    return render(request, 'main/gallery.html')
def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def service(request):
    return render(request, 'main/service.html')
def why(request):
    return render(request, 'main/why.html')

# Create your views here.
