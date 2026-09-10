
import pandas as pd
import argparse
import logging
import os


# create logs folder if it does not exist
os.makedirs("logs", exist_ok=True)

# logging configuration
logging.basicConfig(
    filename="logs/converter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_csv_file(input_file):
    try:
        data = pd.read_csv(input_file)

        print("csv file loaded successfully.")
        logging.info(f"csv file loaded successfully: {input_file}")

        return data

    except FileNotFoundError:
        print("error: input csv file was not found.")
        logging.error(f"input csv file was not found: {input_file}")

    except pd.errors.EmptyDataError:
        print("error: the csv file is empty.")
        logging.error(f"csv file is empty: {input_file}")

    except Exception as e:
        print(f"error: unable to read csv file - {e}")
        logging.error(f"unable to read csv file: {e}")

    return None


def clean_data(data):
    try:
        # normalize column names
        data.columns = (
            data.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        # remove duplicate rows
        data = data.drop_duplicates()

        # handle missing email values
        data["email"] = data["email"].fillna("not_provided")

        # parse joining date
        data["joining_date"] = pd.to_datetime(
            data["joining_date"],
            errors="coerce"
        )

        print("data cleaned successfully.")
        logging.info("data cleaned successfully")

        return data

    except Exception as e:
        print(f"error: unable to clean data - {e}")
        logging.error(f"unable to clean data: {e}")

        return None


def main():
    parser = argparse.ArgumentParser(
        description="convert csv files to cleaned excel files"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="path to input csv file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="path to output excel file"
    )

    args = parser.parse_args()

    data = read_csv_file(args.input)

    if data is not None:

        print("\noriginal data:")
        print(data)

        data = clean_data(data)

        if data is not None:

            print("\ncleaned data:")
            print(data)

            try:
                # create output folder if it does not exist
                output_folder = os.path.dirname(args.output)

                if output_folder:
                    os.makedirs(output_folder, exist_ok=True)

                data.to_excel(args.output, index=False)

                print(
                    f"\nexcel file created successfully: {args.output}"
                )

                logging.info(
                    f"excel file created successfully: {args.output}"
                )

            except Exception as e:
                print(f"error: unable to create excel file - {e}")
                logging.error(
                    f"unable to create excel file: {e}"
                )


if __name__ == "__main__":
    main()

