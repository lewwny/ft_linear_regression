import csv


def precision(x: list, y: list, theta0: float, theta1: float) -> float:
    """calculate the precision of the model using R-squared metric"""
    mean_y = sum(y) / len(y)
    ss_tot = sum((yi - mean_y) ** 2 for yi in y)
    estimations = [theta0 + theta1 * xi for xi in x]
    ss_res = sum((yi - esti) ** 2 for yi, esti in zip(y, estimations))
    r_squared = 1 - (ss_res / ss_tot)
    return r_squared


def main():
    """main function"""
    try:
        with open("theta.csv", "r") as f:
            theta = csv.reader(f)
            for row in theta:
                theta0 = float(row[0])
                theta1 = float(row[1])
    except FileNotFoundError:
        print("Model is not trained yet. Please train the model before "
              "calculating precision.")
        return
    except Exception as e:
        print(f"An error as occured : {e}")
        return
    x = []
    y = []
    try:
        with open("data.csv", "r") as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                mileage = float(row[0])
                price = float(row[1])
                x.append(mileage)
                y.append(price)
    except FileNotFoundError:
        print("Data file not found. Please ensure 'data.csv' is present.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    try:
        precision_value = precision(x, y, theta0, theta1)
        print(f"\033[1;32mPrecision of the model"
              f": {precision_value:.2f}%\033[0m")
        print("Precision < 0 means that the model is worse "
              "than a horizontal line.")
        print("Precision = 1 means that the model perfectly fits the data.")
    except Exception as e:
        print(f"An error occurred while calculating precision: {e}")
        return


if __name__ == "__main__":
    main()
