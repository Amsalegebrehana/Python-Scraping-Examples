# scraping programing languages from github

import requests

def get_repos(language):

    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc'

    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        # print(data)
        print("###########################")
        for repo in data.get('items',[]):
            print(f"Repository: {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"URL: {repo['html_url']}")
            print("\n---\n")
    else:
        print(f"Failed to retrieve GitHub data. Status code: {res.status_code}")


print(get_repos('python'))