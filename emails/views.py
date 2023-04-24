import os
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from dotenv import load_dotenv
from .models import ContactForm, Billing
from .serializers import ContactFormSerializer, BillingSerializer

# Find .env files in the directory and load environment variables
load_dotenv()


class ContactFormList(generics.ListAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer


class ContactFormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer


class ContactFormPost(generics.CreateAPIView):
    serializer_class = ContactFormSerializer

    def create(self, request, *args, **kwargs):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.data
            email = validated_data.get('email')
            subject = validated_data.get('subject')
            message = validated_data.get('message')
            try:
                data = ContactForm.objects.create(**validated_data)
                send_mail(
                    'Contact: {}'.format(subject),
                    'Message: {}'.format(message),
                    email,
                    [os.environ['EMAIL_HOST_USER']],
                    fail_silently=False,
                )
                return Response({'success': 'true'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'success': 'false', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BillingList(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

class BillingnDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

class BillingPost(generics.CreateAPIView):
	serializer_class = BillingSerializer

	def create(self, request, *args, **kwargs):
		srlz = BillingSerializer(data=request.data)
		if srlz.is_valid():
			validated_data = srlz.data
			email = validated_data.get('email')
			subject = validated_data.get('subject')
			message = validated_data.get('message')
			try:
				data = ContactForm.objects.create(**validated_data)
				send_mail(
					'Billing: {}'.format(subject),
					'Message: {}'.format(message),
					email,
					[os.environ['EMAIL_HOST_USER']],
					fail_silently=False,
				)
				return Response({'success': 'true' }, status=status.HTTP_201_CREATED)
			except Exception as e:
				return Response({'success': 'false', 'message': str(e) }, status=status.HTTP_400_BAD_REQUEST)