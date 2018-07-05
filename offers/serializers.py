from rest_framework import serializers
from offers.models import OffersMapping,Offers

class OffersMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffersMapping
        fields = ('offer_list',)

class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = ('offer_id','offer_url','offer_brief','offer_description','offer_details','offer_period','offer_channel')
