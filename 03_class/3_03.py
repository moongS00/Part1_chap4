import library as l

my = l.BookRepository()

my.regisBook(l.Book('python', 20000, '123456'))
my.regisBook(l.Book('Java', 15000, '456789'))
my.regisBook(l.Book('c/c++', 25000, '159753'))

my.printBooksinfo()
my.printBookinfo('456789')
print('\n')
my.removeBook('123456')
my.printBooksinfo()