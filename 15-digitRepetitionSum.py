# Question 15
# Level 2

'''
Question: Write a program that computes the value of a+aa+aaa+aaaa 
with a given digit as the value of a. Suppose the following input 
is supplied to the program: 9 Then, the output should be: 11106

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.
'''

# Solution:

a = input("Enter a digit: ")
n1 = int("%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
n4 = int("%s%s%s%s" % (a,a,a,a))
# print(n1+n2+n3+n4)


# Question 64
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

# Example: If the following n is given as input to the program: 5

# Then, the output of the program should be: 3.55

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints: Use float() to convert an integer to a float

# Solution:

n=int(input("Enter a number:"))
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
# print("{:.2f}".format(sum))


# Question 65
# Write a program to compute:

# f(n)=f(n-1)+100 when n>0 and f(0)=1

# with a given n input by console (n>0).

# Example: If the following n is given as input to the program:

# 5

# Then, the output of the program should be:

# 500

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints: We can define recursive function in Python.

# Solution:

def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input("Enter a number for f(n): "))
print(f(n))