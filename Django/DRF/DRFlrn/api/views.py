import django
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin # ctr + click to view implementattion of them 
from rest_framework.parsers import JSONParser    # here is a warning it will because of our selected pyhton interpreter
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .models import Person
from .serializers import PersonSerializer, PersonModelSerializer
import io

# # Create your views here.
# @csrf_exempt
# def single_object_view(request, id):
#     # this view will return a single object
#    #  data = Person.objects.get(id=id)  # this will get the object with id 1 from the database   # IF THE ID DOES NOT EXIST IT WILL RAISE IN ERROR DUE TO THE GET() METHOD
#     # TO AVOID WE CAN:  
#    #    handle the xception manually 
#    #  or
#       # use get obj or 404
#     data = get_object_or_404(Person, id=id)  # also give the model form which the model data belongs to and the id of the object we want to get  # if the object with the given id does not exist it will return a 404 error response
#     if request.method == "PUT":  # CLIENT WANT TO UPDATE ALL THE FIELDS OF THE OBJECT
#         json = request.body
#         stream = io.BytesIO(json)
#         parsed_data = JSONParser().parse(stream)

#       #   serializer = PersonSerializer(data, data=parsed_data) # as we do update niot create so we will also pass the mmodel obj

#         serializer = PersonModelSerializer(data, data=parsed_data) 

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({"updated": "succesfully"}, status=status.HTTP_200_OK)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == "PATCH":  # CLIENT WANT TO UPDATE SOME THE FIELDS OF THE OBJECT
#          json = request.body
#          stream = io.BytesIO(json)
#          parsed_data = JSONParser().parse(stream)

#          # serializer = PersonSerializer(data, data=parsed_data, partial=True) #partial true is used to allow partial updates  # IF IT IS FALSE IT WILL RAISE AN ERROR THAT THE FIEL DIS MISSING 

#          serializer = PersonModelSerializer(data, data=parsed_data, partial=True)

#          if serializer.is_valid():
#                serializer.save()
#                return JsonResponse({"updated": "succesfully"}, status=status.HTTP_200_OK)
#          return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     serializer = PersonModelSerializer(data)  # this will serialize the data
#     # print(serializer.data) 
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, 
#                         content_type='application/json')

# @csrf_exempt   # needed for post requets to avoid csrf token error
# def list_object_view(request):
#     if request.method == "POST":
#        json = request.body
#        # we needa cponvert the above data into a stream
#        stream = io.BytesIO(json)
#        parsed_data = JSONParser().parse(stream) # parsed_data contains the json data coonverted into python datatypes
#     #    print(parsed_data) # we are gettng an error syays csrf token required, so we needa import it and apply the deccorater on this func
#     #    print(type(parsed_data)) # dictionary

#       # AFTER THE PARSING PROCESS WE WILL IMPPLEMENT DESERIALIZATION PROCESS
#        serializer = PersonModelSerializer(data=parsed_data)
   #     if serializer.is_valid():
   #      #    pass
   #       serializer.save()
   #       return JsonResponse({"created": "succesfully"}, status=status.HTTP_201_CREATED)
   #  #    errors = JSONRenderer().render(serializer.errors)
   #  # or
   #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     data = Person.objects.all() 
#     serializer = PersonModelSerializer(data, many=True)  # this will serialize the data and many=True is used to serialize multiple objects
#     # each dictionary will represent an object
#     # print(serializer.data) 
#    #  json_data = JSONRenderer().render(serializer.data)
#    #  return HttpResponse(json_data, 
#    #                      content_type='application/json')
#    #  or
#     return JsonResponse(serializer.data, safe=False)  # this will return the json data and safe=False is used to allow non-dictionary objects to be serialized


# # WE ARE USING CORE DJANGO VIEWS  NOT WHICH OROVIDED BY THE DRF SO WE NEED TO MANUALLY IMPLEMENT THE SERIALIZATION AND DESERIALIZATION PROCESS IN THE VIEWS AND ALSO WE NEED TO MANUALLY HANDLE THE HTTP METHODS IN THE VIEWS


# # i changes all the PersonSErioaliser by PersonModelSerializer because the model serializer is more efficient and easier to use than the regular serializer as it automatically generates the create and update methods based on the model fields and also it automatically generates the fields based on the model fields so we don't need to manually define the fields in the serializer class.






# DRF VIEWS
# FUNCTION BASED API VIEWS(DRF):
# @api_view(["PUT", "PATCH", "GET"])  # this will allow only the specified HTTP methods to access this view
# def single_object_view(request, id):
#     # this view will return a single object
#    #  data = Person.objects.get(id=id)  # this will get the object with id 1 from the database   # IF THE ID DOES NOT EXIST IT WILL RAISE IN ERROR DUE TO THE GET() METHOD
#     # TO AVOID WE CAN:  
#    #    handle the xception manually 
#    #  or
#       # use get obj or 404
#     data = get_object_or_404(Person, id=id)  # also give the model form which the model data belongs to and the id of the object we want to get  # if the object with the given id does not exist it will return a 404 error response
#     if request.method == "PUT":  # CLIENT WANT TO UPDATE ALL THE FIELDS OF THE OBJECT
#         parsed_data = request.data  # this will automatically parse the json data from the request body and convert it into python datatypes so we don't need to manually parse the json data using JSONParser and also we don't need to manually convert the json data into a stream using io.BytesIO as the DRF request object will automatically handle that for us.
#       #   serializer = PersonSerializer(data, data=parsed_data) # as we do update niot create so we will also pass the mmodel obj
#
#         serializer = PersonModelSerializer(data, data=parsed_data) 
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"updated": "succesfully"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "PATCH":  # CLIENT WANT TO UPDATE SOME THE FIELDS OF THE OBJECT
#          parsed_data = request.data 
#
#          # serializer = PersonSerializer(data, data=parsed_data, partial=True) #partial true is used to allow partial updates  # IF IT IS FALSE IT WILL RAISE AN ERROR THAT THE FIEL DIS MISSING 
#
#          serializer = PersonModelSerializer(data, data=parsed_data, partial=True)
#
#          if serializer.is_valid(raise_exception=True):
#                serializer.save()
#                return Response({"updated": "succesfully"}, status=status.HTTP_200_OK)
#          
#     if request.method == "GET":
#       serializer = PersonModelSerializer(data)  # this will serialize the data
#       # print(serializer.data) 
#       return Response(serializer.data)
#
#
# @api_view(["POST", "GET"])  # this will allow only the specified HTTP methods to access this view
# def list_object_view(request):
#    if request.method == "POST":
#        parsed_data = request.data 
#     #    print(parsed_data) # we are gettng an error syays csrf token required, so we needa import it and apply the deccorater on this func
#     #    print(type(parsed_data)) # dictionary
#
#       # AFTER THE PARSING PROCESS WE WILL IMPPLEMENT DESERIALIZATION PROCESS
#        serializer = PersonModelSerializer(data=parsed_data)
#
#       #  if serializer.is_valid():
#       #   #    pass
#       #    serializer.save()
#       #    return JsonResponse({"created": "succesfully"}, status=status.HTTP_201_CREATED)
#       #  return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#       # or
#        if serializer.is_valid(raise_exception=True):
#            serializer.save()  # this will automatically raise a validation error if the data is not valid against the serializer fields so we don't need to manually check if the serializer is valid or not and also we don't need to manually return the errors in case of invalid data as the DRF will automatically handle that for us and return a proper error response with the appropriate status code and also it will automatically include the error details in the response body so we don't need to manually include the error details in the response body as well.
#            return Response({"created": "succesfully"}, status=status.HTTP_201_CREATED)
#     
#    if request.method == "GET":
#       # print(request.accepted_renderer)  #  <rest_framework.renderers.JSONRenderer object at 0x7f68b05417b0># this will print the accepted renderer for the request which is the renderer that will be used to render the response data and it is determined by the content negotiation process of DRF based on the Accept header of the request and also based on the available renderers in the settings.py file of the project
#       data = Person.objects.all() 
#       serializer = PersonModelSerializer(data, many=True)  # this will serialize the data and many=True is used to serialize multiple objects
#       # each dictionary will represent an object
#       # print(serializer.data) 
#       #  json_data = JSONRenderer().render(serializer.data)
#       #  return HttpResponse(json_data, 
#       #                      content_type='application/json')
#       #  or
#       return Response(serializer.data)  # we don't need the safe = false while using responce instead of JsonResponce
# we also get the error in json 

# OKAY SO, the request in django core views is an is instance of httprequest class but in DRF views the request is an instance of rest_framework.request.Request class 
#    which is a wrapper around the django httprequest class 
#    and it provides some additional functionality like:
#    parsing the request data 
#    and also it provides some additional attributes like .data which contains the parsed data from the request body 
#    and also it provides some additional methods like .is_valid() which is used to validate the data against the serializer fields 
#    and also it provides some additional attributes like .errors which contains the errors if the data is not valid against the serializer fields.

# i also remove the parsing logic as the DRF request object will automatically parse the request body and provide the parsed data in the .data attribute of the request object 
# so we don't need to manually parse the request body using JSONParser and also we don't need to manually convert the json data into a stream using io.BytesIO as the DRF request object will automatically handle that for us. 




# CLASS BASED API VIEWS(DRF):
# class SingleObjectView(APIView):
    
#     def get(self, request, id):
#         data = get_object_or_404(Person, id=id)
#         serializer = PersonModelSerializer(data)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         data = get_object_or_404(Person, id=id)
#         serializer = PersonModelSerializer(data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"updated": "succesfully"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, id):
#         data = get_object_or_404(Person, id=id)
#         serializer = PersonModelSerializer(data, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({"updated": "succesfully"}, status=status.HTTP_200_OK)


# class ListObjectView(APIView):
    
#     def get(self, request):
#         data = Person.objects.all()
#         serializer = PersonModelSerializer(data, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         parsed_data = request.data
#         serializer = PersonModelSerializer(data=parsed_data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({"created": "succesfully"}, status=status.HTTP_201_CREATED)




# GENERIC API 
# and mixins
# class ListObjectView(GenericAPIView, CreateModelMixin, ListModelMixin): # they incapsulate the implementattion ofthe methods
#     queryset = Person.objects.all()  # this will tell the generic view which queryset to use for the view and it is used to get the data from the database and also it is used to perform the CRUD operations on the data in the database
#     serializer_class = PersonModelSerializer  # this will tell the generic view which serializer to use for the view and it is used to serialize the data and also it is used to perform the validation on the data before saving it to the database and also it is used to perform the validation on the data before updating it in the database and also it is used to perform the validation on the data before deleting it from the database

#     # methods like list only requires the request but other like update and retrive() requires id as well which is an additional url peram so for consistancy we always use the *args, **kwargs
#     def get(self, request, *args, **kwargs): # *args - contains the unnamed url perameters as a tuple AND **kwargs - contains the named url prmeter as a idctionary 
#         return self.list(request, *args, **kwargs)  # this will call the list method of the ListModelMixin which will return the list of all the objects in the database in a serialized format and also it will automatically handle the pagination and also it will automatically handle the filtering and also it will automatically handle the ordering of the data based on the query parameters in the request URL and also it will automatically handle the content negotiation process to determine the appropriate renderer to use for rendering the response data based on the Accept header of the request and also based on the available renderers in the settings.py file of the project
    
#     def post(self, request):
#         return self.create(request)  # this will call the create method of the CreateModelMixin which will create a new object in the database based on the data in the request body and also it will automatically handle the validation of the data against the serializer fields and also it will automatically handle the content negotiation process to determine the appropriate renderer to use for rendering the response data based on the Accept header ofthe request and also based onthe available renderers inthe settings.py file ofthe project
    

class SingleObjectView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    
    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  # this will call the retrieve method of the RetrieveModelMixin which will return a single object from the database based on the pk in the URL and also it will automatically handle the content negotiation process to determine the appropriate renderer to use for rendering the response data based on the Accept header ofthe request and also based onthe available renderers inthe settings.py file ofthe project
    
    def put(self, request, pk, *args, **kwargs):
        return self.update(request, *args, **kwargs)  # this will call the update method of the UpdateModelMixin which will update a single object in the database based on the pk in the URL and also it will automatically handle the validation of the data against the serializer fields and also it will automatically handle the content negotiation process to determine the appropriate renderer to use for rendering the response data based on the Accept header ofthe request and also based onthe available renderers inthe settings.py file ofthe project
            
    
    def patch(self, request, pk, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)  # this will call the partial_update method of the UpdateModelMixin which will update a single object in the database based on the pk in the URL and also it will automatically handle the validation of the data against the serializer fields and also it will automatically handle the content negotiation process to determine the appropriate renderer to use for rendering the response data based on the Accept header ofthe request and also based onthe available renderers inthe settings.py file ofthe project
    
    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  # this will call the destroy method of the DestroyModelMixin which will delete a single object from the database based on the pk in the URL and also it will automatically handle the content negotiation process to determine the appropriate renderer to use for rendering the response data based on the Accept header ofthe request and also based onthe available renderers inthe settings.py file ofthe project
    
    def delete(self, request, id, *args, **kwargs):
        return self.destroy(request, id=id, *args, **kwargs)  # this will call the destroy method of the DestroyModelMixin which will delete a single object from the database based on the id in the URL and also it will automatically handle the content negotiation process to determine the appropriate renderer to use for rendering the response data based on the Accept header ofthe request and also based onthe available renderers inthe settings.py file ofthe project

    # we can also customize the generic voew lets say we have something extra than the default in our delete method so we ca juse what we defined instead of what is the default:
        # how:
            # just define your method and it will use 
            # or docs



# with
# concreate classes

class SingleObjectView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer


class ListObjectView(ListCreateAPIView):
    queryset = Person.objects.all()  
    serializer_class = PersonModelSerializer 

    # if we have some complex logic thaty hasn't defied in the concreate classes i. we wanna do something else for that we can also define methods here 
    def get_queryset(self):
        return Person.object.all()

