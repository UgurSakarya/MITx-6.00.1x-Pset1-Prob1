# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print:

# Number of times bob occurs is: 2


count=0
var = "bob"
for i in range(len(s)):
    if s[i:i+3] == var:       # Search by Index. i is every single element is s. it is "i+3" because we have "bob" with 3 letters
        count +=1
print(count)

