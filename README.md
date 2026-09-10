# Syntecxhub CSV to Excel Converter

A Python command-line tool that reads CSV files, cleans and normalizes the data, and converts the cleaned data into an Excel `.xlsx` file.

## Features

* Read CSV files using pandas
* Normalize column names
* Remove duplicate rows
* Handle missing email values
* Parse date values
* Export cleaned data to Excel
* Command-line input and output options
* Automatic output folder creation
* Logging of successful operations and errors
* Error handling for missing and empty CSV files

## Technologies Used

* Python
* Pandas
* OpenPyXL
* Argparse
* Logging

## Project Structure

```text
Syntecxhub_CSV_Excel_Converter/
│
├── input/
│   └── sample_data.csv
│
├── output/
│   └── final_data.xlsx
│
├── logs/
│   └── converter.log
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Create and activate a virtual environment:

```bash
py -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

Run the converter using the following command:

```bash
py main.py --input input/sample_data.csv --output output/final_data.xlsx
```

### Command-line options

`--input`
Path of the input CSV file.

`--output`
Path where the converted Excel file will be created.

## Data Cleaning

The application performs the following cleaning operations:

1. Converts column names to lowercase.
2. Replaces spaces in column names with underscores.
3. Removes duplicate rows.
4. Replaces missing email values with `not_provided`.
5. Converts joining date values into a proper date format.
6. Handles invalid or missing dates using `NaT`.

## Error Handling

The application handles common errors such as:

* Input CSV file not found
* Empty CSV file
* CSV reading errors
* Data cleaning errors
* Excel file creation errors

## Logging

Application activities and errors are stored in:

```text
logs/converter.log
```

The log file records successful operations and errors for easier debugging.

## Example

Input:

```text
First Name,Last Name,Email,Joining Date,Department,Salary
Yogita,Nalawade,yogita@example.com,2026-01-15,IT,35000
```

After cleaning, the column names become:

```text
first_name
last_name
email
joining_date
department
salary
```

The cleaned data is exported to:

```text
output/final_data.xlsx
```

## Internship Project

This project was developed as part of the Syntecxhub Python internship project.

## Author

Yogita Nalawade
