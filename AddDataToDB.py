import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://attendance-system-5a6cb-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')                  # creates 'Students' directory to put data in

data = {
    "08245":
        {
            "name": 'Kobe Bryant',
            "major": 'Sports Management',
            "starting_year": 1996,
            "total_attendance": 24,
            "standing": 'G',
            "year": 8,
            "last_attendance_time": "2023-6-6 00:54:34"
        },

    "032604":
        {
            "name": 'big dawg',
            "major": 'comp sci',
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": 'G',
            "year": 12,
            "last_attendance_time": "2023-6-6 00:54:34"
        },
    "61042":
        {
            "name": 'Elon Musk',
            "major": 'Business Management',
            "starting_year": 2000,
            "total_attendance": 30,
            "standing": 'G',
            "year": 12,
            "last_attendance_time": "2023-6-6 00:54:34"
        },

    "72017":
        {
            "name": 'Ryan Higa',
            "major": 'Communications',
            "starting_year": 2005,
            "total_attendance": 2,
            "standing": 'B',
            "year": 2,
            "last_attendance_time": "2023-6-6 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)                       # sends data
