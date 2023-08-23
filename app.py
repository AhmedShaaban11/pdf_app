"""
Project: PDF Application with PyPDF2
Authors: Ahmed Shaaban, Mazin El-Taher, Ahmed Hesham
Date: March. 8 2022
Version: 1.0
"""

import PyPDF2


# Tips for safe
def tip():
    print("Welcome!")
    print('=' * 20)
    print("Tips:")
    print("- Enter the full path of your files.")
    print("- You must include '.pdf' in the end of file names.")
    print("- Pages are numbered from zero.")


# Output numbers of features
def features_message():
    print('=' * 20)
    print("Available features:")
    print("1 - Merge two files")
    print("2 - Extract a page from file")
    print("3 - Split file into separate pages")
    print("4 - Exit")
    print('=' * 20)


# Merging two files in one merged file
def pdf_merge():

    # Take input from user
    file1 = input("Enter first file name: ")
    file2 = input("Enter second file name: ")
    merged_file = input("Enter name of merged file: ")

    # Open the two files
    pdf_file1 = open(file1, "rb")
    pdf_file2 = open(file2, "rb")

    # Read them by PyPDF2
    pdf_reader1 = PyPDF2.PdfFileReader(pdf_file1)
    pdf_reader2 = PyPDF2.PdfFileReader(pdf_file2)

    # Create a pdf file merger
    pdf_merger = PyPDF2.PdfFileMerger()

    # Add the two files to the merger file
    pdf_merger.append(pdf_reader1)
    pdf_merger.append(pdf_reader2)

    # If the merged file name not ended with .pdf, add it
    if merged_file[merged_file.__len__() - 4 : merged_file.__len__()] != ".pdf":
        merged_file += ".pdf"

    # Open the merged file in write mode
    pdf_file3 = open(merged_file, "wb")

    # Add the content from the pdf merger to the merged file
    pdf_merger.write(pdf_file3)

    # Close all files
    pdf_file1.close()
    pdf_file2.close()
    pdf_file3.close()


# Create a page file from one given file
def create_page(file, reader, page_num):

    # Get the page from the file
    page = reader.getPage(page_num)
    
    # Create a pdf writer
    pdf_writer = PyPDF2.PdfFileWriter()
    
    # Add the page to the pdf writer
    pdf_writer.addPage(page)

    # Put the file name as file-page_num.pdf
    page_file_name = file[:file.__len__() - 4] + '-' + str(page_num) + ".pdf"

    # Open the page file
    page_file = open(page_file_name, "wb")
    
    # Add the content from the pdf writer to the merged file
    pdf_writer.write(page_file)

    # Close the page file
    page_file.close()


# Extract a page from one file
def pdf_extract():
    
    # Take the input from user
    file = input("Enter file name: ")
    page_num = int(input("Enter page number: "))

    # Open the pdf file
    pdf_file = open(file, "rb")

    # Read it by PyPDF2
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Create the page file
    create_page(file, pdf_reader, page_num)

    # Close the file
    pdf_file.close()


# Split a file to page file for each page on it
def pdf_split():

    # Take the input from user
    file = input("Enter file name: ")

    # Open the file
    pdf_file = open(file, "rb")

    # Read it by PyPDF2
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Create a page file for each page
    for num in range(pdf_reader.numPages):
        create_page(file, pdf_reader, num)
    
    # Close the file
    pdf_file.close()


def exit():
    print('=' * 20)
    print("Goodbye!")
    global working
    working = False


def execute():
    features_message()
    num = int(input("Enter feature number: "))
    while num not in features.keys():
        num = int(input("Enter feature number: "))
    features[num]()


def main():
    tip()
    while working:
        execute()
        print("Done!")


working = True
features = {1: pdf_merge, 2: pdf_extract, 3: pdf_split, 4: exit}

main()
