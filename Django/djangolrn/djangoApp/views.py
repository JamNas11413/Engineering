from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
# from django.db import Q, F # short for querry and sing it we can genrate a query expression(a piece of code that produces a value)
from djangoApp.models import Products
# Create your views here.


def post_lists(request):
    # queryset = Products.objects.all()
    # Products.objects.get()
    # Products.objects.filter()
    # querset[2,3]hre it will evaluated
    # try:
    #     profuct = Products.objects.get(pk=0)  # id 0 does ot exist
    # except: ObjectDoesNotExist:
    #     pass # in  real scenario we show an error to the user

        # OR
    profuct = Products.objects.filter(pk=0).first()   # as the filter returns a queryset we can make a complex query of it 
        # the first() return none if the ojb not found, so we don't get an error
    # TO CHECK EXISTANCE 
    profuct = Products.objects.filter(pk=0).exist() # exist return a boolean value

    # FILTERING DATA

    queryset = Products.objects.filter(price = 20)  # all the product heaving price of 20

    # but what if we wanna find out all the product expensive than 20 we can't use logical ops here

    # so we do with look uptypes 
    # gt-> greater than
    # gte-> greater than or equal to
    # lt / lte  _> as above 
    queryset = Products.objects.filter(price__lte= 20)

    #  WE CAN SEARCH FOR QUERY SET API DJANGO
    # ALSO FOR LOOK UP TYPES LIKE range, 



    # COMPLEX LOOK UPS USING Q OBJ:
    # applying multiple filters 
    # to apply: products: inventory < 10 AND price <20
    queryset = Products.objects.filter(inventory__lt = 10, unit_price__lt = 20)   # look up for the sql statement that the orm generated on Ddjango debug toolbar
    # or
    queryset = Products.objects.filter(inventory__lt = 10).filter(unit_price__lt = 20)
    # they both are same 

    # but what about or
    # to do so we have to use Q objects 
    # to apply: products: inventory < 10 OR price <20
    queryset = Products.objects.filter(Q(inventory__lt=10) | Q(price__lt=20))  # instead of passing a keyword argument we are going to pass a Q obj
        # so each quiery obj encapsulates a keyword argument or a query expression 
        # then combine it with another Q obj using betwise OR operater (|) -> it will translate to logical or in sql query

    # can also
    queryset = Products.objects.filter(Q(inventory__lt=10) | ~Q(price__lt=20))  # negate the q with ~ -> not
    queryset = Products.objects.filter(Q(inventory__lt=10) & Q(price__lt=20))




    # REFRENCOING FIELD USING F OBJ:
    # some times when filterign data we nedda refrence  aprticular field 
    # i.e products: price = inventory   => so we are combining differnt fields
    # like:
    queryset = queryset = Products.objects.filter(inventory=price) # we get an error 
    # but
    queryset = queryset = Products.objects.filter(inventory=F('price'))  #so we refrence field like this using F obj




    # SORTING:
    queryset = Products.objects.order_by('title') # all the producsts are niw sorted in alphabetical order
    queryset = Products.objects.order_by('-title') # descending oredr
    queryset = Products.objects.order_by('price','-title') # ascending + descending
    # the order_by return a queryset obj and one of the methods of queryset is reverse
    queryset = Products.objects.order_by('title').reverse() # descending 

    # object instead of queryset
    product = Products.objects.order_by('title')[0] # 1st item in the sorted items  # return object and not queryset because it returns only one obj and with one we can't perform ther ops like order_by or filtering etc

    # other methods etc like earliest or latest etc



    # LIMITING RESULTS:
        # often we dont wanna show all product to the user in one disk
        # we wanna show pages of products

    product = Products.objects.all()[:5]  # 1st 5 (0 to 4)

    




    # SELECTING FIELDS/column TO QUERY:
    product = Products.objects.values('id', 'title')  # with this implementtation we are only rreadu gid and titile of each product
    # we can also read related fields i.e
    product = Products.objects.values('id', 'title', 'collection__title')   # with this we will have an inner join b\w the product ansd collection tables because we are reading related filed 

    # the values methods returns a bunch of dictionary objects not products instancese


    return render(request, 'post/post_list.html',) #{'products:' list(queryset)})



