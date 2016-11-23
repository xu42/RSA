#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'RSA algorithm practice for my course design of Network System Security Technology'

__author__ = 'Yangjie Xu'


from utils import key, encryption, decryption


def features():

	print()
	print("----------- Welcome ------------")
	print("       My course design")
	print("     RSA algorithm practice")
	print("Network System Security Technology")
	print()
	
	message = input("Please enter the message to be encrypted: ")
	message = int(message)

	myKey = key.initKey()

	print()
	print("----------- Variables Begin ------------")
	print("** p = " + str(myKey['p']))
	print("** q = " + str(myKey['q']))
	print("** n = " + str(myKey['n']))
	print("** r = " + str(myKey['r']))
	print("** e = " + str(myKey['e']))
	print("** d = " + str(myKey['d']))
	print("----------- Variables End ------------")

	print()
	print("----------- Keys Begin ------------")
	print("** Public  Key (n,e) = (" + str(myKey['n']) + "," + str(myKey['e']) + ")")
	print("** Private Key (n,d) = (" + str(myKey['n']) + "," + str(myKey['d']) + ")")
	print("----------- Keys End ------------")

	cipher = encryption.en(message, myKey['e'], myKey['n'])
	plain = decryption.de(cipher, myKey['d'], myKey['n'])

	print()
	print("** Encrypted: " + str(cipher))
	print("** Decrypted: " + str(plain))


if __name__=='__main__':
    features()
