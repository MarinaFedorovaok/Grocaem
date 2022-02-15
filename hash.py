book = dict()
book['apple'] = 0.67
book['pear'] = 1.67
book['bananas'] = 0.7
#print(book['apple'])
value = book.get('apple')
def find_goods(text):
    if book.get(text):
        print ("Here is it!")
    else:
        book[text] = True
        print ("OOPS")
#find_goods('appl')
