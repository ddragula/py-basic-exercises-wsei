import requests
import threading


def fetch_universities(country, result_dict, errors_dict):
    try:
        url = f"http://universities.hipolabs.com/search?country={country}"
        response = requests.get(url)
        if response.status_code in range(200, 299):
            data = response.json()
            universities = [university["name"] for university in data]
            result_dict[country] = universities
        else:
            errors_dict[country] = response.status_code
    except Exception as e:
        errors_dict[country] = f"Error: {e}"


countries = [
    "Poland", "Andorra", "San Marino", "Liechtenstein", "Monaco",
    "Malta", "Luxembourg", "Iceland", "Montenegro", "Kosovo",
    "Slovenia", "Estonia", "Latvia", "Lithuania", "Cyprus",
    "Moldova", "Georgia", "Armenia", "Albania", "North Macedonia"
]
results = {}
errors = {}

threads = []

for country in countries:
    thread = threading.Thread(
        target=fetch_universities,
        args=(country, results, errors)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for country, universities in results.items():
    print(f"{country}: {universities}")
