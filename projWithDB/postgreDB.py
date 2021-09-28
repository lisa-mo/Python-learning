import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='pass123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='pass123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES ("f"'{item}',"f"'{quantity}',"f"'{price}')")
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='pass123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='pass123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item="f"'{item}'")
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='pass123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity="f"'{quantity}', price="f"'{price}' WHERE item="f"'{item}'")
    conn.commit()
    conn.close()


create_table()
insert("Scotch Glass", 1, 500)
insert("Bees", 1, 500)
update(11, 6, "Scotch Glass")
insert("Water Glass", 10, 5)
insert("Wine Glass", 50, 10)
insert("Jin Glass", 50, 10)
delete("Bees")
print(view())
