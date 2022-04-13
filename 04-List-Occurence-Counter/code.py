# Exercise Name:
# 	04-List-Occurence-Counter
# Description:
# 	Display all duplicate items from a list
# Given:
# 	sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
# Return:
# 	[20, 60, 30]
# Hint: 
# 	Count occurence of each item in the list and print items occuring more than once.

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]


import collections

duplicates = []
for item, count in collections.Counter(sample_list).items():
    if count > 1:
        duplicates.append(item)

print(sample_list)
print(duplicates)




# counts = {}
# for ele in sample_list:
#     if ele in counts:
#         counts[ele] += 1
#     else:
#         counts[ele] = 1

# print(counts)

# dupes = []
# for key, value in counts.items():
#     if value > 1:
#         dupes.append(key)

# print(dupes)