# Sample JSON data:
# "metadata": {
#     "category": null,
#     "title": "make Confit Byaldi",
#     "admin_topics": [],
#     "topics": [
#         "food"
#     ],
#     "primary_topic": null,
#     "is_request_attached": null,
#     "summary": "A variation on the traditional French dish ratatouille.",
#     "main_image_uuid": "ef3a128c94144176b57876a5a1576d78",
#     "original_request_uuid": null
# }

from redisco import models

class Metadata(models.Model):

	category 				= models.Attribute(indexed=True)
	title 					= models.Attribute(indexed=True)
	primary_topic 			= models.Attribute(indexed=True)
	is_request_attached 	= models.Attribute(indexed=True)
	summary 				= models.Attribute(indexed=True)
	main_image_uuid 		= models.Attribute(indexed=True)
	original_request_uuid	= models.Attribute(indexed=True)
	admin_topics 			= models.ListField(unicode, indexed=True)
	topics 					= models.ListField(unicode, indexed=True)