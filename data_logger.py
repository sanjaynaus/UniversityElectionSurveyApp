# -----------------------------------------------------------
# University Election Survey App - Code Submission
# File: data_logger.py
#
# Description:
# This module handles logging of survey responses into CSV files.
#
# Usage:
# - Used by the main app during survey execution.
#
# Author: Sanjay Tamata
# Date: 25th May, 2025
# -----------------------------------------------------------


import os
import csv

DATA_FILE = "survey_responses.csv"

def initialize_csv():
    """Creates the CSV file with header if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Question", "Selected Answer", "Candidate"])

def log_response(question, answer, candidate):
    """Logs a single response to the CSV file."""
    with open(DATA_FILE, "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([question, answer, candidate])

# Initialize CSV automatically when imported.
initialize_csv()
