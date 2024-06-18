def report(s):
    # Convert the string to lowercase to make it case insensitive
    s = s.lower()
    # Iterate over each letter in the alphabet
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        # Count the occurrences of the letter in the string
        count = s.count(letter)
        # Print the letter and its count if the count is greater than zero
        if count > 0:
            print(f"{letter}: {count}")

# Example usage:
report("Hello, World!")