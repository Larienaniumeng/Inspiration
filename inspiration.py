
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def random_quotes():
    with open('inspiration.txt', 'r', encoding='utf-8') as fp:
        lines = fp.read().split('\n')
    quote = random.choice(lines)
    return quote
