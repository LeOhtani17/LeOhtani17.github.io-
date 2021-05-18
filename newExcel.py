#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:17:57 2020

@author: yushi
"""

import openpyxl as px

book = px.Workbook()
book.get_sheet_names()

sheet = book.get_sheet_by_name('Sheet')


sheet['A1'] = '企業名'
sheet['B1'] = 'URL'

sheet['A2'] = 'google'
sheet['A3'] = 'apple'
sheet['A4'] = 'facebook'
sheet['A5'] = 'amazon'


book.save('yamaguchi.xlsx')