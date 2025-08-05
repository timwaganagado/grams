import csv
import os
import sys

# Function to read the CSV file into a list of dictionaries
def read_csv(filename):
    data = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Function to display a subset of the data (first 5 rows for simplicity)
def print_data(data, num_rows=5):
    for row in data[:num_rows]:
        print(row)

# Function to add a row to the dataset (manually add row, could be extended)
def add_row(data, row):
    data.append(row)

# Function to sort the data by a specified column
def sort_data(data, column):
    # To handle cases where values are not directly comparable (e.g., prices as strings)
    try:
        print(f"Data sorted by {column}")
        return sorted(data, key=lambda x: float(x[column]))
    except ValueError:
        print("Error: Sorting failed due to invalid values.")
        return data
    except KeyError:
        print("Error: Sorting failed due to invalid column (Column is case sensetive).")
        return data

# Main function to run the program
def main():
    # Read the CSV data into memory
    filename = "/melb_data.csv"
    filename = os.path.dirname(sys.argv[0]) + filename
    data = read_csv(filename)

    # User interaction loop
    while True:
        print("\nOptions:")
        print("1. Print data")
        print("2. Add a row")
        print("3. Sort data by column")
        print("4. Exit")
        
        choice = input("Enter a choice: ")

        if choice == '1':
            # Print the first few rows of the data
            print_data(data)
        
        elif choice == '2':
            # Add a new row (simple example of adding a row manually)
            print("Enter the new row as a dictionary (e.g., {'Property_ID': '123456789', 'Suburb': 'Melbourne', 'Price': '1000000'}):")
            new_row = eval(input())  # In practice, you would handle this input more safely!
            add_row(data, new_row)
            print("Row added!")
        
        elif choice == '3':
            column = input("Enter the column number to sort by (e.g., 'Price', 'Rooms'): ")
            data = sort_data(data, column)
            
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()