# Sample JSON data:
#
# {
#   "guide": {
#     "uuid": "0bed6fee853b4f4e966cec0f1210079d",
#     "last_edited": 1343395079,
#     "master_uuid": "afd67cf1fa3d4d07a06b5d948daa4c77",
#     "seq": 9,
#     "branch_uuid": "afd67cf1fa3d4d07a06b5d948daa4c77",
#     "branch_point_master_seq": null,
#     "branch_point_seq": null,
#     "branch_point_txn_id": null
#     "publish_date": 1343395079,
#     "publish_title": "Make Sous Vide Chicken at Home",
#     "publish_url": "/guides/make-sous-vide-chicken-at-home/",
#     "publish_main_image_uuid": "77907e4f073b43c9971d12d6141332a8",
#     "short": "vcyq",
#     "like_count": 1492,
#     "is_liked": true,
#     "view_count": 21172,
#     "guide_comment_count": 89,
#     "supplies_comment_count": 1,
#     "total_comment_count": 131,
#     "supplies_uuid": "30e7aa4efe664f52bbf23c0cea430720",
#     "metadata":  { ... },
#     "author":  { ... },
#     "media":  { ... },
#     "items": [ ... ],
#     "supplies": { ... },
#     "topics": [ ... ],
#   },
#   "success":true
# }
#
# Description: 
#
# This model is for storing a guide
#
# Rules:
#
# 1. The image attribute is a string used for constructing a link to the guide's image - which exists in a Snapguide owned S3 bucket.
#
# Example: http://images.snapguide.com/images/<type>/<unique_identifier>/<size>.jpg
# 
# The <type> can be a guide, a profile, or a topic. <unique_identifier> is that image attribute string. The <size> is the size PLUS the cropping strategy.
#
# 2. The UUID is guaranteed to be unique. This is to be expected from the API and from the model logic.
#
# 3. Time is counted from UNIX epoch.
#
# 4. The default index value is always true (according to the documenation) but I found out that I couldn't actually search for that value so I set it manually.
#
# 5. NoSQL is ALWAYS the right choice because it is WEBSCALE!!!!oneone!!11
#
# 6. I may move to a more document oriented NoSQL store like Couchbase (they have a well documented SDK) if I have the science to back up some reasons for transitioning. Or if I just feel like it. Even though Redis and Redisco work well... Redisco doesn't have a lot of support and deeply nested JSON is somewhat hard to code around.


from redisco import models
from oh_snap.models.author import Author
from oh_snap.models.content import Content
from oh_snap.models.item import Item
from oh_snap.models.media import Media
from oh_snap.models.metadata import Metadata
from oh_snap.models.supply import Supply
from oh_snap.models.topic import Topic

class Guide(models.Model):

	# Union
	uuid 					= models.Attribute(indexed=True)
	# seq 					= models.IntegerField(indexed=True)
	# short 					= models.Attribute(indexed=True)
	# like_count 				= models.IntegerField(indexed=True)
	# is_liked 				= models.BooleanField(indexed=True)
	# view_count 				= models.IntegerField(indexed=True)
	# guide_comment_count 	= models.IntegerField(indexed=True)
	# supplies_comment_count 	= models.IntegerField(indexed=True)
	# total_comment_count 	= models.IntegerField(indexed=True)
	# topics 					= models.ListField(unicode, indexed=True)

	# # Intersect for UUID fetch result
	# last_edited 			= models.IntegerField(indexed=True)
	# master_uuid 			= models.Attribute(indexed=True)
	# branch_uuid 			= models.Attribute(indexed=True)
	# branch_poind_master_seq = models.Attribute(indexed=True)
	# branch_point_seq 		= models.Attribute(indexed=True)
	# branch_point_txn_id 	= models.Attribute(indexed=True)
	# publish_date 			= models.IntegerField(indexed=True)
	# publish_title 			= models.Attribute(indexed=True)
	# publish_url 			= models.Attribute(indexed=True)
	# publish_main_image_uuid = models.Attribute(indexed=True)
	# supplies_uuid 			= models.Attribute(indexed=True)

	# # References to other models
	# metadata 				= models.ListField(Metadata, indexed=True)
	# author 					= models.ReferenceField(Author, indexed=True)
	# media 					= models.ListField(Media, indexed=True)
	# items 					= models.ListField(Item, indexed=True)
	# supplies 				= models.ListField(Supply, indexed=True)

	# # Intersect for top-level
	# step_count				= models.Attribute(indexed=True)
	# primary_topic			= models.Attribute(indexed=True)
	# guide_image				= models.Attribute(indexed=True)
	# is_public				= models.BooleanField(indexed=True)
	# is_hidden				= models.BooleanField(indexed=True)
	# author_external_id		= models.Attribute(indexed=True)
	# title 					= models.Attribute(indexed=True)
	# skip_popular_feed 		= models.BooleanField(indexed=True)
	# author_tombstoned 		= models.Attribute(indexed=True)
	# summary 				= models.Attribute(indexed=True)
	# path 					= models.Attribute(indexed=True)