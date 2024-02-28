import sys
import datetime
import csv
import os


def main():
    # filename= f"{datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S.%f")[:-3]}".md"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S.%f")[:-3]
    folder_path = "entries"

    # Check if the folder exists, create it if it doesn't
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    filename = os.path.join(folder_path, f"{timestamp}.md")
    print(filename)
    try:
        with open(filename, "a") as file:
            file.write("This is a new line\n")
    except FileNotFoundError:
        sys.exit("File not found.")




if __name__ == "__main__":
    main()
