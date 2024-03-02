from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

#@api_view(["GET"])
#def api_home(request, *args, **kwargs):
#    instance = Product.objects.all().order_by("?").first()
#    #data = {}
#    """
#    DRF API VIEW
#    """

#    if instance:
       # data = model_to_dict(instance, fields=['id', 'content', 'price', 'sale_price'])
#        data = ProductSerializer(instance).data

#    return Response(data) 

@api_view(["POST"])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save(commit=False)
        #print(instance)
        print(serializer.data)
        return Response(serializer.data) 
    return Response({"invalid": "invalid data"}, status = 400)
#Difference between JsonResponse and HttpResponse is that JsonResponse takes python dict as an argument whereas
# HttpResponse takes text.
  #if model_data: 
    #    data["id"] = model_data.id
    #    data["title"] = model_data.title
    #    data["content"] = model_data.content
    #    data["price"] = model_data.price
        #SERIALIZATION - WE TAKE REPREZENTATION OF AN INSTANCE (MODEL_DATA) WE TURN IT INTO PYTHON DICTIONARY AND RETURN JSON TO MY CLIENT.
        #in ther words: We take model representation of an database instance, turn it into python dict and then convert it to json using JsonResponse()
    #BETTER APPROACH USING MODEL_TO_DICT