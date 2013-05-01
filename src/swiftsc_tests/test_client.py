# -*- coding: utf-8 -*-
"""
    Copyright (C) 2013 Kouhei Maeda <mkouhei@palmtb.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import unittest
import sys
import os.path
sys.path.append(os.path.abspath('src'))
import swiftsc.client as c
import test_vars as v


class ClientTests(unittest.TestCase):

    def test_generate_uri(self):
        self.assertEqual(c.generate_url(v.partial_uri_list_2), v.url_2)
        self.assertEqual(c.generate_url(v.partial_uri_list_3), v.url_3)
