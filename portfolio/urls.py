"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

urlpatterns = [
# admin urls
    path('admin/', admin.site.urls),

# custom registration path to use via browser
    path('accounts/register/',
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/",
         ), name="django_registration_register"),

# other urls used by django registration package
    path('accounts/',
         include("django_registration.backends.one_step.urls")),

# login path to use via browser
    path('accounts/',
         include("django.contrib.auth.urls")),

# login via browsable api
    path('api-auth/',
         include("rest_framework.urls")),

    path('api/',
         include("users.api.urls")),

    path('api/',
         include("posts.api.urls")),

# login via REST
    path('api/rest-auth/',
         include("rest_auth.urls")),

# registraton via REST
    path('api/rest-auth/registration/',
         include("rest_auth.registration.urls")),

#uses a catch-all regular expression to redirect all other links to this page
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")

]
