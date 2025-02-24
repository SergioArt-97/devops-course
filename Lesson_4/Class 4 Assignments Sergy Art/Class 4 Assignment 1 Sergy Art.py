import requests
url = "https://api.github.com/users/avielb/repos"
response = requests.get(url)
if response.status_code == 200:
    repositories = response.json()
    repo_names = []
    for repo in repositories:
        repo_names.append(repo['name'])
    assert len(repo_names) > 5, "There are less than 5 repos in the Github"
    print("These are the repos in the Github:")
    for i, name in enumerate(repo_names):
        if i == len(repo_names) - 1:
            print(name)
        else:
            print(name, end=", ")
    print(f"there are {len(repo_names)} repos in this github")
else:
    print("Failed to fetch repositories. Status code:", response.status_code)