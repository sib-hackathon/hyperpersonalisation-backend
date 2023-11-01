from django.urls import path
from transactions.views import DebitLimitSuggester

urlpatterns = [
    path('api/limit-suggester/', DebitLimitSuggester.as_view(), name='limit-suggester'),
]
