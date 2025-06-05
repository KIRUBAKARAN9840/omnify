from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer

from django.utils.timezone import now

class FitnessClassList(APIView):
    def get(self, request):
        classes = FitnessClass.objects.filter(date_time__gte=now()).order_by('date_time')
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)

class BookClass(APIView):
    def post(self, request):
        class_id = request.data.get('class_id')
        client_name = request.data.get('client_name')
        client_email = request.data.get('client_email')

        try:
            fitness_class = FitnessClass.objects.get(id=class_id)
        except FitnessClass.DoesNotExist:
            return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)

        if fitness_class.available_slots <= 0:
            return Response({'error': 'No slots available'}, status=status.HTTP_400_BAD_REQUEST)

        Booking.objects.create(
            fitness_class=fitness_class,
            client_name=client_name,
            client_email=client_email
        )
        fitness_class.available_slots -= 1
        fitness_class.save()

        return Response({'message': 'Booking successful'}, status=status.HTTP_201_CREATED)

class GetBookingsByEmail(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


