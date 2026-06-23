import os

def main():
    print ("Hello World runs on Action!")

    for i in [1, 2, 3, 4, 5]:
        print ("XD " * i)

    
    name = os.getenv("USERNAME")
    print (f"Hello { name }")


if __name__ == "__main__":
    main()