#######################################
#### SIMPLE LIBRARY CATALOG SYSTEM ####
#######################################

# import libraries
import sys
import time
import json

# import checked out/returned books in a json file
filename = 'people.json'
with open(filename) as f:
  people = json.load(f)
filename = 'books_in.json'
with open(filename) as f:
  books_in = json.load(f)

# 3 example children in our grade
# people = {
# 'rishi' : list(),
# 'brody' : list(),
# 'franny' : list(),
# }

# 3 example passwords for each person
passwords = {
  'rishi': 'hello88',
  'brody': 'hockey01',
  'franny': 'socks97',
}

# 3 example books in library
books = {
  '4321': 'Harry Potter',
  '1111': 'Legend',
  '1234': 'Amulet',
}

# books_in = {
# 4321 : 'Harry Potter',
# 1111 : 'Legend',
# 1234 : 'Amulet',
# }

# ask to reset: for developers ONLY
resetting = input('Would you like to reset? [Y/n] ')
if resetting == 'y' or resetting == 'Y':
  print('Processing...')
  # reset checked out books
  people = {
    'rishi': list(),
    'brody': list(),
    'franny': list(),
  }
  books_in = {
    "4321": 'Harry Potter',
    "1111": 'Legend',
    "1234": 'Amulet',
  }

  time.sleep(3)

# ask for name + password
name = input('What is you name? (all lower case) ')
if name not in people.keys():
  print('Your name is not verified')
  sys.exit()

password = input('What is your password? ')
if not password == passwords[name]:
  print('Your password is not verified')
  sys.exit()

# if name and password are correct the user will be let into the system
print('You have been verified. Welcome Mr.', name)
  
# ask if you would like to return or borrow
return_or_borrow = input('Would you like to return or borrow? ')
if return_or_borrow == 'borrow':
  print('Processing...')
  return_or_borrow = True
elif return_or_borrow == 'return':
  print('Processing...')
  return_or_borrow = False
else:
  sys.exit()

if return_or_borrow:
  """You would like to check-out"""
  barcode = input('What is the barcode of the book you want to check out? ')
  print('Processing...')
  time.sleep(3)

  # check if library has book
  if barcode in books_in.keys():
    print('Your book has been found')
  else:
    print('This book has been checked out or is not in our library')
    sys.exit()

  # check out book
  people[name].append(barcode)
  del books_in[barcode]
  print(
    'Your book has been checked out in the system, you may take the book now.')
else:
  """You would like to return"""
  barcode = input('What is the barcode of the book you want to return? ')
  print('Processing...')
  time.sleep(3)

  # check if books has been checked out and then check them out
  if barcode in people[name]:
    k = people[name]
    i = people[name].index(barcode)
    del k[i]
    people[name] = k
    books_in.update({barcode: books[barcode]})
    print('Your book has been successfully returned')
  else:
    print('This book has not been checked out or is not in our library')
    sys.exit()
# asks to view books
print()
show_books = input(
  'Would you like to see all the books you have checked out? [Y/n] ')
print()
if show_books == 'y' or show_books == 'Y':
  if len(people[name]) > 0:
    for book in people[name]:
      print('• ', books[book])
  else:
    print('You have no books checked out')

# export checked out/returned books in a json file
filename = 'people.json'
with open(filename, 'w') as f:
  json.dump(people, f)
filename = 'books_in.json'
with open(filename, 'w') as f:
  json.dump(books_in, f)
