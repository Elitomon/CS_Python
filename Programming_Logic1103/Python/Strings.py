# strings.py
# Eli Monroe
# 26 Oct 2021
# sample string operations

str1 = "Hello, world"
print (str1)
str2 = "Python is fun"
print (str2)

str3 = str1 + str2
print (str3)
str3 = str1 + " " + str2
print (str3)

print (" ") # repeated chars *********************************

print ("-" * 20)
print ("1" * 10 , 'w' * 14)
print ("<" * 10 , "hyper text" , ">" * 10)
print ("<" * 10 + 'hyper text' + '>' * 10)

print (" ") # escaped chars **********************************

print ("We're the so-called \"Vikings\" from the north")
print ("this is one line\nand this is another")
print ("\tThis\tis\ttabbed\toutput")

print (" ") # oop ********************************************

print (str1 , str2)
print ("str1 has", len(str1), "characters")
print ("str2 has", len(str2), "characters")
print ("first char in str1 is", str1[0])
print ("last char in str1 is ", str1[11])
print (str1.replace ("H" , "J"))
print (str1.upper())
print (str2.lower())
