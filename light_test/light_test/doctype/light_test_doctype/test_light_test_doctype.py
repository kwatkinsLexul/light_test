# -*- coding: utf-8 -*-
# Copyright (c) 2015, Keith and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

# test_records = frappe.get_test_records('light_test_doctype')

class Testlight_test_doctype(unittest.TestCase):
	pass
@frappe.whitelist()
def test_method():
    msgprint("Hello from python!")


def validate(self):
    print("Grrrrrrayson")