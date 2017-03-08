import frappe
import datetime  # import for current date

#test_list = []


@frappe.whitelist(allow_guest=True)
def get_text_setting():
	return frappe.get_doc("Light Settings", "Light Settings").testtext


@frappe.whitelist(allow_guest=True)
def put_text_text(text=None):
	print text


@frappe.whitelist(allow_guest=True)
def insert_grayson_audit(company_name=None, store_number=None, random_text="", random_int=0):
	if company_name is None or store_number is None:
		return "Failure, {} must be given".format(("store_number", "company_name")[company_name is None])
	doc = frappe.new_doc("Grayson Audit")
	doc.update({
		"company_name": company_name,
		"store_number": store_number,
		"random_text": random_text,
		"random_int": random_int
	})
	# does not work. doc.name = "Audit - {} #{} - " + doc.name
	# try different way of inserting
	doc.insert(ignore_permissions=True)
	# docRename = frappe.get_doc("Grayson Audit", doc.name)
	# docRename.name = "Audit - {} #{} - ".format(company_name, store_number) + docRename.name
	# docRename.save(ignore_permissions=True)
	# return docRename.name
	return doc.name


@frappe.whitelist(allow_guest=True)
def test_insert_real(item_name):
	item_ref = frappe.get_doc("Item", item_name)
	print "the item_code i got was: " + str(item_ref.item_code)


@frappe.whitelist(allow_guest=True)
def test_insert_title(item_name):
	# item_ref = frappe.get_doc("Item", item_name)
	item_dic = frappe.get_all("Item", filters={'item_name': item_name}, fields={"item_name", "item_code"})
	print item_dic
	item_ref = frappe.get_doc("Item", item_dic[0]["item_code"])
	print "the item_code i got was: " + str(item_ref.item_code)
	print "the obj is: " + str(item_ref)


@frappe.whitelist(allow_guest=True)
def audit_insert(store_name, store_number, street_address, date=None):
	if date is None:
		date = str(datetime.date.today())
	doc = frappe.new_doc("Audit Dev")
	doc.update({
		"store_name": store_name,
		"street_address": street_address,
		"naming_series": store_number,
		"transaction_date": frappe.utils.data.getdate(date),
		"title": "Audit - {} #{}".format(store_name, store_number)
	})
	doc.insert(ignore_permissions=True)
	return doc.name


@frappe.whitelist(allow_guest=True)
def child_insert(parent_name, item_name, qty, location, quantity_burned_out):
	parent = frappe.get_doc("Audit Dev", parent_name)
	child = frappe.new_doc("Audit Child Dev")
	child.update({
		"fixture_type": frappe_lookup_item(item_name),
		"qty": qty,
		"location": location,
		"quantity_burned_out": quantity_burned_out
	})
	parent.append("child_table", child)
	parent.save()  # probably this
	#parent.insert()  # do i need these? maybe a save? Not sure
	#parent.submit()  # Might need ignore_permissions=True


def frappe_lookup_item(item_name):  # TODO make this work
	item_ref = frappe.get_doc("Item", item_name)
	#print
	return item_ref.as_dict

# @frappe.whitelist(allow_guest=True)
# def insert_string(text):
# 	test_list.append(text)
# 	return "Added: " + str(text)
#
# @frappe.whitelist(allow_guest=True)
# def clear():
# 	global test_list
# 	test_list = []
# 	return "List cleared!"
#
# @frappe.whitelist(allow_guest=True)
# def print_list():
# 	global test_list
# 	print test_list
# 	return test_list
