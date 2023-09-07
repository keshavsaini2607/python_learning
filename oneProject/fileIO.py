text = input('Enter text to enter in file: ')
with open('test.txt', 'a') as file:
    file.write(f"\n{text}")
print('file is there')