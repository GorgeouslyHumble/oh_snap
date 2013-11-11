# Example JSON data:
#
# {
#     "content": {
#         "caption": "You can get the recipe from the nytimes website.",
#         "media_item_uuid": "2a934132ea194f71b7ad67e82eeab4a6"
#     },
#     "comment_count": 0,
#     "type": "image",
#     "uuid": "aa1fe443b1cd43d4acba65b3b4ab6750"
# }

from redisco import models

class Item(models.Model):

	uuid 			= models.Attribute(indexed=True, required=True, unique=True)
	item_type 		= models.Attribute(indexed=True)
	content 		= models.ReferenceField(Content, indexed=True)
	comment_count	= models.IntegerField(indexed=True)
