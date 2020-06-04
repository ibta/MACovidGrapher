import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("data/CasesByDate.csv")
    dates = []
    cases = []
    for date in df["Date"]:
        raw_date = date.split("/")
        dates.append(f"{raw_date[0]}/{raw_date[1]}")

    for new_cases in df["New"]:
        cases.append(new_cases)
    plt.plot(dates, cases)
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
