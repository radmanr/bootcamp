noun = input("Type in a noun: ")
verb = input("Type in a verb: ")
place = input("Type in a place: ")
print(f"{noun} went to {place} while {verb}")

a = "tea"
b = "coffee"
a, b = b, a
print(a, b)

item = "Karak chai"
price = 1.5
qty = 3
print(f"Karak chai x3 ..... {price * qty} AED.")

minutes = int(input("Type in how many minutes: "))
hours = minutes//60
remainder = minutes%60
print(f"{hours} hours and {remainder} minutes")

age = int(input("How old are you? "))
weeks = age*52
print(f"You have been alive for {weeks} weeks")