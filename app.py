from flask import Flask, request, redirect, render_template
import string
import random
from database import init_db, insert_url, get_long_url

app = Flask(__name__)

init_db()

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = generate_short_url()
        insert_url(long_url, short_url)
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    return 'URL not found', 404
