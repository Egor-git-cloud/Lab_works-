class Book():

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")

pushkin = Book('Капитанская дочка', 'А.C. Пушкин', '1836 ')
turgenev = Book('Муму', 'И.С. Тургенев', '1852')

pushkin.get_info()
turgenev.get_info()



