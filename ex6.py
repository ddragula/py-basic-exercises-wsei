import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

url = 'https://danepubliczne.imgw.pl/api/data/meteo/format/xml'

response = requests.get(url)
response.raise_for_status()

tree = ET.fromstring(response.text)

stations = {}
for station in tree.findall('item'):
    name = station.find('nazwa_stacji').text

    try:
        wind_speed = float(station.find('wiatr_srednia_predkosc').text)
    except TypeError:
        continue

    stations[name] = wind_speed


plt.figure(figsize=(12, 6))
plt.bar(stations.keys(), stations.values(), color='blue')
plt.xlabel('Stacja')
plt.ylabel('Średnia prędkość wiatru (m/s)')
plt.title('Średnia prędkość wiatru na stacjach pogodowych')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
