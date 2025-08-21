from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def str_to_int(value_str: str):
    if value_str.endswith("M"):
        value = float(value_str[:-1]) * 1_000_000
        return value
    if value_str.endswith("K"):
        value = float(value_str[:-1]) * 1_000
        return value
    else:
        value = float(value_str[:-1])
        return value


def main():
    data = load('population_total.csv')
    moroccon_data = data[data["country"] == "Morocco"]
    albanian_data = data[data["country"] == "Albania"]

    moroccon_data_values = [str_to_int(v)
                            for v in moroccon_data.values[0][1:252]]
    albanian_data_values = [str_to_int(v)
                            for v in albanian_data.values[0][1:252]]
    plt.plot(moroccon_data.columns.values[1:252].astype(int),
             moroccon_data_values, label='Morocco')
    plt.plot(albanian_data.columns.values[1:252].astype(int),
             albanian_data_values, label='Albania')
    plt.suptitle('Population Projections')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.xticks(np.arange(1800, 2041, 40))
    plt.yticks([20000000, 40000000, 60000010,], ['20M', '40M', '60M'])
    plt.legend(loc='lower right')
    plt.show()


if __name__ == '__main__':
    main()
