from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Anagrafiche"),
			"items": [
				{
					"type": "doctype",
					"name": "Comune",
					"label": _("Comuni"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Location",
					"label": _("Terreni"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Asset",
					"label": _("Mezzi e Attrezzatura"),
					"onboard": 1,
				}
			]
		}
	]