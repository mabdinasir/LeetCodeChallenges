# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example

# : Append  to the list, .
# : Append  to the list, .
# : Insert  at index , .
# : Print the array.
# Output:
# [1, 3, 2]

if __name__ == '__main__':
    N = int(input("Enter the number of commands: "))
    list = []
    for i in range(N):
        command = input("Enter the command: ").split()
        if command[0] == 'insert':
            list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(list)
        elif command[0] == 'remove':
            list.remove(int(command[1]))
        elif command[0] == 'append':
            list.append(int(command[1]))
        elif command[0] == 'sort':
            list.sort()
        elif command[0] == 'pop':
            list.pop()
        elif command[0] == 'reverse':
            list.reverse()
        else:
            print("Invalid command")