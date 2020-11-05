def print_book_info(title, author=None, year=None):
    #  Write your code here

    text = '"' + title + '"'
    if author is not None or year is not None:
        text = text + ' was written '
    if author is not None:
        text = text + 'by ' + author + ' '
    if year is not None:
        text = text + 'in ' + year + ' '
    print(text)
