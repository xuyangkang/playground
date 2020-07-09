from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views
from django.conf.urls import include, url

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^fib', views.FibView.as_view(), name='fib'),
]