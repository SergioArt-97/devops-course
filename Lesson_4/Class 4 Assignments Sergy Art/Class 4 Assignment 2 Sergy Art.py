import random
import requests

url = "https://api.agify.io/?name="
first_names = [
    'Christopher', 'Charles', 'Matthew',
    'Anthony', 'Donald', 'Andrew',
    "Alice", "Bob", "Charlie",
    "David", "Emma", "Fiona",
    "George", "Hannah", "Isaac",
    "Jack", "Katie", "Liam",
    "Mia", "Noah", "Olivia",
    "Paul", "Quinn", "Rachel"
                ]

people = random.sample(first_names, k = 3)

responses  = []

for person in people:
    responses.append((requests.get(url + person)))

for response in responses:
    if response.status_code == 200:
        response = response.json()
        assert response['age'] >= 0, "That is too young" if response['age'] < 120 else "That is too old"
        print(response['name'], response['age'])
    else:
        print(f"bad response, status code: {response.status_code}")
print("All ages are good")