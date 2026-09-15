name = "Radman" 
year = 2026
hours_per_week = 4

print(name)
print(year)
print(hours_per_week * 24) # you can do math with number variables
weeks = 24
total_hours = weeks * hours_per_week
print(f"{name} will train for {weeks} weeks - about {total_hours} hours.")

name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Nice to meet you, {name}. In 10 years, you will be {age+10}.")
