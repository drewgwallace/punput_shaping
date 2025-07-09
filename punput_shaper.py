#!/usr/bin/env python3
import requests

# Dad jokes API (active)
response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
# Official Joke API (programming/general)
# response = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
# Chuck Norris API
# response = requests.get("https://api.chucknorris.io/jokes/random")
# JokeAPI (programming jokes)
# response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")

if response.status_code == 200:
    data = response.json()
    # Parsing based on active API:
    # Dad jokes:
    if "joke" in data:
        joke = data["joke"]
    # Official Joke API returns a list
    elif isinstance(data, list) and len(data) > 0 and "setup" in data[0]:
        joke = data[0]["setup"] + " " + data[0]["punchline"]
    # Chuck Norris API
    elif "value" in data:
        joke = data["value"]
    # JokeAPI
    elif "joke" in data:
        joke = data["joke"]
    else:
        joke = "No joke found."
else:
    joke = "Failed to fetch joke."

print(joke)