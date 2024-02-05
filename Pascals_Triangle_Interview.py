def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        # Return an empty list if n is less than or equal to 0
        return []

    # Initialize an empty list to store the Pascal's triangle
    triangle = []
    
    # Iterate over each row of the triangle
    for i in range(n):
        # Initialize an empty list to store the current row
        row = []
        
        # Iterate over each element in the current row
        for j in range(i + 1):
            # If the element is at the edges of the row, set it to 1
            if j == 0 or j == i:
                row.append(1)
            # Otherwise, calculate the element using the values from the previous row
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        # Append the current row to the triangle
        triangle.append(row)
    
    # Return the generated Pascal's triangle
    return triangle

# Test the function
print(pascal_triangle(7))
