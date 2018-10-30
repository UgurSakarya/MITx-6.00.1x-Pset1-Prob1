-- MITx-6.00.1x-Pset1-Prob1
Solution for MITx: 6.00.1x Introduction to Computer Science and Programming Using Python  Problem Set 1 and Problem 1


-- Assume s is a string of lower case characters.

-- Write a program that counts up the number of vowels contained in the string s. 
-- Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
-- For example, if s = 'azcbobobegghakl', your program should print:
-- Number of vowels: 5

-- NOTE: Do not define your own VALUES!

count = 0      # defining count as 0 because we need to put them in a box as a increasing number
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="u" or i=="o":        # Conditions
        count += 1                                            # This is where magic happens.
print("Number of vowels: ", str(count))                       # Printing count AS string
