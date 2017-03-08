// Copyright (c) 2016, Keith and contributors
// For license information, please see license.txt

frappe.ui.form.on('light_test_doctype', {
	refresh: function(frm) {

	},
	onload: function(frm) {
		   alert("hey");
	},
});

//activate button

cur_frm.cscript.activate = function(doc, dt, dn){
	console.log("activate for " + doc + " : " + dt + " : " + dn);
	  frappe.call({
    method: "light_test.api.getTestMessage",
    callback: function(r) {alert(r.message);}
  });


alert("after frappe2");

}
