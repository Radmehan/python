def searcher():
    import time
    #some 4 seconds time consuming task
    book="This is a book on Harry and code with Harry and good"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")

search=searcher()
print("Search started")
next(search)
print("Next method run")
search.send("Harry")

search.close()


# input("Press any key : ")
# search.send("Harry and")
# input("Press any key : ")
# search.send("this is")
# input("Press any key : ")
# search.send("joker")
# input("Press any key : ")
# search.send("like thid video")





