import json
import random

file = open("bible.json")
data = json.load(file)
books = data['books']

rand_book_no = random.randrange(len(books))

rand_book = books[rand_book_no]

book = rand_book['name']

rand_chapter_no = random.randrange(len(rand_book['chapters']))
rand_chapter = rand_book['chapters'][rand_chapter_no]

chapter = rand_chapter['num']

rand_verse_no = random.randrange(len(rand_chapter['verses']))
rand_verse = rand_chapter['verses'][rand_verse_no]

verse = rand_verse['num']

print(rand_verse['text'] + "\n    - " + book + " " + str(chapter) + " : " + str(verse))
