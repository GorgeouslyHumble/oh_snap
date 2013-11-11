# This module is used by the application to construct links to resources in S3. Initially, this will be the image for a guide... but the API documentation hints at other resources
#
# S3_links rules:
#
# 1. The image attribute is a string used for constructing a link to the guide's image - which exists in a Snapguide owned S3 bucket
#
# Example: http://images.snapguide.com/images/<type>/<unique_identifier>/<size>.jpg
#
# The <type> can be guide, profile, or topic. <unique_identifier> is that image attribute string. The <size> is the size PLUS the cropping strategy.
#
# 2. The URIs are constructed similar to how the API URIs are constructed in the API class. A category is provided by the endpoint method and filters are provided by the method dedicated to pulling that specific resource
#
# 3. How URIs are constructed ar also similar to the API class... postfix strings lead with a blackslash

class S3_links:

	#Constructs the endpoint for an S3 category using the root URI
	def construct_endpoint(self, type):
		root = "http://images.snapguide.com/images"
		endpoint = root + point + "/"

		return endpoint

	#Constructs the link itself
	def construct_link(self, **construct_link_params):
		resource_type = construct_link_params['resource_type']
		uuid = construct_link_params['uuid']
		size = construct_link_params['size']

		endpoint = self.construct_endpoint(resource_type)

		link = "{endpoint}/{uuid}/{size}.jpg".format(endpoint=endpoint, uuid=uuid, size=size)

		return link