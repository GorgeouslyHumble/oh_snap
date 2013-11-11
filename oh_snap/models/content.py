# Example JSON data:
#
#     "content": {
#         "caption": "You can get the recipe from the nytimes website.",
#         "media_item_uuid": "2a934132ea194f71b7ad67e82eeab4a6"
#     }
#
# As a note, content is applicable to multiple API resources, unfortunately.
from redisco import models

class Content(models.Model):

	media_item_uuid	= models.Attribute(indexed=True, required=True, unique=True)
	caption			= models.Attribute(indexed=True)
	text 			= models.Attribute(indexed=True)