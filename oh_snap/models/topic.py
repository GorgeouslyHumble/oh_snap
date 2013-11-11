# Example JSON data:
#
# "topics": [
#     {
#         "thumb_image_uuid": "687d90acc1b94e6ebc31161e576a5d94",
#         "description": "Inspiration and information from passionate chefs and everyday cooks. Swipe to discover go-to meals, secret family recipes, and special occasion show-stoppers. ",
#         "is_editorial": false,
#         "skip_featured_view": false,
#         "has_subtopics": false,
#         "cover_image_uuid": "687d90acc1b94e6ebc31161e576a5d94",
#         "thumb_image_type": "guide",
#         "short_description": "",
#         "display_name": "Food",
#         "slug": "food",
#         "cover_image_type": "guide",
#         "uuid": "f8ee3611dacf4e1ba822c5f9b1c017a5"
#     }
# ]

from redisco import models

class Topic(models.Model):

    uuid                    = models.Attribute(indexed=True, required=True, unique=True)
    thumb_image_uuid        = models.Attribute(indexed=True)
    cover_image_uuid        = models.Attribute(indexed=True)
    cover_image_type        = models.Attribute(indexed=True)
    description             = models.Attribute(indexed=True)
    short_description       = models.Attribute(indexed=True)
    display_name            = models.Attribute(indexed=True)
    slug                    = models.Attribute(indexed=True)
    is_editorial            = models.Attribute(indexed=True)
    skip_featured_view      = models.BooleanField(indexed=True)
    has_subtopics           = models.BooleanField(indexed=True)
