name = input("Enter a string: ")
char_frequency = {}
for char in name:
    if char != ' ':
        char_frequency[char] = char_frequency.get(char, 0) + 1
print("Character Frequency: ")    
for char, count in char_frequency.items():
    print(f"{char}: {count}")
