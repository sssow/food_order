# -*- coding: utf-8 -*-
# Copyright (c) 2018, Shapelite and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RestaurantOrder(Document):
	def validate(self):
		total = 0
		for item in self.ro_items:
			total = total + (item.oi_quantity * float(item.oi_price))
		self.ro_total = total
		frappe.logger(__name__).debug('Total is {0}'.format(total))
