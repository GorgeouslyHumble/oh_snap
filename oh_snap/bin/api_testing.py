import requests
from pprint import pprint
import simplejson as json
from redisco import models

#A playground for trying out some Python stuff that is relevant to the project

request = requests.get("http://snapguide.com/api/v1/guides/latest?limit=100")

# request = requests.get("http://snapguide.com/api/v1/guide/b995492d5e7943e3b2757a88fe3ef7c6")

my_json = request.text

value = json.loads(my_json)
# value = json.dumps(my_json)

# pprint(value['guide']['media'].keys()[0])

for item in value['guides']:
	pprint(item)

# api_response_structure = json.loads(my_json)

# pprint(api_response_structure['guides'])

# another_value = {u'author': u'Jess Ford',
#               u'author_external_id': u'0qMX97b-TamPTZdULOy4TQ',
#               u'author_image': u'0dc1dd91c05c4f999351a37f6c972e15',
#               u'author_location_text': u'Australia',
#               u'author_profile': u'jess-ford',
#               u'author_tombstoned': None,
#               u'created': 1383552436,
#               u'guide_comment_count': 6,
#               u'guide_id': 649124,
#               u'image': u'04adde7b35d5453eb38e28c6ea3b12a6',
#               u'is_hidden': False,
#               u'is_liked': False,
#               u'is_public': True,
#               u'like_count': 22,
#               u'path': u'make-pandan-chiffon-cake',
#               u'primary_topic': u'desserts',
#               u'primary_topic_display_name': u'Desserts',
#               u'public_snapshot_id': 355231,
#               u'short': u'bht2i',
#               u'skip_popular_feed': False,
#               u'slug': u'make-pandan-chiffon-cake',
#               u'step_count': 28,
#               u'summary': None,
#               u'supplies_comment_count': 0,
#               u'title': u'Make Pandan Chiffon Cake',
#               u'tombstoned': None,
#               u'topics': [u'desserts'],
#               u'total_comment_count': 7,
#               u'uuid': u'fc8f9218e7a4435db5d111655cfbbb9f',
#               u'view_count': 596}

#print another_value['author']

#pprint(value)

#print value

# class Guide(models.Model):
# 	author = models.Attribute(indexed=True)
# 	author_external_id = models.Attribute(indexed=True)
# 	author_image = models.Attribute(indexed=True)
# 	author_location_text = models.Attribute(indexed=True)
# 	author_profile = models.Attribute(indexed=True)
# 	author_tombstoned = models.Attribute(indexed=True)
# 	created = models.IntegerField(indexed=True)
# 	guide_comment_count = models.IntegerField(indexed=True)
# 	guide_id = models.IntegerField(indexed=True)
# 	image = models.Attribute(indexed=True)
# 	is_hidden = models.BooleanField(indexed=True)
# 	is_liked = models.BooleanField(indexed=True)
# 	is_public = models.BooleanField(indexed=True)
# 	like_count = models.IntegerField(indexed=True)
# 	path = models.Attribute(indexed=True)
# 	primary_topic = models.Attribute(indexed=True)
# 	primary_topic_display_name = models.Attribute(indexed=True)
# 	public_snapshot_id = models.IntegerField(indexed=True)
# 	short = models.Attribute(indexed=True)
# 	skip_popular_feed = models.BooleanField(indexed=True)
# 	slug = models.Attribute(indexed=True)
# 	step_count = models.IntegerField(indexed=True)
# 	summary = models.Attribute(indexed=True)
# 	supplies_comment_count = models.IntegerField(indexed=True)
# 	title = models.Attribute(indexed=True)
# 	tombstoned = models.Attribute(indexed=True)
# 	topics = models.ListField(unicode, indexed=True)
# 	total_comment_count = models.IntegerField(indexed=True)
# 	uuid = models.Attribute(unique=True, required=True)
# 	view_count = models.IntegerField(indexed=True)

# guides = api_response_structure['guides']

# value = 0
# for guide in guides:
# 	value += 1
# print value

# for guide in guides:
# 	guide_key = Guide.objects.get_or_create(
# 					author=guide['author'],
# 					author_external_id=guide['author_external_id'],
# 					author_image=guide['author_image'],
# 					author_location_text=guide['author_location_text'],
# 					author_profile=guide['author_profile'],
# 					author_tombstoned=guide['author_tombstoned'],
# 					created=guide['created'],
# 					guide_comment_count=guide['guide_comment_count'],
# 					guide_id=guide['guide_id'],
# 					image=guide['image'],
# 					is_hidden=guide['is_hidden'],
# 					is_liked=guide['is_liked'],
# 					is_public=guide['is_public'],
# 					like_count=guide['like_count'],
# 					path=guide['path'],
# 					primary_topic=guide['primary_topic'],
# 					primary_topic_display_name=guide['primary_topic_display_name'],
# 					public_snapshot_id=guide['public_snapshot_id'],
# 					short=guide['short'],
# 					skip_popular_feed=guide['skip_popular_feed'],
# 					slug=guide['slug'],
# 					step_count=guide['step_count'],
# 					summary=guide['summary'],
# 					supplies_comment_count=guide['supplies_comment_count'],
# 					title=guide['title'],
# 					tombstoned=guide['tombstoned'],
# 					topics=guide['topics'],
# 					total_comment_count=guide['total_comment_count'],
# 					uuid=guide['uuid'],
# 					view_count=guide['view_count'])
# 	guide_key.save()

# guide_list = Guide.objects.all()

# pprint(guide_list)

# for item in guide_list:
# 	print item.uuid

