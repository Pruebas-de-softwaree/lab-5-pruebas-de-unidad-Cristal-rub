from book import Book
from library import Library
from user import User

#Pruebas Unitarias
def test_book():
    print("Testing Book class...")
    #Prueba unitaria 001 de la clase Book que verifica el estado inicial:
    libro = Book("1984", "George Orwell", 1949, "ISBN001")
    
    if libro.borrowed == False:
        print("Test 1 passed: Initial state is correct")
    else:
        print("Test 1 failed: Initial state is incorrect")

    #Prueba unitaria 002 de la clase Book que verifica el método borrow:
    try:
        libro.borrow()
        if libro.borrowed == True:
            print("Test 2 passed: Borrow method works correctly")
        else:
            print("Test 2 failed: Borrow method did not change state correctly")
    except ValueError as e:
        print("Test 2 failed:", e)
#Prueba unitaria 003 de la clase Book que verifica el método return_book:
    try:
        libro.return_book()
        if libro.borrowed == False:
            print("Test 3 passed: Return method works correctly")
        else:
            print("Test 3 failed: Return method did not change state correctly")
    except ValueError as e:
        print("Test 3 failed:", e)
#Prueba unitaria 004 de la clase Book que verifica que no se puede prestar un libro ya prestado.
    try:
        libro.borrow()
        libro.borrow()  # Intentar prestar de nuevo
        print("Test 4 failed: Allowed borrowing an already borrowed book")
    except ValueError as e:
        print("Test 4 passed:", e)

#Pruebas de integración:
def test_mix():
    print("Testing integration between User, Book, and Library classes...")
    #Prueba de integración 001: Usuario pide prestado un libro disponible.
    lib = Library()
    book1 = Book("1984", "George Orwell", 1949, "ISBN001")
    user1 = User("Anna", "U001")
    lib.add_book(book1)
    lib.add_user(user1)

    try:
        lib.borrow_book("U001", "ISBN001")
        if book1.borrowed == True and user1.get_history()[-1] == "Borrwed: 1984":
            print("Integration Test 1 passed: User successfully borrowed available book")
        else:
            print("Integration Test 1 failed: Book state or user history incorrect")
    except ValueError as e:
        print("Integration Test 1 failed:", e)

    #Prueba de integración 002: Usuario intenta pedir prestado un libro ya prestado.
    try:
        lib.borrow_book("U001", "ISBN001")  # Intentar prestar de nuevo
        print("Integration Test 2 failed: Allowed borrowing an already borrowed book")
    except ValueError as e:
        print("Integration Test 2 passed:", e)

    #Prueba de integración 003: Usuario devuelve un libro y otro usuario lo pide prestado.
    user2 = User("Juan", "U002")
    lib.add_user(user2)

    try:
        lib.return_book("U001", "ISBN001")
        lib.borrow_book("U002", "ISBN001")
        if book1.borrowed == True and user2.get_history()[-1] == "Borrwed: 1984":
            print("Integration Test 3 passed: Book successfully returned and borrowed by another user")
        else:
            print("Integration Test 3 failed: Book state or user history incorrect after return and borrow")
    except ValueError as e:
        print("Integration Test 3 failed:", e)


if __name__ == "__main__":
    #test_book()
    test_mix()
    print("All tests completed.")