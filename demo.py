# import psycopg2

# conn = psycopg2.connect(dbname="dvrental", user="postgres", password="Cartelo009")
# cur = conn.cursor()

# cur.execute("SELECT title FROM film;")
# cur.fetchall()

def recurfact(x):
    '''return factorial n! of a number'''
    if x.__eq__(1):
        return 1
    return x*recurfact(x-1)

print(recurfact(1))

