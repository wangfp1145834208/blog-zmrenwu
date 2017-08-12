from django.http import HttpResponse

def first_page(request):
    return HttpResponse("<p>Welcome to django practice.</p>")
