# Protext



## Project Structure Overview

data/examples.json
stores sample SMS messages that the detection system analyzes.
current number of messages: 20 personal messages

engine/analyzer.py
the logic that decides whether a message is suspicious

engine/__pycache__/
created automatically by Python to store compiled versions of the code. Speeds up program startup

cli.py
command line interface. how a user interacts with the program