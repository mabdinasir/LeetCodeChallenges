# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example
# records = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]
# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry. The names are printed in alphabetical order.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    records = []  # Initialize an empty list
    for _ in range(int(input("Enter number of students: "))):
        name = input("Enter a name: ")
        score = float(input("Enter a score: "))
        records.append([name, score])
    records.sort(key=lambda x: x[1])
    # Getthe second lowest grade
    second_lowest = sorted(list(set([x[1] for x in records])))[1]
    # Get the names of students with the second lowest grade
    second_lowest_names = [x[0] for x in records if x[1] == second_lowest]
    second_lowest_names.sort()
    for name in second_lowest_names:
        print(name)