#!/usr/bin/env python3 
print("\t\tMultiplication table")
print("-" * 50)
# Display the number title
print("  |", end = '')
for j in range(1, 10):
    print("  ", j, end = ' ')
print()  #Jump to the new line 
print("--------------------------------------------------") #print("-" * 50)

# Display table body
for i in range(1, 10):
    print(i, "|", end = ' ')
    for j in range(1, 10):      #Nested Loop
        #Display the product and align properly
        #Decimal integer format with width 4
        print("%4d" % (i * j), end='|') # Or print(format(i * j, "4d"), end = ' |') 
    print() # Jump to the new line 
    
print("-" * 50) 
