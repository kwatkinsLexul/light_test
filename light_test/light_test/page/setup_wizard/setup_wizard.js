frappe.pages['setup-wizard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Setup Wizard',
		single_column: true
	});
}