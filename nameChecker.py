while True:
    try:
        name = input("Write your name here: ")
        if len(name)>=9:
            print("Name is good")
        else:
            print("Name must be atlest 12 characters long")
    except Exception as e:
        print("Sorry unable to do it")