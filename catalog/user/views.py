from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("Giriş başarılı")
            return redirect('index')
        else:
            print("Geçersiz kimlik bilgileri")
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def register(request):

    if request.method == "POST":
        # print("submitted")
        # get form values
        username =request.POST['username']
        email =request.POST['email']
        password =request.POST['password']
        repassword =request.POST['repassword']

        if password == repassword:
            # Username kontrolu
            if User.objects.filter(username= username).exists():
                print("Bu kullanıcı adı önceden alınmıs")
                return redirect('register')
            else:
                if User.objects.filter(email= email).exists():
                    print("Bu email adresi önceden alınmıs")
                    return redirect('register')
                else:
                    # print("Her sey guzel")
                    user = User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    print("Kullanıcı oluşturuldu")
                    return redirect('login')


        else:
            print("Paralolar eşleşmiyor")
            return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    return render(request, 'user/logout.html')


