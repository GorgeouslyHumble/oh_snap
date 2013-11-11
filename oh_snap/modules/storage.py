# This module contains all the methods that stores data returned from the API and also handles retrieving that data from Redis so that it could be consumed by the application's views
#
# Rules for Storage:
#
# 1. Any method that retrieves data from the database has the 'retrieve' postfix attached to the method name
#
# 2. Any method that accepts multiple parameters will accept a dictionary
#
# 3. Every guide is returned as a dictionary. Every list of guides is returned as a list of dictionaries.
#
# 4. Something to note is that the retrieve_guide_list method exists in both the API class and the Storage class, you can tell which one is being called by which class that is being instantiated in the application's views

import redisco
import simplejson as json
from modules.api import API
#Import ALL the models!
from models.item import Item
from models.content import Content
from models.media import Media
from models.metadata import Metadata
from models.topic import Topic
from models.guide import Guide

class Storage:

	def store_author(self, **author):
		author_key = Author.get_or_create(
			first_name 				= author['first_name'],
			last_name 				= author['last_name'],
			name 					= author['name'],
			image 					= author['image'],
			is_following_author 	= author['is_following_author'],
			profile_path 			= author['profile_path'],
			external_id 			= author['external_id']
			)

		author_key.is_valid()
		author_key.save()

		return author_key

	def store_content(self, **content):
		content_key = Content.get_or_create(
			text 				= content['text'],
			caption 			= content['caption'],
			media_item_uuid 	= content['media_item_uuid']
			)

		content_key.is_valid()
		content_key.save()

		return content_key

	def store_item(self, **item):
		content = self.store_content(**item['content'])

		item_key = Item.get_or_create(
			content 		= content,
			comment_count 	= item['content_count'],
			type 			= item['type'],
			uuid 			= item['uuid']
			)

		item_key.is_valid()
		item_key.save()

		return item_key

	def store_media(self, **media):
		media_key = Media.get_or_create(
			uuid 			= media.keys()[0],
			url 			= media['url'],
			width 			= media['width'],
			media_type 		= media['media_type'],
			content_type 	= media['content_type']
			height 			= media['height']
			)

		media_key.is_valid()
		media_key.save()

		return media_key

	def store_metadata(self, **metadata):
		metadata_key = Metadata.get_or_create(
			category 			= metadata['category'],
			title 				= metadata['title'],
			primary_topic 		= metadata['primary_topic'],
			is_request_attached = metadata['is_request_attached'],
			summary 			= metadata['summary'],
			main_image_uuid 	= metadata['main_image_uuid']
			original_request_id = metadata['original_request_id'],
			admin_topics 		= metadata['admin_topics'],
			topics 				= metadata['topics']
			)

		metadata_key.is_valid()
		metadata_key.save()

		return metadata_key

	def store_topic(self, **topic):
		topic_key = Topic.get_or_create(
			uuid = topic['uuid'],
			thumb_image_uuid 	= topic['thumb_image_uuid'],
			cover_image_uuid 	= topic['cover_image_uuid'],
			cover_image_type 	= topic['cover_image_type'],
			description 		= topic['description'],
			short_description 	= topic['short_description'],
			display_name 		= topic['display_name'],
			slug 				= topic['slug'],
			is_editorial 		= topic['is_editorial'],
			skip_featured_view 	= topic['skip_featured_view'],
			has_subtopics 		= topic['has_subtopics']
			)

		topic_key.is_valid()
		topic_key.save()

		return topic_key

	def store_guide(self, uuid):
		request = API()
		guide = request.retrieve_guide(uuid)
		author = self.store_author(guide['author'])
		metadata = self.store_metadata(guide['metadata'])

		media = []
		items = []
		supplies = []

		for media_item in guide['media']:
			media.extend(self.store_media(media_item))

		for item in guide['items']:
			items.extend(self.store_item(item))

		for supply in guide['supplies']
			supplies.extend(self.store_supply(supply))

		guide = Guide.objects.get_or_create(
			last_edited 				= guide['last_edited'],
			master_uuid 				= guide['master_uuid'],
			branch_uuid 				= guide['branch_uuid'],
			branch_point_master_seq 	= guide['branch_point_master_seq'],
			branch_point_seq 			= guide['branch_point_seq'],
			branch_point_txn_id 		= guide['branch_point_txn_id'],
			publish_date 				= guide['publish_date'],
			publish_title				= guide['publish_title'],
			publish_main_image_uuid		= guide['publish_main_image_uuid'],
			supplies_uuid				= guide['supplies_uuid'],
			metadata 					= metadata,
			author                      = author,
			media 						= media,
			items 						= items,
			supplies 					= supplies
			)

		guide.is_valid()
		guide.save()

		return guide

	# Stores all the guides returned from a top-level respose
	def store_guides_from_top(self):
		request = API()
		guide_list_params = {'time_point' : 'latest', 'limit' : '100'}
		guide_list_json = request.retrieve_guide_list(**guide_list_params)

		author = self.

		for guide in guide_list_json:
			guide = Guide.objects.get_or_create(
				author 						= guide['author'],
				author_external_id 			= guide['author_external_id'],
				author_image 				= guide['author_image'],
				author_location_text 		= guide['author_location_text'],
				author_profile 				= guide['author_profile'],
				author_tombstoned 			= guide['author_tombstoned'],
				created 					= guide['created'],
				guide_comment_count 		= guide['guide_comment_count'],
				guide_id 					= guide['guide_id'],
				image 						= guide['image'],
				is_hidden 					= guide['is_hidden'],
				is_liked 					= guide['is_liked'],
				is_public 					= guide['is_public'],
				like_count 					= guide['like_count'],
				path 						= guide['path'],
				primary_topic 				= guide['primary_topic'],
				primary_topic_display_name 	= guide['primary_topic_display_name'],
				public_snapshot_id 			= guide['public_snapshot_id'],
				short 						= guide['short'],
				skip_popular_feed 			= guide['skip_popular_feed'],
				slug 						= guide['slug'],
				step_count 					= guide['step_count'],
				summary 					= guide['summary'],
				supplies_comment_count 		= guide['supplies_comment_count'],
				title 						= guide['title'],
				tombstoned 					= guide['tombstoned'],
				topics 						= guide['topics'],
				total_comment_count 		= guide['total_comment_count'],
				uuid 						= guide['uuid'],
				view_count 					= guide['view_count']
				)

			guide.is_valid()
			guide.save()

			return guide_list_json

	# Wasn't sure how to name this sucka'. It stores all the metadata for a single guide.
	# Unfortunately, how it is written at the moment is that it requires a network call per iteration. Threading and maybe memoization can probably cut down the execution time. However, because it will be on a queue and because of the scope of the current iteration of this program, I don't necesserily need a high performing pull
	def store_guides_all(self):
		guide_list_json = self.store_guides_from_top

		for guide in guide_list_json:
			self.store_guide(uuid=guide['uuid'])


	def retrieve_guide(self, uuid):
		guide = Guide.objects.filter(uuid=uuid)[0]

		return guide.attributes_dict

	#I'll add some filters in later... in case I want to grow the application in a way that requires that it needs to store more than the top 100 guides
	def retrieve_guide_list(self):
		guides = Guide.objects.all()

		return guides

		