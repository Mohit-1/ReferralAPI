from rest_framework import generics, status
from .serializers import PartnerSerializer, ReferralSerializer
from .models import Partner, Referral
from rest_framework.response import Response
from rest_framework.views import APIView

class RetrieveRefCode(APIView):
	def get(self, request):
		user_id = self.request.query_params.get('user_id', None)
		if user_id is not None and user_id != "":
			try:
				partner = Partner.objects.get(id=user_id)
			except Partner.DoesNotExist:
				return Response(status=status.HTTP_400_BAD_REQUEST)

			return Response({"referral code" : partner.referral_code}, status=status.HTTP_200_OK)
		return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateDestroyReferral(APIView):
	def post(self, request):
		referred_email = self.request.query_params.get('referred_email', None)
		referral_code = self.request.query_params.get('referral_code', None)

		if referred_email is not None and referred_email != "" and referral_code is not None and referral_code != "":
			referred_user = Partner.objects.filter(email=referred_email)
			if referred_user:
				return Response(status=status.HTTP_400_BAD_REQUEST)

			try:
				referrer = Partner.objects.get(referral_code=referral_code)
			except Partner.DoesNotExist:	
				return Response(status=status.HTTP_400_BAD_REQUEST)
			
			if referrer.referral_credits == 0:
				return Response(status=status.HTTP_400_BAD_REQUEST)	 		

			serializer = ReferralSerializer(data={"referred_email": referred_email, "referrer": referral_code})
			if serializer.is_valid():
				serializer.save()
				referrer.referral_credits -= 1
				referrer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
		
		return Response(status=status.HTTP_400_BAD_REQUEST)	

	def delete(self, request):
		referred_email = self.request.query_params.get('referred_email', None)
		referral_code = self.request.query_params.get('referral_code', None)
		
		if referred_email is not None and referred_email != "" and referral_code is not None and referral_code != "":
			try:
				referrer = Partner.objects.get(referral_code=referral_code)
			except Partner.DoesNotExist:	
				return Response(status=status.HTTP_400_BAD_REQUEST)
			
			referral = Referral.objects.filter(referred_email=referred_email, referrer=referrer)
			if not referral:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			
			referred_user = Partner.objects.filter(email=referred_email)
			if referred_user:
				return Response(status=status.HTTP_400_BAD_REQUEST)	
			
			referral.delete()
			referrer.referral_credits +=1
			referrer.save()
			
			return Response(status=status.HTTP_204_NO_CONTENT)

		return Response(status=status.HTTP_400_BAD_REQUEST)				

class ConvertReferral(APIView):
	def post(self, request):
		email = self.request.query_params.get('email', None)
		referral_code = self.request.query_params.get('referral_code', None)

		if email is not None and email != "" and referral_code is not None and referral_code != "":
			try:
				referrer = Partner.objects.get(referral_code=referral_code)
			except Partner.DoesNotExist:	
				return Response(status=status.HTTP_400_BAD_REQUEST)

			referral = Referral.objects.filter(referred_email=email, referrer=referrer)
			if referral:
				referred_user = Partner.objects.filter(email=email)
				if referred_user:
					return Response(status=status.HTTP_400_BAD_REQUEST)

				serializer = PartnerSerializer(data=request.data)
				if serializer.is_valid():
					username = serializer.data.get('username')
					partner = Partner(email=email, course_credits=1, username=username)
					partner.save()
					referrer.course_credits += 1
					referrer.save()
					referral.delete()
					return Response(status=status.HTTP_201_CREATED)

				return Response(status=status.HTTP_400_BAD_REQUEST)	

			return Response(status=status.HTTP_400_BAD_REQUEST)

		return Response(status=status.HTTP_400_BAD_REQUEST)	