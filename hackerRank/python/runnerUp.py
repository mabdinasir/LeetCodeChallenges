# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input("Enter the number of participants:"))
    arr = list(map(int, input("Enter the scores: ").split()))

    # Convert the map object to a list
    arr = list(arr)
    # Remove duplicates
    arr = list(set(arr))
    # Sort the list in ascending order
    arr.sort()
    # Print the second last element
    print(arr[-2])

# Sample Input
# 5
# 2 3 6 6 5

# Sample Output
# 5