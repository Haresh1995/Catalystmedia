from allauth.account.views import LoginView

class MyloginView(LoginView):
    template_name = 'login.html'