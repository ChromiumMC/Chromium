test = ["game1", "game2", "game3"]

# Create an empty list called 'test2' outside the loop
test2 = []

for x in test:
   # Use '+=' to append each string in the list to 'test2'
   test2 += f'AAAAA{x},'

# Convert the list 'test2' to a string using the join method
test2 = ''.join(test2)

print(test2)


