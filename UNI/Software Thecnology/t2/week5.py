def calcCost(books):
    return books * 17.50



def main():
    books = int(input("Enter # of books: "))
    print(f"Total: $ {calcCost(books)}")


if __name__ == "__main__":
    print("=== Book Order Cost Calculator ===")
    main()