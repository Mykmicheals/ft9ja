
from django.urls import path
from .views import TraderDetailsView, GraphDataViews, AdminDashboardView

urlpatterns = [
    path('data/', TraderDetailsView.as_view()),
    path('graph/', GraphDataViews.as_view()),
    path('admin/', AdminDashboardView.as_view()),
]
