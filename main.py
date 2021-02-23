import datetime

class BikeRental:
    def __init__(self,stock=0):
        self.stock = stock
        #Our constructor class that instantiates bike rental shop

    def display_stock(self):
        print(f"We have currently {self.stock} bikes available for rent.")
        return self.stock

    def rent_hourly_basis(self,n):
        if n <= 0:
            print("Number of bikes should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry we currently have {self.stock} bikes to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented{n} bikes on hourly basis today at {now}. ")
            print(f"You will be charged $5 per hour for each bike.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def rent_daily_basis(self,n):

        if n <= 0:
            print("Number of bikes should be positive")
            return None

        elif n > self.stock:
            print(f"Sorry we currently have {self.stock} bikes to rent.")
            return None
        else:
            now = datetime.datetime.now
            print(f"You have rented {n} bikes on daily basis at {now}.")
            print("You will be charged $20 per day for each bike.")
            print("We hope that you enjoy our service")

            self.stock -= n
            return now

    def rent_weekly_basis(self,n):

        if n <= 0:
            print("Number of bikes should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry we currently have {self.stock} bikes available for rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n}bikes on weekly basis on {now}.")
            print("You will be charged $100 per week for each bike.")
            print("We hope you enjoy our service.")

            self.stock -= n
            return now











