import frappe
from jinja2 import Template
@frappe.whitelist(allow_guest=True)
def keith(text=None):
	try:
		test = frappe.get_doc("Audit Dev", "27400002")
		#return str(test)
		item_string = "<p>"
		audit_dict = test.as_dict()
		#return str(test.street_address)
		for k,v in audit_dict.iteritems():
			item_string += str(k)
			item_string += ':'
			item_string += str(v)
			item_string += "<br>"

		#return str(item.get('table_test'))
		item_string+="</p>"
		return item_string
	except Exception as e:
		return e

	return 'my name is keith'

@frappe.whitelist(allow_guest=True)
def jared(text=None):
	try:
		template = Template('Hello {{ name }}!')
		return template.render(name = 'Jared')
	except Exception as e:
		return str(e)

	return 'my name is keith'