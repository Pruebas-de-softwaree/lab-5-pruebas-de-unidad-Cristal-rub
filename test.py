from book import Book
from library import Library
from user import User

def test_book():
    print("Testing Book class...")
    #Prueba 1 de la clase Book que verifica el estado inicial:
    libro = Book("1984", "George Orwell", 1949, "ISBN001")
    
    if libro.borrowed == False:
        print("Test 1 passed: Initial state is correct")
    else:
        print("Test 1 failed: Initial state is incorrect")

if __name__ == "__main__":
    test_book()
    print("All tests completed.")