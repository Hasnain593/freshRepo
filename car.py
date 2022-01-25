command = ""
started = False
stopped = False

while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already Started")
        else:
            print("Car Started")
            started = True
    elif command == "stop":
        if stopped:
            print("Car is already Stopped")            
        else:
            print("Car Stopped")
            stopped = True
    elif command=="help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I do'nt Understand 101")



