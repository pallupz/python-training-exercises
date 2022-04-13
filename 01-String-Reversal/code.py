# Exercise Name:
# 	01-String-Reversal
# Description:
# 	Reverse each word of a string.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"nohtyP si emosewA"

sentence = 'Python is Awesome'

reversed = ' '.join([word[::-1] for word in sentence.split(' ')])

print(sentence)
print(reversed)