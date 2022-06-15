
from django.contrib import admin
from django.urls import path, include
from Taqvim.views import About
urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/', include('Taqvim.urls')),
    path('about/', About),
]
