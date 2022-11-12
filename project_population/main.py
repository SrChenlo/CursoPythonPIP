import csv
import charts
import pandas as pd

def main():

    # def read_csv(path):
    #     with open(path, "r") as cvsfile:
    #         reader = csv.reader(cvsfile, delimiter=",")
    #         header = next(reader)
    #         for row in reader:
    #             pair = zip(header, row)
    #             if "Argentina" in row:
    #                 dict_country = {key : value for key, value in pair}
    #         # print(dict_country)
    #         ages = ["1970", "1980", "1990", "2000", "2010", "2015", "2020","2022" ]
    #         population = {}
    #         for age in ages:
    #             population.update({f"{age} Population": dict_country[f"{age} Population"]})
    #         return population

    # population = read_csv("./data.csv")
    # charts.generate_bar_chart(population.keys(), population.values())
    # charts.generate_pie_chart(population.keys(), population.values())

    df = pd.read_csv("data.csv")
    df = df[df["Continent"] == "Africa"]

    countries = df["Country/Territory"].values
    porcentages = df["World Population Percentage"].values
    charts.generate_bar_chart(countries, porcentages)
    charts.generate_pie_chart(countries, porcentages)


if __name__ == "__main__":
    main()
