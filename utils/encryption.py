#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'RSA algorithm practice for my course design of Network System Security Technology'

__author__ = 'Yangjie Xu'


import sys



def en(plain, e, n):
	return pow( plain, e, n )

