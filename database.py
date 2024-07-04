import sqlite3

def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT NOT NULL,
            short_url TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def insert_url(long_url, short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('INSERT INTO urls (long_url, short_url) VALUES (?, ?)', (long_url, short_url))
    conn.commit()
    conn.close()

def get_long_url(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT long_url FROM urls WHERE short_url = ?', (short_url,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None
