from django.shortcuts import redirect#,render
#from home.views import post


def login_redirect(request):
    return redirect('accounts/login/')

