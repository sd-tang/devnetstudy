x = 0
while True:

    try:
        filename = input("Which file would you like to read?:")
        with open(filename, "r") as f:
            data = f.read()

    except FileNotFoundError:
        print(f"Sorry, the filename {filename} doesn't exist, please try again.")

    else:
        print(data)
        x = 0
        break

    finally:
        x += 1
        if x == 3:
            print("Unsuccessful attempts exceeded. \nFind out the correct name and run again")
            break