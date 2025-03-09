#!/usr/bin/env python3

# Author ID: SMISHRA27 / 137285227

def read_file_string(file_name):

    """Reading the file and returns it as a single string."""

    with open(file_name, 'r') as file:

        return file.read()

def read_file_list(file_name):

    """Reading a file and returns its lines as a list, stripping newline characters."""

    with open(file_name, 'r') as file:

        return [line.strip() for line in file]


if __name__ == '__main__':

    file_name = 'data.txt'

    print(read_file_string(file_name))

    print(read_file_list(file_name))
