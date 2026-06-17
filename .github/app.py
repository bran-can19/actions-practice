import os

print("Hello, World!")

for i in (1, 2, 3, 4, 5):
    print("Xd")

def main():
    username = os.getenv("USER", "Invitado")
    print(f"Hello, {username}!")

if __name__ == "__main__":
    main()