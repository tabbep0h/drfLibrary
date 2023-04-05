from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.BookAPIList.as_view()),
    path('books/<int:pk>/', views.BookAPIDetail.as_view()),
    path('orders/', views.OrderAPIList.as_view()),
    path('orders/<int:pk>/', views.OrderAPICreate.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
