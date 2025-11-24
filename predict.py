import csv


def main():
    """"""
    try:
        with open("theta.csv", "r") as f:
            data = csv.reader(f)
            for row in data:
                theta0 = float(row[0])
                theta1 = float(row[1])
    except FileNotFoundError:
        theta0 = 0.0
        theta1 = 0.0
    except Exception as e:
        print(f"An error as occured : {e}")
        return
    try:
        if (not theta0 and not theta1):
            raise ValueError("Model is not trained yet. Please train the model"
                             " before making predictions.")
        mileage = float(input("Enter the mileage of the car: "))
        if mileage < 0:
            raise ValueError("Mileage cannot be negative.")
        estiamed_price = theta0 + theta1 * mileage
        if estiamed_price < 0:
            estiamed_price = 0.0
        print(f"The estimated price for a car with {mileage} "
              f"mileage is: {estiamed_price}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    main()
