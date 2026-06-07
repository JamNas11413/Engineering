from django.db import models

# Create your models here.

# Constants defined at module level so all classes can access them
MEMBERSHIP_BRONZ = 'B'
MEMBERSHIP_SILVER = 'S'
MEMBERSHIP_GOLD = 'G'
PENDING = 'P'
COMPLETE = 'C'
FAILED = 'F'

# choice field 


MEMBERSHIP = [
    (MEMBERSHIP_BRONZ, 'bronz'),  # on erepresentation in db and the other is human readable name {we need them too see in ADMIN INTERFACE } 
    (MEMBERSHIP_SILVER, 'silver'),
    (MEMBERSHIP_GOLD, 'gold')
] # caps because i am showing that it should not be changed




ORDER = [
    (PENDING, 'PENDING'),
    (COMPLETE, 'COMPLETED'),
    (FAILED, 'FAILED')
]

# just know from the DB design what you need in the table and then search for it-> to do in the best way

class Products(models.Model):
    slug = models.SlugField(default='_')  # unique slug field for product url
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)    # 1st time
    updated_at = models.DateTimeField(auto_now=True)    # at every update
    order_status = models.CharField(max_length=1, choices=ORDER, default=PENDING)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
    
    
    
class Customers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField( unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP, default=MEMBERSHIP_BRONZ)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name']

# one to one reationship between customer and address
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    customer = models.OneToOneField(Customers, on_delete=models.CASCADE, primary_key=True) # one to one relationship with customer model
    zip = models.CharField(max_length=10, default='00000') # default value for zip code

# on eto many relationship between customer and order
class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.PROTECT) # one to many relationship with customer model
    product = models.ForeignKey(Products, on_delete=models.PROTECT)  # not to delete the asspciated ordere item via protect # one to many relationship with product model
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    unit_order = models.DecimalField(max_digits=10, decimal_places=2)  # price an be changed, every time on ordering we will set the price

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name}'
    
    class Meta:    # for setting the default order
            ordering = ['order_date']
            
# many to many relationship between order and product
class OrderItem(models.Model):
    new_order = models.ForeignKey(Orders, on_delete=models.CASCADE) # one to many relationship with order model
    product = models.ForeignKey(Products, on_delete=models.CASCADE) # one to many relationship with product model
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2) 


# resolving circular relationships/dependancy
    # when two classes are dependant on eachother at same time we can use string reference to resolve the circular relationship
    # for example in the above code we have circular relationship between order and product models because order model has foreign key to product model and product model has foreign key to order model, to resolve this we can use string reference in the foreign key field like this:
    # order = models.ForeignKey ('Orders', on_delete=models.CASCADE) # using string reference to resolve circular relationship 'oders' is the name of the model class as a string set related name to + so it will tells django not make that reverse relationship


# Generic relationships
    # when we want to create a relationship between two models but we don't want to create a foreign key field in one of the models we can use generic relationships
    # for example we have a model called review and we want to create a relationship between review and product models but we don't want to create a foreign key field in review model because we want to use the same review model for other models like customer model we can use generic relationships like this:
    # from django.contrib.contenttypes.fields import GenericForeignKey
    # from django.contrib.contenttypes.models import ContentType
    # class Review(models.Model):
    #     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #     object_id = models.PositiveIntegerField()
    #     content_object = GenericForeignKey('content_type', 'object_id')
    # in the above code we have created a generic relationship between review model and product model and we can use the same review model for other models like customer model by setting the content_type and object
    

