# Open the file and read the content
with open('C:\\Users\\jhili\\Python\\Decorator\\hello.txt', 'r') as file:
    words = file.read().split()

# Using list comprehension to find words starting with 'A' or 'a'
a_words = [word for word in words if word.lower().startswith('a')]

# Print the list
print(a_words)