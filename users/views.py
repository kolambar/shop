from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import UserForm
from users.models import User


# Create your views here.

class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    # def form_valid(self, form):
    #     product = form.save(commit=False)
    #     user = self.request.user
    #     form.instance.user = user
    #     form.instance.location = user.user_location
    #     form.save()
    #     return super(ProductCreateView, self).form_valid(form)

