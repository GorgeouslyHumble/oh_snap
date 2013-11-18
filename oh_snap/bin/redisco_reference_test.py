#Note to self... contact the owner of Redisco and ask if he can update his damn documenation to include how to do references. >:C

from redisco import models

class Doghouse(models.Model):

	location = models.Attribute(indexed=True)

class Dog(models.Model):

	name = models.Attribute(indexed=True, required=True)
	breed = models.Attribute(indexed=True)
	description = models.Attribute(indexed=True)

	current_doghouse = models.ReferenceField(Doghouse, indexed=True)
	previous_doghouses = models.ListField(Doghouse, indexed=True)

couch = Doghouse(location='living room')
couch.is_valid()
couch.save()

silent_treatment = Doghouse(location='the cold side of the bed')
silent_treatment.is_valid()
silent_treatment.save()

snide_comments = Doghouse(location='kitchen table')
snide_comments.is_valid()
snide_comments.save()

cold_shoulder = Doghouse(location='everywhere')
cold_shoulder.is_valid()
cold_shoulder.save()

dog = Dog(name="Daryl", 
		  breed="Construction worker", 
		  description="He told his wife that he liked her sister's cooking better.",
		  current_doghouse=(couch),
		  previous_doghouses=[silent_treatment])

dog.is_valid()
dog.save()

daryl = Dog.objects.filter(name="Daryl")[0]
print daryl.previous_doghouses

daryl.previous_doghouses.append([snide_comments, cold_shoulder])
print daryl.previous_doghouses

