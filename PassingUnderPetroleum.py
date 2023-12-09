while True:
    lapsRun = float(input("Laps run: "))
    galStart = float(input("Gallons start: "))
    galRem = float(input("Gallons remaining: "))

    galUsed = galStart - galRem
    lapGal = round((lapsRun / galUsed), 1)
    lapTank = round((lapGal * galStart), 1)

    print("Laps per gallon: ", lapGal)
    print("Laps per Tank: ", lapTank)

    user_input = input("Continue? y/n: ").strip().lower()

    if user_input != 'y':
        print("Exiting...")
        break  # Exit the loop
