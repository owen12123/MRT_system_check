import csv
import sys
import os

# Help segment of the program
Syntax_Help = '{0} csv_file'

# System check
# Function printing each row of a CSV file
def print_csv(name: str) -> None:
    # Opens a file as a CSV
    with open(name, 'r') as fin:
        reader = csv.reader(fin, delimiter = ',')

        # Prints each row individually
        for row in reader:
            print(row)


# Entry point of the application
if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            print_csv(sys.argv[1])
        else:
            print(Syntax_Help.format(os.path.basename(sys.argv[0])))

    except Exception as e:
        print("<Error>\t{0}".format(e.args[0]))
