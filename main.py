from SplayTree import Splay
import csv
import argparse

def main():
    parser = argparse.ArgumentParser(description='Splay tree implementation')
    parser.add_argument('csv_file', help='Path to csv file with values to insert into splay tree')    
    args = parser.parse_args()

    # Initializes the splay tree
    tree = Splay()
    
    with open(args.csv_file) as csvfile:
        value_reader = csv.reader(csvfile, delimiter=',')

        # Insert all of the values in the csv file into our
        # splay tree
        for row in value_reader:
            for value in row:
                tree.insert(value)
    
    # Prints out information about the tree
    tree.print()

if __name__ == '__main__':
    main()
