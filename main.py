import psycopg2

#connect to postgree database

conn = psycopg2.connect(host="localhost",
                       port=5433,
                       database="book_db",
                       user="postgres",
                       password="admin123")


cur = conn.cursor()
print("Connected Successfully")

#create table
cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    year INT
);
""")

conn.commit()
print("Table created.")

#insert table
cur.execute("""
INSERT INTO books (title, author, year)
VALUES(%s, %s, %s)
""", ("The Alchemist", "Paulo Coelho", 1988))

conn.commit()
print("Book Inserted")

#Retrieve data(GET)
cur.execute("SELECT * FROM books")
rows = cur.fetchall()
for row in rows:
    print(row)
    
#update data
cur.execute("""
UPDATE books SET year = %s WHERE title = %s""", (1993, "The Alchemist"))

conn.commit()
print("Book Updated")

#delete data
cur.execute("DELETE FROM books WHERE title = %s", ("The Alchemist",))
conn.commit()
print("Book deleted.")

#close connection
cur.close()
conn.close()