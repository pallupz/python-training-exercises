# Exercise Name:
# 	03-List-Manipulation
# Description:
# 	Remove items greater than 50 from a list while iterating but without creating a different copy of a list.
# Given:
# 	number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Return:
# 	[10, 20, 30, 40, 50]
# Note:
# 	ID of input and output list should match

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(number_list)
print(id(number_list))

i = 0
n = len(number_list)
while i < n:
    if number_list[i] > 50:
        del number_list[i]
        n -= 1
    else:
        i += 1

print(number_list)
print(id(number_list))