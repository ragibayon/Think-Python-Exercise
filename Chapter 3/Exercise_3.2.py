# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 21:11:36 2020
Exercise 3.2 not complete
@author: Ragib Shahariar Ayon
"""
def do_twice(fun):
    fun()
    fun()
def print_spam():
    print('spam')

do_twice(print_spam)    

