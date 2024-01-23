import requests

api_url = "https://jsonplaceholder.typicode.com/todos"

try:
    # fetch data

    response = requests.get(api_url)
    todos = response.json()

    # extracting data 'qui'
    titles = [todo['title'] for todo in todos if 'qui' in todo['title'].lower()]

    # display titles

    for title in titles:
        print(f"Titles: {str(title)}")

    # checking title with type int
    if any(isinstance(title, int) for title in titles):
        print("There is a title with type int.")
    else:
        print("There is no title with a type int.")

except requests.exceptions.RequestException as error:
    print("Error fetching todos", error)