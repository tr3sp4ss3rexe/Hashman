#!/usr/bin/python3
##########################################################
# Made by 						 #
# Daniel M. Fard					 #
# EC-Council ECE credits(Development of a security tool) #
##########################################################

import hashlib
import os
from pyfiglet import Figlet as F

######
f = F(font="standard")
print (f.renderText("Hashman\n"))
print("Hello, Welcome to Hashman!")
input("press Enter to continue...")

os.system("cls" if os.name == "nt" else "clear")

######
alpha = '"{}"'.format(input("Enter the text you want to encrypt: "))
os.system("cls" if os.name == "nt" else "clear")

######
print("1) MD5\n")
print("2) SHA-1\n")
print("3) SHA-256\n")
print("4) SHA-224\n")
print("5) SHA-384\n")
print("6) SHA-512\n")

beta = input("choose an algorithm: ")

if beta == "1":
	gamma = hashlib.md5(str(alpha).encode("utf-8")).hexdigest()
	print(gamma)
	
elif beta == "2":
	delta = hashlib.sha1(str(alpha).encode("utf-8")).hexdigest()
	print(delta)
	
elif beta == "3":
	epsilon = hashlib.sha256(str(alpha).encode("utf-8")).hexdigest()
	print(epsilon)
	
elif beta == "4":
	zeta = hashlib.sha224(str(alpha).encode("utf-8")).hexdigest()
	print(zeta)
	
elif beta == "5":
	eta = hashlib.sha384(str(alpha).encode("utf-8")).hexdigest()
	print(eta)
	
elif beta == "6":
	theta = hashlib.sha512(str(alpha).encode("utf-8")).hexdigest()
	print(theta)
	
else: 
	print("Mentioned cifer is not supported! Try again!")





