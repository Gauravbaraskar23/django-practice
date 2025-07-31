from django.shortcuts import render,HttpResponse ,redirect
from test_app.models import test
# Create your views here.
def home(request):
    data = test.objects.all() # getting all the data from the table to django
    # dict_on={
    #     'data':data,
    # }

    if request.method == 'POST':
        var1 = request.POST.get('name')
        var2 = request.POST.get('number')

        test_instance = test(name = var1,number = var2)
        test_instance.save()
        return redirect('home')
    return render(request, 'home.html',{'data':data,})
    # return HttpResponse("Hello, this is the home page!")  

