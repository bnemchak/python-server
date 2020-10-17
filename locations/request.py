import sqlite3
import json

from models import Location

locations = [
     Location(1, 'North Nashville', '8422 Johnson Pike'),
     Location(2, 'Nashville South', '209 Emory Dr'),
]


def get_all_locations():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)

        locations = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    return json.dumps(locations)


# Function with a single parameter
def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, ( id ))

        data = db_cursor.fetchone()

        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)

def create_location(location):
    max_id = locations[-1].id

    new_id = max_id + 1

    location["id"] = new_id

    locations.append(location)

    return location

def delete_location(id):
    location_index = -1

    for index, location in enumerate(locations):
        if location.id == id:
            location_index = index

    if location_index >= 0:
        locations.pop(location_index)

def update_location(id, new_location):
    for index, location in enumerate(locations):
        if location.id == id:
            locations[index] = new_location
            break
