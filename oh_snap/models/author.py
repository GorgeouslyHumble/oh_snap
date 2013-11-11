# Example JSON data:
#
# "author": {
#     "first_name": "Chez",
#     "last_name": "Fred",
#     "name": "Chez Fred",
#     "image": "f1cbde84ab024618afe1b91e84e2810f",
#     "is_following_author": false,
#     "profile_path": "chez-fred",
#     "external_id": "Z0LTA0gmTYGRYA2dsU-6ag"
# }

from redisco import models

class Author:

	name 				= models.Attribute(indexed=True)
	first_name			= models.Attribute(indexed=True)
	last_name			= models.Attribute(indexed=True)
	profile_path		= models.Attribute(indexed=True)
	external_id			= models.Attribute(indexed=True)
	image				= models.Attribute(indexed=True)
	is_following_author	= models.BooleanField(indexed=True)