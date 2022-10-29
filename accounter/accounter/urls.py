
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api_income/", include("incomes.urls"), name="api_income"),
]
