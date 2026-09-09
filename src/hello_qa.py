import sys

def greet(name):
    return f"Привет, {name}! Твой первый автотест скоро будет написан."

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "QA-инженер"
    print(greet(name))
