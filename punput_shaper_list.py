#!/usr/bin/env python3
import random
import os

# Get the full path to the punput.txt file located in the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "punput.txt")

# Read all non-empty lines from the file
with open(file_path, 'r', encoding='utf-8') as f:
    jokes = [line.strip() for line in f if line.strip()]

# Pick and print a random joke
print(random.choice(jokes))
