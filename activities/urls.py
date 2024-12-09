from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('theorical_activity/', views.activity_view, name='activity_view'),
    path('interactive_activity/', views.activity_view, name='activity_view'),
     path('mcq_activity/', views.activity_view, name='activity_view'),
]