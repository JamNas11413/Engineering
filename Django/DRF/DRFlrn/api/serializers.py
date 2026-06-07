# this file will contain all the serializers for this app

from rest_framework import serializers  # the warning ia because the current python interpreter in the venv is not the one global ...

from .models import Person    # serializers contains all the serializers

class PersonSerializer(serializers.Serializer):
    # fields that we wanna send to / recieve form / the user
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()  # the integer field for age is used for positive negstive and all integer field in DRF
    city = serializers.CharField(max_length=100)
    # we can also include field tghat don't exists in our model class i.e
    price_with_tax = serializers.SerializerMethodField(method_name='calc_tax')

    def calc_tax(self, person: Person): # we can inotate it 
        return person.age / 2

    def create(self, validated_data):  # WILL CALLED BY save()
        # this method will create a new object in the database
        return Person.objects.create(**validated_data)  # this will create a new object in the database using the validated data

    def update(self, instance, validated_data):  # will be called by save() when we are updating an object  # THE INSTANCE IS THE DATA (MODEL DATA THAT WE HAVE PASSED TO THE SERIALIZER) THAT WE WANT TO UPDATE AND THE VALIDATED_DATA IS THE NEW DATA THAT WE WANT TO UPDATE THE INSTANCE WITH
        # this method will update an existing object in the database
        instance.name = validated_data.get('name', instance.name)  # this will update the name field of the instance with the new value if it is provided in the validated data otherwise it will keep the old value
        instance.age = validated_data.get('age', instance.age)  # this will update the age field of the instance with the new value if it is provided in the validated data otherwise it will keep the old value
        instance.city = validated_data.get('city', instance.city)  # this will update the city field of the instance with the new value if it is provided in the validated data otherwise it will keep the old value
        instance.save()  # this will save the updated instance to the database
        return instance  # this will return the updated instance
    
class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person  # this will tell the serializer which model to use for serialization and deserialization
        fields = '__all__'  # this is a bad practice we should always use the name of the field in a list as we can change ur model later in time but we may not want to show it to user # this will tell the serializer to include all the fields of the model in the serialization and deserialization process
        # or we can also specify the fields that we want to include in the serialization and deserialization process
        # fields = ['name', 'age','price_with_tax']  # this will tell the serializer to include only the name and age fields of the model in the serialization and deserialization process
        # we can also include field tghat don't exists in our model class i.e
        # price_with_tax = serializers.SerializerMethodField(method_name='calc_tax')

        # def calc_tax(self, person: Person): # we can inotate it 
        #     return person.age / 2

                                                                                                                        


# serializing relationships:
    # 4 ways
        # PRIMARY KEY
        # STRING 
        # nested objects
        # hyper links





