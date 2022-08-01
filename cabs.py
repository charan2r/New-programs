vehicles = [
    "car: Maximum no. of passengers - 3 and 4, A/C Non A/C",
    "van: Maximum no. of passengers - 6 and 8, A/C Non A/C",
    "3 wheeler: Maximum no. of passengers - 3",
    "truck: Size - 7ft and 12ft",
    "lorry: Max load - 2500kg and 3500kg"
]

print("""
        CAB SERVICE 

        Choose a task from below >>
                a - Add a vehicle
                b - Remove a vehicle
                c - See available vehicles
                d - Assign a hire
        
           Type end to finish.     
""")

name = input("Please enter your name: ")
while True:
    task = input("Please enter your preferred task? ")


    def addVehicle():
        if task == 'a':
            vehicle = input("What type of vehicle do you want to add? ")
            vehicles.append(vehicle)
            print(vehicle + " added ")
            print(vehicles)


    def removeVehicle():
        if task == 'b':
            vehicle = input("What type of vehicle do you want to remove? ")
            vehicles.remove(vehicle)
            print(vehicle + " removed ")
            print(vehicles)


    def seeVehicle():
        if task == 'c':
            print("Vehicle Details: ")
            print(vehicles)


    def assignHire():
        if task == 'd':
            vehicle2 = input("What type of vehicle do you want for the hire? ")
            if vehicle2 == 'car':
                p = input("No. of passengers? (3 or 4) ")
                q = input("Air condition? (yes/no) ")
                if q == 'yes':
                    fees = "Rs. 1000"
                else:
                    fees = "Rs. 800"
                print("""
                     Your Vehicle Assigned
                 """)
                print("Customer Name : " + name)
                print("Vehicle type : " + vehicle2)
                print("No. of passengers : " + p)
                print("Air condition : " + q)
                print("Total amount for the hire : " + fees)

            if vehicle2 == 'van':
                p = input("No. of passengers? (6 or 8) ")
                q = input("Air condition? (yes/no) ")
                if q == 'yes':
                    fees = "Rs. 2000"
                else:
                    fees = "Rs. 1500"
                print("""
                        Your Vehicle Assigned
                 """)
                print("Customer Name : " + name)
                print("Vehicle type : " + vehicle2)
                print("No. of passengers : " + p)
                print("Air condition : " + q)
                print("Total amount for the hire : " + fees)

            if vehicle2 == '3 wheel':
                p = input("No. of passengers? (Maximum 3) ")
                fees = "Rs. 500"
                print("""
                         Your Vehicle Assigned
                 """)
                print("Customer Name : " + name)
                print("Vehicle type : " + vehicle2)
                print("No. of passengers : " + p)
                print("Total amount for the hire : " + fees)

            if vehicle2 == 'truck':
                p = input("Please select the size? (7ft or 12ft) ")
                if p == '7ft':
                    fees = "Rs. 4500"
                else:
                    fees = "Rs. 5000"
                print("""
                          Your Vehicle Assigned
                 """)
                print("Customer Name : " + name)
                print("Vehicle type : " + vehicle2)
                print("Truck size : " + p)
                print("Total amount for the hire : " + fees)

            if vehicle2 == 'lorry':
                p = input("Please select the maximum load size? (2500kg or 3500kg) ")
                if p == '2500kg':
                    fees = "Rs. 9000"
                else:
                    fees = "Rs. 10000"
                print("""
                         Your Vehicle Assigned
                 """)
                print("Customer Name : " + name)
                print("Vehicle type : " + vehicle2)
                print("Lorry load size : " + p)
                print("Total amount for the hire : " + fees)

        print("""
                Thank You!
         """)

    addVehicle()
    removeVehicle()
    seeVehicle()
    assignHire()

    if task == 'end':
        break