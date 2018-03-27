from datetime import datetime, timedelta

import sqlite3


def persist_bitcoin_price(price):
    with sqlite3.connect("bitcoint.db") as connection:
        cursor = connection.cursor()
        table_sql = "CREATE TABLE IF NOT EXISTS bitcoin_price(date TEXT, price REAL, currency TEXT)"
        cursor.execute(table_sql)
        cursor.execute("INSERT INTO bitcoin_price VALUES(datetime('now', 'localtime'), {}, 'eur')".format(price))

def get_bitcoin_price_history():
    with sqlite3.connect("bitcoint.db") as connection:
        cursor = connection.cursor()
        select_sql = "SELECT * FROM bitcoin_price LIMIT 10"
        import ipdb
        ipdb.set_trace()
        result = cursor.execute(select_sql)
        return result.fetchall()

def get_last_five_minutes_price():
    now = datetime.now()
    five_minutes_delta = timedelta(minutes=5)
    past_time = now - five_minutes_delta
    with sqlite3.connect("bitcoint.db") as connection:
        sql = "SELECT * FROM bitcoin_price WHERE date >= '{}' AND date <= '{}' LIMIT 1".format(past_time, now)
        cursor = connection.cursor()
        result = cursor.execute(sql)
        res =  result.fetchone()
        if res:
            return res[1]
        return None

