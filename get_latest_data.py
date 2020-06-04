import requests
import zipfile
from datetime import date
import calendar


def main():
    # Get the current date
    full_date = str(date.today())

    # Get the current year from the date
    year = full_date[0:4]

    # Get the current month from the date
    month = int(full_date[6])

    # Get the current day from the date
    day = full_date[8:]

    # If the day has a zero at the front of it remove it because this is the format that is followed
    if day[0] == "0":
        day = day[1]

    # Get month name
    month = str(calendar.month_name[month]).lower()

    # Assemble the current date url following the format of the urls previous
    current_date = f"https://www.mass.gov/doc/covid-19-raw-data-{month}-{day}-{year}/download"

    # Write the data.zip file to the data folder after downloading it using requests
    r = requests.get(current_date)
    with open("data/data.zip", "wb") as outfile:
        outfile.write(r.content)

    # Unzip the file
    with zipfile.ZipFile("data/data.zip") as zf:
        for file in zf.namelist():
            if file.endswith("CasesByDate.csv"):
                zf.extract(file, "data")


if __name__ == "__main__":
    main()
