# Question 93
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

# Hints: Use set() and "&=" to do set intersection operation.

# Solution:

set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print(li)


# Question 94
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

# Hints: Use set() to store a number of values without duplicate.

# Solution:

def removeDuplicate( li ):
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )

    return seen

li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))