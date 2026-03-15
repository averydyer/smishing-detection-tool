# Smishing Detection Tool

A Python-driven tool which analyzes text messages to
determine whether they have a chance of being smishing
attempts. Multiple aspects of the message are reviewed 
such as dangerous keywords and suspicious links, which
are each given a point value that is added to the overall
risk score. The final risk score is on a scale of 0-100,
with 0 being a completely safe message and 100 being an
extremely dangerous/obvious smishing attempt

## Project Structure Overview

#### data/examples.json
Stores sample SMS messages that the detection system analyzes. Current number of messages: 20

#### engine/analyzer.py
The logic that decides whether a message is suspicious

#### cli.py
Command line interface - how the user interacts with the program