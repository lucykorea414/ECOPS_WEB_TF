from django.shortcuts import render

# Create your views here.

def login(request):
    # if request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     search_email = data['email']
    #     obj = Account.objects.get(email=search_email)

    #     if data['password'] == obj.password:
    #         return HttpResponse(status=200)
    #     else:
    #         return HttpResponse(status=400)
    # elif request.method == "GET":
    #     return render(request, 'users/login.html')
    return render(request, 'users/login.html')