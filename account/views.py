from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from lmestate.models import Agency


from .forms import UserSignupForm

class UserSignUp(SuccessMessageMixin,CreateView):
    model = User
    form_class = UserSignupForm
    success_url = reverse_lazy('address')
    success_message = "User created successfully"
    template_name = "account/register.html"
    def form_valid(self, form):
        super(UserSignUp,self).form_valid(form)
    # The form is valid, automatically sign-in the user
        user = authenticate(self.request, username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'])
        if user == None:
        # User not validated for some reason, return standard form_valid() response
            return self.render_to_response(self.get_context_data(form=form))
        else:
            # Log the user in
            login(self.request, user)
            # Redirect to success url
            return HttpResponseRedirect(self.get_success_url())


def login_view(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if Agency.objects.filter(agent=user).exists():
                return redirect("home")
            else:
                return redirect("create-agency")
        else:
            return redirect('login')
    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect("home")


