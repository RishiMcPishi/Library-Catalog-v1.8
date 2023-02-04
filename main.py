################################
#### LIBRARY CATALOG SYSTEM ####
################################

# import libraries
import os
import sys
import time
import json
from getpass import getpass as secret_input

# import checked out/returned books in a json file
filename = 'people.json'
with open(filename) as f:
  people = json.load(f)
filename = 'books_in.json'
with open(filename) as f:
  books_in = json.load(f)

# the passwords of people my class
passwords = {
  'rishi': os.getenv("rishi_password"),
  'brody': 'hockey95',
  'francisco': 'soccer34',
  'omer':'giraffe9',
  'vince':'fortnitekid69'
}

# 3 example books in library
books = {
  '4321': 'Harry Potter',
  '1111': 'Legend',
  '1234': 'Amulet',
}

# give welcome message
print(
  '--------------------------------------------------------------------------------',
  "\033[36m")
print("📚 Welcome to the catalog system! 📚", "\033[0m")

# ask for name + password with verification

name = input('What is you name? ')
name = name.lower()
if name not in people.keys():
  print('Your name is not verified.')
  sys.exit()

password = secret_input('What is your password? ')
if not password == passwords[name]:
  # password is incorrect
  print('Your password is not verified.')
  sys.exit()

print('Processing...')
time.sleep(3)

# if name and password are correct the user will be let into the system
print(f'You have been verified. Welcome Master {name.title()}! 😀')

# ask for which transaction the user would like to do
print('1 - Borrow')
print('2 - Return')
print('3 - Look at the books you have checked out.')
if name == 'rishi':
  print('4 - Reset')
options = input('What transaction would you like to do? ')

if int(options) > 3 and not name == 'rishi':
  sys.exit()

print('Processing...')
time.sleep(3)

print()
if options == '1':
  """You would like to borrow a book"""
  barcode = input('What is the code of the book you want to check out? ')
  print('Processing...')
  time.sleep(3)

  # check if library has book
  if barcode in books_in.keys():
    print('Your book has been found.')
    # make sure there was no typo in the barcode
    confirm = input(
      f'Just to confirm, you would like to check out {books_in[barcode]}? [Y/n] '
    )
    if confirm == 'Y' or confirm == 'y':
      print('Ok! 😀')
    else:
      print('Oh, looks like you made a typo.')
      sys.exit()
  else:
    # check for multiple cases of the book not being able to get checked out
    k = people[name]
    if barcode in k:
      print('You have already checked out this book.')
    elif barcode in books:
      print('This book has been checked out.')
    else:
      print('This book is not in our library.')
    sys.exit()

  # check out book
  people[name].append(barcode)
  del books_in[barcode]
  print(
    'Your book has been checked out in the system, you may take the book now. 😀'
  )
elif options == '2':
  """You would like to return"""
  barcode = input('What is the code of the book you want to return? ')
  print('Processing...')
  time.sleep(3)

  # check if books has been checked out and then check them out
  if barcode in people[name]:
    k = people[name]
    i = people[name].index(barcode)
    confirm = input(
      f'Just to confirm, you would like to return {books[barcode]}? [Y/n] ')
    if confirm == 'Y' or confirm == 'y':
      print('Ok! 😀')
    else:
      print('Oh, looks like you made a typo.')
      sys.exit()
    del k[i]
    people[name] = k
    books_in.update({barcode: books[barcode]})  # see sources at the bottom
    print('Your book has been successfully returned. 😀')
  else:
    print('You have not checked out this book.')
    sys.exit()
elif options == '3':
  if len(people[name]) > 0:
    for book in people[name]:
      print('• ', books[book])
  else:
    print('You have no books checked out.')
elif options == '4':
  # ask to reset: for me ONLY
  print('Done! 😀')
  # reset checked out books
  people = {
    'rishi': list(),
    'brody': list(),
    'francisco': list(),
  }
  books_in = {"4321": "Harry Potter", "1111": "Legend", "1234": "Amulet"}
else:
  # you gave number that doesn't correspond to an option
  sys.exit()

print(
  '--------------------------------------------------------------------------------'
)

# export checked out/returned books in a json file
filename = 'people.json'
with open(filename, 'w') as f:
  json.dump(people, f)
filename = 'books_in.json'
with open(filename, 'w') as f:
  json.dump(books_in, f)

# Thanks to these scources that helped me make this project what it is now
# https://www.w3schools.com/python/ref_dictionary_update.asp                                                             