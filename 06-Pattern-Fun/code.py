# Exercise Name:
# 	06-Pattern-Fun
# Description:
# 	Prompt for row count and print a number pattern using that value
# Given:
# 	row_count = 5
# Return:
# 	1 1 1 1 1 
# 	2 2 2 2 
# 	3 3 3 
# 	4 4 
# 	5

rows = int(input('Enter the number of rows: '))

init = 1
for val in range(rows, -1, -1):
    out = ' '.join([str(init) for _ in range(val)])
    print(out)
    init += 1