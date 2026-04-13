import requests

def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Joke:", data["value"])
    else:
        print("Error fetching joke")

if __name__=="__main__":
    get_joke()