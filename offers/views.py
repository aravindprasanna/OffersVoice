from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from offers.models import OffersMapping
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from offers.models import OffersMapping,Offers
from offers.serializers import OffersMappingSerializer,OffersSerializer

# Create your views here.

@csrf_exempt
def offer_list(request,type,card,activity):

    if request.method == 'GET':
        relevant_offers = OffersMapping.objects.get(offer_type=type.lower(),offer_card=card.lower(),offer_activity=activity.upper())
        serializer = OffersMappingSerializer(relevant_offers)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def offer(request,offer_id):

    if request.method == 'GET':
        selected_offer = Offers.objects.get(offer_id=offer_id)
        serializer = OffersSerializer(selected_offer)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def offer_by_type(request,type):

    if request.method == 'GET':
        relevant_offers = OffersMapping.objects.get(offer_type=type.lower(),offer_card="all",offer_activity="all")
        serializer = OffersMappingSerializer(relevant_offers)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def offer_search(request,search_parm):

    if request.method == 'GET':
        relevant_offers = Offers.objects.all().filter(offer_details__icontains=search_parm)
        serializer = OffersSerializer(relevant_offers,many=True)
        return JsonResponse(serializer.data, safe=False)


