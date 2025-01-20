users = [
    {"name": "Alice", "age": 25, "job": "Engineer"},
    {"name": "Bob", "age": 30, "job": "Designer"},
    {"name": "Charlie", "age": 22, "job": "Developer"},
    {"name": "Diana", "age": 28, "job": "Teacher"},
    {"name": "Edward", "age": 35, "job": "Manager"},
    {"name": "Fiona", "age": 27, "job": "Data Analyst"},
    {"name": "George", "age": 29, "job": "Marketing Specialist"},
    {"name": "Hannah", "age": 26, "job": "Researcher"},
    {"name": "Ian", "age": 31, "job": "Accountant"},
    {"name": "Julia", "age": 24, "job": "HR Specialist"}
]

def lambda_func(user):
    return user['age'] > 27 and user['age'] < 30

# adults = filter(lambda user: user['age'] > 27 and user['age'] < 30, users)
adults = filter(lambda_func, users)
print(list(adults))

