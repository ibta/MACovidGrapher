import pandas as pd
import matplotlib.pyplot as plt
from numpy import ravel
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor


def main():
    df = pd.read_csv("data/CasesByDate.csv")
    dates = []
    cases = []
    for date in df["Date"]:
        raw_date = date.split("/")
        dates.append(f"{raw_date[0]}/{raw_date[1]}")

    for new_cases in df["New"]:
        cases.append(new_cases)

    indexes_list = []
    for a in range(67):
        indexes_list.append(a)

    indexes_list = pd.DataFrame(indexes_list)

    X = indexes_list.values.reshape(-1, 1)
    y = ravel(df['New'].values.reshape(-1, 1))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # knn = KNeighborsClassifier()
    # knn.fit(X_train, y_train)
    #
    # print(X_test)
    # print(len(X_test))
    #
    # y_pred = knn.predict(X_test)
    #
    # df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
    # print(df)

    point_list = []
    for a in range(68, 70):
        point_list.append([a])

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    print(X_test[9])
    print(X_test.flatten())

    y_pred = regressor.predict(X_test)

    df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
    print(df)

    result = regressor.predict(point_list)

    print(result.flatten())

    # rfr = RandomForestRegressor()
    # rfr.fit(X_train, y_train)
    #
    # y_pred = rfr.predict(X_test)
    #
    # df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
    # print(df)
    #
    # result = rfr.predict([[df]])
    # print(f"PREDICTED({ds}): {result.flatten()}")

    # plt.xlabel("Date")
    # plt.ylabel("Cases")
    # plt.tight_layout()
    # plt.savefig("test.svg")
    cases_predicted = []
    for i in range(69):
        cases_predicted.append(regressor.predict([[i]]))

    dates_predicted = dates.copy()

    dates_predicted.append("5/7")
    dates_predicted.append("5/8")

    plt.plot(dates, cases, '-o')
    plt.plot(dates_predicted, cases_predicted, linestyle='dashed')
    ax = plt.gca()
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.title("Coronavirus Daily Cases")
    temp = ax.xaxis.get_ticklabels()
    temp = list(set(temp) - set(temp[::7]))
    for label in temp:
        label.set_visible(False)
    plt.savefig("covid_daily.png")


if __name__ == "__main__":
    main()
