from django.contrib import admin
from django.urls import include, path

from core.views import HomeView, UserHomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', UserHomeView.as_view(), name='user_home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('transactions/', include('transactions.urls', namespace='transactions')),
    path('loans/', include('loans.urls', namespace='loans')),
]
