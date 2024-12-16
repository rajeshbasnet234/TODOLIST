from django.shortcuts import render, HttpResponse

# Create your views here.
def home (request):
    person = [
        {'name':'Rajesh','age': 26},
        {'name':'Anuja','age':18},
        {'name':'Rajesh','age': 26},
        {'name':'Anuja','age':18},
        {'name':'Rajesh','age': 26},
        {'name':'Anuja','age':18},
        {'name':'Rajesh','age': 26},
        {'name':'Anuja','age':18}
    ]

    context = {
        "name" :"Rajesh",
        "persons":person
    }
    return render( request,'index.html',context)

def contact (request):
    return HttpResponse("This is contact page")
