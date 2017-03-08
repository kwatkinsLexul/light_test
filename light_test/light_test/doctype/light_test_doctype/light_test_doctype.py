# -*- coding: utf-8 -*-
# Copyright (c) 2015, Keith and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class light_test_doctype(Document):

	def validate(self):
		print("Grrrrrrayson - Validate")

	def on_update(self):
		print("Grayson also - Update")

	def on_submit(self):
		print("Another Grayson thing - Submit")