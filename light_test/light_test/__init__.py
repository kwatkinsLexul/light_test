import frappe

@frappe.whitelist(allow_guest=True)
def scope_test():
	return "Inside of module"