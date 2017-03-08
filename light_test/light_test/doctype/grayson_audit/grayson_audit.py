# -*- coding: utf-8 -*-
# Copyright (c) 2015, Keith and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class GraysonAudit(Document):

	def after_insert(self):
		self.name = "Audit - {} #{} - ".format(self.company_name, self.store_number) + self.name
		print "the name is: {}".format(self.name)
		pass
