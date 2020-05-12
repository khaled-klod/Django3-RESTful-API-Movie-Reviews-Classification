from django.urls import path
from .views import api_sentiment_pred

app_name = 'modeling'

urlpatterns = [
    path('api/predict/', api_sentiment_pred, name='api_sentiment_pred'),
]