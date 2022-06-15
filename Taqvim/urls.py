from django.urls import path
from .views import UzTaqvim, RuTaqvim , KrTaqvim

urlpatterns = [
    path('uz/<int:pk>/', UzTaqvim, name="Lotincha-Taqvim"),
    path('ru/<int:pk>/', RuTaqvim, name="Russcha-Taqvim"),
    path('kr/<int:pk>/', KrTaqvim, name="Krilcha-Taqvim"),
]
