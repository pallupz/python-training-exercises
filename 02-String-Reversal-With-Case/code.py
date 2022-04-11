# Exercise Name:
# 	02-String-Reversal-With-Case
# Description:
# 	Reverse each word of a string without changing upper-case positions.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"Nohtyp si Emosewa"

sentence = 'Python is Awesome'

reversed = ' '.join([word[::-1] for word in sentence.lower().split(' ')])

output = ''
for idx, char in enumerate(sentence):
    if char.isupper():
        output += reversed[idx].upper()
    else:
        output += reversed[idx]

print(output)

