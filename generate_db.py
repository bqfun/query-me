import sqlite3

from faker import Faker


def generate_example_db():
    Faker.seed(20200905)
    fake = Faker("ja_JP")
    profiles = (fake.profile() for _ in range(1000))

    with sqlite3.connect("example.db") as con:
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, birthdate TEXT, sex TEXT)"
        )

        cur.executemany(
            "INSERT INTO users(name, birthdate, sex) VALUES (?, ?, ?)",
            ((p['name'], p['birthdate'], p['sex']) for p in profiles),
        )


if __name__ == "__main__":
    generate_example_db()
