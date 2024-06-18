def mult(rows, cols):
    # Initialize a 2D list with zeros
    table = [[0] * cols for _ in range(rows)]
    print(table)
    
    # Fill the table with multiplication results
    for i in range(rows):
        for j in range(cols):
            table[i][j] = (i + 1) * (j + 1)
    
    return table

# Example usage:
rows = 5
cols = 5
multiplication_table = mult(rows, cols)

# Print the multiplication table
for row in multiplication_table:
    print(row)