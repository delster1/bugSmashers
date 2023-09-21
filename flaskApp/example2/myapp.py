from flask import Flask, render_template
import json
import random

app = Flask(__name__)


quotes = json.load(open('quotes.json'))

quotesList = quotes["quotes"]

def getQuotes():
    return quotesList


@app.route('/')
def hp():
    quotesList = getQuotes()
    
    title = 'd3 server'
    quotes = quotesList
    oneQuote = random.choice(quotesList)
    
    return render_template('temp.html', title=title,quotes=quotesList,oneQuote=oneQuote)
    
@app.route('/quotes')
def quotes():
    quotesList = getQuotes()

    title = 'list of quotes'

    return render_template('quotes.html', title=title, quotes=quotesList)

if __name__ == '__main__':
    app.run(debug=True)
