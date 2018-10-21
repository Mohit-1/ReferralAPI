from rest_framework import serializers
from .models import Partner, Referral

class PartnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Partner
		fields = ('username',)

class ReferralSerializer(serializers.ModelSerializer):
	class Meta:
		model = Referral
		fields = '__all__'