from book import Book
from library import Library
from user import User

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

if __name__ == "__main__":
    test_book()
    print("All tests completed.")