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

    plt.plot(dates, cases, '-o')

    ax = plt.gca()
    plt.xlabel("Date")
    plt.ylabel("Active Cases")
    plt.title("Coronavirus Active Cases")
    temp = ax.xaxis.get_ticklabels()
    temp = list(set(temp) - set(temp[::7]))
    for label in temp:
        label.set_visible(False)
    plt.savefig("graphs/covid_daily.png")


if __name__ == "__main__":
    main()
