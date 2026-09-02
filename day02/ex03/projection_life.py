from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Display life expectancy against income per person for 1900.

    Loads the income and the life expectancy files, takes the '1900'
    column of each, prints both arrays, then draws one green dot per
    country on a logarithmic x axis with a title and axis labels
    before showing the figure.
    """
    file_path = 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
    income_data = load(file_path)
    life_expectancy_data = load('life_expectancy_years.csv')
    incomin_data = income_data['1900'].values
    life_expectancy = life_expectancy_data['1900'].values
    print(incomin_data)
    print(life_expectancy)
    plt.plot(incomin_data, life_expectancy, 'go')
    plt.title("Year 1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xscale('log')
    plt.xticks([300, 1000, 10000,], ['300', '1k', '10k'])

    plt.show()


if __name__ == '__main__':
    main()
