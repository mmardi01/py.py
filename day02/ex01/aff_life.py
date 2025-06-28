from load_csv import load
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = load('life_expectancy_years.csv')
    morocco = data[data["country"] == "Morocco"]
    # print(morocco.columns.values[1:].astype(int))
    plt.plot(morocco.columns.values[1:].astype(int), morocco.values[0][1:])
    plt.suptitle('Morocco Life expectancy Projections')
    plt.ylabel('Life expectancy' )
    plt.xlabel('Year')
    plt.yticks(np.arange(30, 99, 10))
    plt.xticks(np.arange(1800, 2081, 40))
    # plt.ticks(np.arange(30, 90, 10))
    # plt.axis((1800, 2080, 30, 90))
    # df = pd.DataFrame({"Year": morocco.columns.values[1:], "Value": morocco.values[0][1:]} , columns=["Year", "Value",])
    # sns.lineplot(data=df, x='Year', y='Value')
    # plt.title("Morocco Life expectancy Projections")
    # plt.ylabel('Frequency')
    plt.show()