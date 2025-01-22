def menu() -> None:
    print("\nMenu:")
    print("\t1. Register User\n\t2. Filter users by age\n\t3. Filter users by job.\n\t4. Get all users")

def print_users(users: list[dict]) -> list[dict]:
    print("\nA List of Users:")
    for number, user in enumerate(users, start=1):
        print(f"{number}. {user['name']} is {user['age']} and {user['job']}.")

def add_user(users: list[dict]) -> list[dict]:
    print("Enter data for new user")
    name = input("Name: ")
    age = int(input("Age: "))
    job = input("Job: ")

    new_user = {
        "name": name,
        "age": age,
        "job": job,
    }
    users.append(new_user)
    return users

def get_users_by_age(users: list[dict], age: int) -> list[dict]:
    return list(filter(lambda user:user['age']==age,users))

def get_users_by_job(users: list[dict], job: str) -> list[dict]:
    return list(filter(lambda user:user['job']==job.lower(),users))

def main():
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

    while True:
        menu()

        choice = input("Enter Option: ")
        if choice == '1':
            users = add_user(users)
        elif choice == '2':
            age = int(input("Enter min age: "))
            filtered_users = get_users_by_age(users, age)
            print(filtered_users)
        elif choice == '3':
            job = str(input("Enter job: "))
            filtered_users = get_users_by_job(users, job)
            print(filtered_users)
        elif choice == '4':
            print_users(users)
        else:
            print("Invalid choice.")

main()

