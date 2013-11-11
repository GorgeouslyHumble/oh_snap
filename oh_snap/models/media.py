# Example JSON data:
#
# "media": {
#     "ef0a59935f214b35a103ef255d9a810b": {
#         "url": "http://images.snapguide.com/images/guide/ef0a59935f214b35a103ef255d9a810b/original.jpg",
#         "width": 960,
#         "type": "guide_image",
#         "content_type": "image/jpeg",
#         "height": 640
#     }
# },
#
# As a note, the media entry for the Snapguide API *seems* to be breaking styling conventions. Most groups tend to be an object that contains an array of objects... however, media, as a group, is an array of objects which, in turn, contain more objects. Veird. 

from redisco import models

class Media(models.Model):

	uuid 			= models.Attribute(indexed=True, required=True, unique=True)
	url 			= models.Attribute(indexed=True)
	width 			= models.Attribute(indexed=True)
	media_type 		= models.Attribute(indexed=True)
	content_type 	= models.Attribute(indexed=True)