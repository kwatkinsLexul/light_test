import frappe

@frappe.whitelist()
def getTestMessage():
    #return "This is the test message that will be replied"
    settings = frappe.get_doc("Light Settings", "Light Settings")
    return settings.testtext;

