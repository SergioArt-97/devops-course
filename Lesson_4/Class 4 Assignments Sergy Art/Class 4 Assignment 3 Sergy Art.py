import requests


url = "http://universities.hipolabs.com/search?country=Israel"
response = requests.get(url)

university_names = []

if response.status_code == 200:
    responses = response.json()
    for response in responses:
        university_names.append(response['name'])
    if len(university_names) >= 5:
        print(f"There are {len(university_names)} universities in israel")
    else:
        print("There are less than 5 universities in Israel")
else:
    print("Failed to fetch israel universities. Status code:", response.status_code)