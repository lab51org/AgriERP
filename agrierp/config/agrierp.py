from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Anagrafiche"),
			"items": [
				{
					"type": "doctype",
					"name": "Regione",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Provincia",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Comune",
					"onboard": 1,
				}
			]
		}
	]