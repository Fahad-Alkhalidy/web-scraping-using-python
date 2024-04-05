import requests
from bs4 import BeautifulSoup
import csv

country = input("Please enter your counter with small letters: ")
page = requests.get("https://www.timeanddate.com/weather/{country}")
countries_details = []

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    countryWeather = soup.findAll("tbody")
    def get_Country_Info(countryWeather):
        countryName = countryWeather.contents[0].contents[1].text
        countryHighTempRegion = countryWeather.contents[1].contents[1].text
        countryLowTempRegion = countryWeather.contents[2].contents[1].text
        maxWind = countryWeather.contents[3].contents[1].text
        countryInMap = soup.find("div", {'id': "bk-map"}).contents[0]
        countries_details.append({"Country":countryName,"Highest Temp":countryHighTempRegion,"Lowest Temp":countryLowTempRegion,"Max Wind":maxWind, "Country Location": countryInMap})

    get_Country_Info(countryWeather[0])
    keys = countries_details[0].keys()
    get_Country_Info(countryWeather[0])

    with open("C:\\Users\\fahad\\Desktop\\CountriesWeather\\weather_details.csv", 'w') as output_Weather_File:
        dict_writer = csv.DictWriter(output_Weather_File, keys)
        dict_writer.writeheader()
        dict_writer.writerows(countries_details)

main(page)
