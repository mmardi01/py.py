from load_csv import load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Display Morocco's life expectancy from 1800 to 2100.

    Loads life_expectancy_years.csv, keeps the Morocco row, uses the
    year column headers as the x axis and that row's values as the y
    axis, then labels the figure and shows it.
    """
    data = load('life_expectancy_years.csv')
    morocco = data[data["country"] == "Morocco"]
    plt.plot(morocco.columns.values[1:].astype(int), morocco.values[0][1:])
    plt.suptitle('Morocco Life expectancy Projections')
    plt.ylabel('Life expectancy')
    plt.xlabel('Year')
    plt.yticks(np.arange(20, 60, 20))
    plt.xticks(np.arange(1800, 2050, 40))
    plt.show()


if __name__ == '__main__':
    main()
