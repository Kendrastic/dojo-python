"""
Basic - Print all integers from 0 to 150.
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)"""


# Basic
from audioop import mul


for basic_number in range(0, 150+1):
    print(basic_number)

#Multiples of 5
for multiple_5 in range(5, 1000+1, 5):
    print(multiple_5)

#Counting

for counting_dojo_way in range(1, 100+1):
    if counting_dojo_way % 5 == 0:
        print("Coding")
    else:
        print(counting_dojo_way)

#Whoa
for whoa_integer in range(0, 500000+1):
    whoa_integer += whoa_integer
print(whoa_integer)

#Countdown by fours
for countdown_by_four in range(2018, -1, -4):
    print(countdown_by_four)

#Flexible Counter
print("flex counter")
low_num = 2
high_num = 9
mult = 3

for flexible_counter in range(low_num, high_num+1):
    if flexible_counter % mult == 0:
        print(flexible_counter)
    else: 
        continue
