# 1. Caeser Cipher ---Starts

"""
This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during the Gallic Wars.
The idea is rather simple – every letter of the message is replaced by its nearest consequent (A becomes B, B becomes C, and so on).
The only exception is Z, which becomes A.


text = input("Enter your message: ")
cipher = ''

for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)
    
print(cipher)

"""
# Caeser Cipher ---Ends


# 2. --Numbers Processor--

"""
#The processing will be extremely easy
#– we want the numbers to be summed.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0

try:
    for substr in strings:
        total += float(substr)
    print("The total is: ", total)
except:
    print(substr, " is not a number.")

"""
#--Numbers Processor-- End

# 3. IBAN Validator

'''
iban = input("Enter IBAN, please: ")
iban = iban.replace(' ', '')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short")
elif len(iban) > 31:
    print("IBAN entered is too long")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid")
'''        
# ---IBAN Validator ends

# 4. Caesar cipher improved

# Input the text you want to encrypt.

'''
text = input("Enter message: ")

# Enter a valid shift value (repeat until it succeeds).
shift = 0

while shift == 0:
    try:    
        shift = int(input("Enter the cipher shift value (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Incorrect shift value!")

cipher = ''

for char in text:
    # Is it a letter?
    if char.isalpha():
        # Shift its code.
        code = ord(char) + shift
        # Find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Make correction.
        code -= first
        code %= 26
        # Append the encoded character to the message.
        cipher += chr(first + code)
    else:
        # Append the original character to the message.
        cipher += char

print(cipher)
'''

# 5. Palindromes: It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.
'''
text = input("Enter text: ")

# Remove all spaces...
text = text.replace(' ','')

# ... and check if the word is equal to reversed itself
if len(text) > 1 and text.upper() == text[::-1].upper():
	print(text, "is a palindrome")
else:
	print(text, "is not a palindrome")
'''

# 6. Anagram:
#An anagram is a new word formed by rearranging the letters of a word,
#using all the original letters exactly once.
#For example, the phrases "rail safety" and
#"fairy tales" are anagrams, while "I am" and "You are" are not.

# Solution Hints: This is what we're going to do with both strings:
# - remove spaces
# - change all letters to upper case
# - convert into list
# - sort the list
# - join list's elements into string
# and finally, compare both strings.
# Let's do it!
    
'''
str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
if len(strx_1) > 0 and strx_1 == strx_2:
	print("Anagrams")
else:
	print("Not anagrams")
'''
# 7. The Digit of Life

# It's simple – you just need to sum all the digits of the date.
# If the result contains more than one digit,
# you have to repeat the addition until you get exactly one digit.
'''
date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
if len(date) != 8 or not date.isdigit():
    print("Invalid date format.")
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print("Your Digit of Life is: " + date)
'''

# 8. Find a word!

# Your task is to write a program which answers
# the following question: are the characters comprising
# the first string hidden inside the second string?

'''
word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Yes")
else:
	print("No")
'''

# 9. Sudoku

# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Enter row #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Incorrect row data - 9 digits required")
    rows.append(row)

ok = True

# Check if all rows are good.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Check if all columns are good.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Make a string containing all digits from a sub-square.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")