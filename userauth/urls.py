
from .views import SignupView, CustomTokenObtainPairView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),


    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
