#!/usr/bin/env python3
import requests
import random
import sys
import os

def get_dadjoke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    if response.ok:
        return response.json().get("joke", "No joke found.")
    return "Failed to fetch Dad Joke."

def get_official_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
    if response.ok:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0].get("setup", "") + " " + data[0].get("punchline", "")
    return "Failed to fetch Official Joke."

def get_chuck_norris():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.ok:
        return response.json().get("value", "No joke found.")
    return "Failed to fetch Chuck Norris joke."

def get_jokeapi():
    response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
    if response.ok:
        return response.json().get("joke", "No joke found.")
    return "Failed to fetch JokeAPI joke."

def get_local_joke():
    local_file = os.path.join(os.path.dirname(__file__), "punput.txt")
    if not os.path.isfile(local_file):
        return "punput.txt not found."
    with open(local_file, "r", encoding="utf-8") as f:
        jokes = [line.strip() for line in f if line.strip()]
        return random.choice(jokes) if jokes else "No jokes in punput.txt."

# Map command-line argument to function
sources = {
    "icanhazdadjoke": get_dadjoke,
    "officialjoke": get_official_joke,
    "norris": get_chuck_norris,
    "jokeapi": get_jokeapi,
    "local": get_local_joke
}

# Get argument from command line or use default
source_key = sys.argv[1].lower() if len(sys.argv) > 1 else "icanhazdadjoke"
joke_func = sources.get(source_key, get_dadjoke)

try:
    print(joke_func())
except Exception as e:
    print(f"[ERROR] Could not fetch joke: {e}")
