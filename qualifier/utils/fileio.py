# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
def save_to_csv(list_data, desired_path):
    """saves file, from user input, to CSV file"""
    with open(desired_path, "w") as open_file:
        csv_writer = csv.writer(open_file, delimiter = '\n')
        csv_writer.writerow(list_data)


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
    