def generate_pascals_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [1]  # First element of each row is always 1
        if i > 0:
            for j in range(1, i):
                # Calculate each element based on the elements from the previous row
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

# Example usage:
num_rows = 8  # Change this value to adjust the number of rows
pascals_triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(pascals_triangle)
