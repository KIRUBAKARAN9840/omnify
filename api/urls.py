from django.urls import path
from .views import FitnessClassList, BookClass, GetBookingsByEmail

urlpatterns = [
    path('classes/', FitnessClassList.as_view(), name='classes'),
    path('book/', BookClass.as_view(), name='book'),
    path('bookings/', GetBookingsByEmail.as_view(), name='bookings-by-email'),
]
