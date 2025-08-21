from load_csv import load
import matplotlib.pyplot as plt
import numpy as np
def main():
    income_data = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_expectancy_data = load('life_expectancy_years.csv')
    print(income_data['1900'].values)
    print(life_expectancy_data['1900'].values)
    plt.plot(income_data['1900'].values,
        life_expectancy_data['1900'].values, 'ro')
    plt.title("Year 1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xscale('log')
    plt.xticks([300, 1000, 10000,], ['300', '1k', '10k'])
    
    plt.show()
if __name__ == '__main__':
    main()
