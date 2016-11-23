#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'RSA algorithm practice for my course design of Network System Security Technology'

__author__ = 'Yangjie Xu'


from fractions import gcd
import sys
import random


# primeP, primeQ, productN, totientR, e, d = 0


def initKey():
	
	# primeP, primeQ, productN, totientR, e, d = 0

	primeP = 11;
	primeQ = 13;
	productN = primeP * primeQ
	totientR = (primeP - 1) * (primeQ - 1)
	e = __getE(totientR)
	d = __getD(e, totientR)
	return {'p': primeP, 'q': primeQ, 'n': productN, 'r': totientR, 'e': e, 'd': d}

	
def __getE(r):
	es = []
	for x in range(2, r):
		if gcd(x, r) == 1:
			es.append(x)
	return es[random.randint(0, len(es)-1)]


def __getD(e, totientR):
	g, x, y = __egcd(e, totientR)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % totientR


def __egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = __egcd(b % a, a)
		return (g, x - (b // a) * y, y)

