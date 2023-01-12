"""
taskrabbit URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from core.views import index, sign_up
import core.customer.urls
import core.courier.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("login/", LoginView.as_view(template_name="login.html"), name='login'),
    path("logout/", LogoutView.as_view(next_page="/"), name='logout'),
    path("sign-up", sign_up, name='sign_up'),
    path("customer/", include(core.customer.urls, namespace="customer")),
    path("courier/", include(core.courier.urls, namespace="courier")),
]
