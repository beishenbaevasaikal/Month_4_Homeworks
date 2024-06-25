from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from . import models, forms


class RegistrationView(CreateView):
    form_class = forms.UserRegistrationForm
    template_name = "users/registration.html"
    success_url = "/login/"

    def form_valid(self, form):
        response = super().form_valid(form)
        age = form.cleaned_data["age"]
        if age < 5:
            self.object.club = "Категория не присваивается"
        elif 5 <= age <= 10:
            self.object.club = "Первая категория"
        elif 11 <= age <= 15:
            self.object.club = "Вторая категория"
        elif 16 <= age <= 25:
            self.object.club = "Высшая категория"
        else:
            self.object.club = "Категория не определена"
        self.object.save()
        return response


class AuthLoginView(LoginView):
    template_name = "users/login.html"
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse("users:user_list")


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


class ProfileListView(ListView):
    template_name = "users/profile_list.html"
    context_object_name = "profile"
    model = models.ProfileUser

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["club"] = getattr(self.request, "club", "Категория не определена")
        return context
