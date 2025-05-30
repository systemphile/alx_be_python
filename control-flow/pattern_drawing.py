#Python Script Drawing Patterns with Nested Loops

#prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

#initialize iterator
i = 1

#print character according to pattern size
while i <= size:
    while i <= size:
        print("*" * size)
        i += 1