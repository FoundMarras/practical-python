# bounce.py
#
# Exercise 1.5

height = 100
number_bounces = 10

while number_bounces > 0:
    height = height * (3/5)
    number_bounces = number_bounces - 1
    print(10 - number_bounces,round(height,4))
