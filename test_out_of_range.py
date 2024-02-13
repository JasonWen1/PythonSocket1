import random
from client1 import start_client  

#There are 10 test cases, each with a random name and number
def generate_random_name():
    first_names = ["John", "Jane", "Sam", "Alice", "Bob", "Diana", "Mike", "Carol", "Steve", "Laura"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Taylor"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def run_client():
    client_name = generate_random_name()
    client_number = 0 - random.randint(1, 100)
    start_client(client_name, str(client_number))

def main():
    run_client()

if __name__ == '__main__':
    main()