import random
characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*"
numbers="1234567890"
all="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
special_chars="!@#$%^&*"
both="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
length_password=int(input("enter the length of the password:"))
numbers=input("do you want numbers:")
special_requires=input("do you want special requires:")
if numbers=="yes" and special_requires=="yes":
  a="".join(random.sample(both,length_password))
elif numbers=="no" and special_requires=="yes":
  a="".join(random.sample(characters,length_password))
elif special_requires=="no" and numbers=="yes":
  a="".join(random.sample(all,length_password))
elif special_requires=="no" and numbers=="no":
  a="".join(random.sample(alpha,length_password))
print(f"your password is{a}")