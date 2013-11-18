# "supplies": [
#     {
#         "item": "Yellow squash",
#         "num": null,
#         "unit": null,
#         "denum": null,
#         "qty": null
#     },

from redisco import models

class Supply(models.Model):

	item = models.Attribute(indexed=True, required=True, unique=True)
	unit = models.Attribute(indexed=True)
	denum = models.Attribute(indexed=True)

	qty = models.IntegerField(indexed=True)
	num = models.IntegerField(indexed=True)