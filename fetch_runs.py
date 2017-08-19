#!/usr/bin/env python2.7

import sqlite3
import config
from endomondo import MobileApi


# Only required the first time.
# endomondo = MobileApi(email='', password='')
# auth_token = endomondo.get_auth_token()
# print (auth_token)


auth_token = config.endomondo_key
endomondo = MobileApi(auth_token=auth_token)
connection = sqlite3.connect(config.db_path)

for workout in endomondo.get_workouts(maxResults=2):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Runs WHERE id = ?", [str(workout.id)])
    exists = cursor.fetchone()[0]

    if workout.sport == 0 and not workout.live and exists < 1:
        # eligible run found, put in queue
        connection.execute(
            "INSERT INTO Runs (id, date, distance, processed) values (?, ?, "
            "?, ?)",
            (workout.id, workout.start_time, round(workout.distance, 2), 0))

connection.commit()
connection.close()
