"""
Vinnie 
24/03/2026
This program was made to simulate a book store system - Object oriented programming. We are going to have a Book class, with parameters like book name, code, category, price, and number of pages.
Then we are creating functions to perform some tasks: display introduction, creating book objects, display books information, saving it in a file, separate books through categories, and let the user find by category.

"""

class Book:
    categoryCodes = ["CS", "IS", "SE", "SO", "MI"]
    categoryNames = ["Computer science" , "Information System", "Segurity", "Society", "Miscellaneous"]
#with defacult values if nothing has been input
    def __init__(self, book_id ="", category_name_of_book="", book_title="Unknown", num_of_pages=0, price=0):
        self._book_title = book_title
        self._num_of_pages = num_of_pages
        self._price = price
        self.set_book_id(book_id)
        

    def get_book_id(self):
        return self._book_id
        
        
#Here the books are already being categorized accordingly with the prefix
    def set_book_id(self,new_id):
        prefix = new_id[0:2].upper()
        if prefix in Book.categoryCodes:
            self._book_id = new_id
        else:
            self._book_id = "MI" + new_id[2:]
            prefix = "MI"
            
        position = Book.categoryCodes.index(prefix)
        self._category_name = Book.categoryNames[position]
        
        
 #Here I am using the formatting we learned so it can look better       
    def __str__(self):
        line1 = "%-20s %s\n" % ("Book title:", self._book_title)
        line2 = "%-20s %s\n" % ("Code:", self._book_id)
        line3 = "%-20s %s\n" % ("Category:", self._category_name)
        line4 = "%-20s %d\n" % ("Pages:", self._num_of_pages)
        line5 = "%-20s $%.2f\n" % ("Price:", float(self._price)) 
    
        return line1 + line2 + line3 + line4 + line5
        
        
#I had to add this one so we can format the file names in CSV when saving in the txt.
    def to_csv(self):
        return "%s,%s,%d,%.2f" % (self._book_id, self._book_title, self._num_of_pages, self._price)
        
        
def display_introduction():
    print("*"*60)
    print("*"*16,"Welcome to Big V Bookstore","*"*16)
    print("*"*5,"Written by Gobatto de Moraes, Vinicius  12850713","*"*5)
    print("*"*60)
    
    
#I had to generalized this code so I could use it in more than one situation
def input_value(min,max, prompt):
    while True:
        try:
            number = int(input(prompt))
            if min <= number <= max:
                return number
            else:
                print(f"Number must be between {min} and {max}")
        except:
            print("Invalid input. Please use a integer number")
            
            
#Had to create this one mostly for the price, where can be accepted float numbers            
def input_float(min, max, prompt):
    while True:
        try:
            raw_input = input(prompt)
            #If user puts "," instead of ".", as I did
            clean_input = raw_input.replace(",", ".") 
            number = float(clean_input)
            if min <= number <= max:
                return number
            else:
                print("Number must be between %.2f and %.2f" % (min, max))
        except ValueError:
            print("Invalid input. Please use numbers")
            
            
def is_valid(book_id):
    if len(book_id) != 5:
        return False
    prefix = book_id[0:2]
    if not (prefix.isalpha() and prefix.isupper()):
        return False
    suffix = book_id[2:5]
    if not suffix.isdigit():
        return False
    else:
        return True
        
        
def get_book_data(n):
    book_list = []
    
    for each in range(n):
        print(f"\nInformation of book {each+1}")
        while True:
            #I put this upper() so it helps if users don't do the input with uppercase
            each_id = input("Book code: ").upper()
            if is_valid(each_id):
                break
            else:
                print("Book ID is not valid. It must be 2 letters and 3 digits")
        title=input("Book title: ")
        pages = input_value(1, 5000, "Number of pages: ")
        price = input_float(1, 5000, "Book price: $")
            
        new_book = Book(each_id, "", title,pages,price)
        book_list.append(new_book)
            
    return book_list
    
    
def display_all_books(books):
    print("\nList of books:\n")
    for each in books:
        print (each)
        
        
def save_books_to_file(filename, books):
    with open (filename + ".txt","w") as f1:
        for each in books:
            f1.write(each.to_csv() + "\n")
        print(f"Books saved to {filename}.txt")
        
        
#Loading book datas. Created clean_lines so it doesnt the program don't get Error when reading the lines        
def load_books_from_file(filename):
    copy_list = []
    try:
        with open(filename + ".txt", "r") as f1:
            for line in f1:
                clean_line = line.strip()
                if not clean_line:
                    continue
                data = clean_line.split(",")
                new_book = Book(data[0], "", data[1], int(data[2]), float(data[3]))
                copy_list.append(new_book)
        return copy_list
    except:
        return []
        
        
def get_book_lists(books):
    print("\nBook Categories\n")
    for code in Book.categoryCodes:
        count = 0
        for each_category in books:
            prefix = each_category.get_book_id()[0:2]
            if prefix == code:
                count +=1
        print (f"{code}: {count}")


def books_by_category(book_list):
    print()
    while True:
        #Input is explaining what is happening, so user can understand as well
        category = input("Which category do you want to check? (Press X to exit):\n").upper()
        list_category = []
        if category == "X":
            break
        
        for each in book_list:
            if each.get_book_id()[0:2] == category:
                list_category.append(each)
        if list_category:
            print("\nBooks on this category:\n")
            for each in list_category:
                print(each)
        else:
            print("\nNo books found on this category\n")


def main():
    display_introduction()
    number_of_books=input_value(1,1000,"\nHow many books are you entering:\n")
    library =get_book_data(number_of_books)
    display_all_books(library)
    student_surname_book = input("Your surname: ")
    save_books_to_file(student_surname_book, library)
    get_book_lists(library)
    books_by_category(library)
    library_file = load_books_from_file(student_surname_book)
    display_all_books(library_file)
    
    
if __name__ == "__main__":
    main()
