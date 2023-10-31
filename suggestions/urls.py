from django.urls import path
from suggestions.views import ButtonSuggestionView, CustomSavedButtons

urlpatterns = [
  path('option-suggestions', ButtonSuggestionView.as_view(), name='suggestions'),
  path('option-save', CustomSavedButtons.as_view(), name='saved'),
]