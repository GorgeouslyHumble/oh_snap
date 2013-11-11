# This module contains methods for directly interfacing with Snapguide's API
#
# Rules for API:
#
# 1. The prefix string will always contain a backslash and, subsequently, the postfix string will not lead with a backslash
#	 Example: "http://mylittleponyfanclub.com/api/v9001/ + bronies/brony_uuid"
#
# 2. Any method that makes a request against the API has the 'retrieval' prefix as part of the method name
#
# 3. The construct_endpoint method will only point to a 'category' destination - URL parameters are left up to the retrieval method
#
#			 construct_endpoint    retrieval method
#                     |            |        |
#	Example: "{root_endpoint}/{query}?{parameter}"
#
# 4. Something to note is that the retrieve_guide_list method exists in both the API class and the Storage class, you can tell which one is being called by which class that is being instantiated in the application's views

import requests
import simplejson as json

class API:

	# Normalize the json reponses from the api
	def normalize_response(self, unicode_text):
		response_structure = json.loads(unicode_text)

		# Returns a dictionary
		return response_structure

	# Constructs the endpoint for an API category using the root endpoint
	def construct_endpoint(self, point):
		root = "http://snapguide.com/api/v1/"
		endpoint = root + point + "/"

		return endpoint

	# I don't know if I'll actually use this method since everything is being cached and it'll be quicker to just retrieve it from Redis. Oh, and one less thing will break if the application can't connect to the API (considering that the data store has junk in it)
	def retrieve_guide(self, uuid):
		endpoint = self.construct_endpoint('guide')

		params_string = "{endpoint}/{uuid}".format(endpoint=endpoint, uuid=uuid)
		request = requests.get(params_string)
		response = self.normalize_response(request.text)

		return response

	# A method to retrieve an amount (specified by the limit parameter) of guides from a time point (latest, for example)
	# Any method that takes in more than one argument will take in a dictionary
	def retrieve_guide_list(self, **params):
		time_point = params['time_point']
		limit = params['limit']

		endpoint = self.construct_endpoint('guides')

		params_string = "{endpoint}/{time_point}?limit={limit}".format(endpoint=endpoint, time_point=time_point, limit=limit)
		request = requests.get(params_string)
		response = self.normalize_response(request.text)

		return response['guides']

