from booklover import BookLover

test = BookLover("David H.", "fxj5fe@virginia.edu", "drama")

test.add_book("Star Wars", 5)

test.num_books_read()

print("Number of books read:", test.num_books_read())