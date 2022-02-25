person = {
    "firstName": "umer",
    "age": 21,
    "course": "computer science"
}

course = {
    "name": "computer science",
    "current_subject": "dsa",
    "favorite_subject": "web_development"
}

for (key, value) in person.items():
    print(f"{key}: {value}")

for key in course:
    print(f"{key}: {course[key]}")
