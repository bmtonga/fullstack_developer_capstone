from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # API authentication endpoints
    path('login', views.login_user, name='login'),
    path('register', views.registration, name='register'),
    path('logout', views.logout_request, name='logout'),

    # Car data endpoints
    path('get_cars', views.get_cars, name='get_cars'),

    # Dealership endpoints
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='get_dealer_details'),
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('add_review', views.add_review, name='add_review'),
]