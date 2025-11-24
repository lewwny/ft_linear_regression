import csv
import matplotlib.pyplot as plt


def estimated_price(mileage, theta0, theta1):
    """"""
    return theta0 + theta1 * mileage


def train(path: str, learning_rate=0.1, iterations=10000000):
    """"""
    x = []
    y = []

    with open(path, "r") as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            x.append(float(row[0]))
            y.append(float(row[1]))

    m = len(x)
    theta0 = 0.0
    theta1 = 0.0
    x_norm = [(i - min(x)) / (max(x) - min(x)) for i in x]

    for _ in range(iterations):
        sum_error_theta0 = 0.0
        sum_error_theta1 = 0.0

        for i in range(m):
            pred = estimated_price(x_norm[i], theta0, theta1)
            error = pred - y[i]

            sum_error_theta0 += error
            sum_error_theta1 += error * x_norm[i]

        tmp0 = theta0 - learning_rate * (1 / m) * sum_error_theta0
        tmp1 = theta1 - learning_rate * (1 / m) * sum_error_theta1

        theta0 = tmp0
        theta1 = tmp1
    delta = max(x) - min(x)
    theta1real = theta1 / delta
    theta0real = theta0 - (theta1real * min(x))

    with open("theta.csv", "w") as f:
        f.write(f"{theta0real},{theta1real}")

    print("TRAINING DONE")
    print(f"Theta0 = {theta0real}")
    print(f"Theta1 = {theta1real}")
    # Plotting the data and the regression line
    line = [estimated_price(i, theta0real, theta1real) for i in x]
    plt.plot(x, line, color='red', label='Regression Line')
    plt.scatter(x, y)
    plt.title("Mileage vs Price")
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.xlim(20000, None)
    plt.show()


def main():
    """"""
    try:
        train("data.csv")
    except Exception as e:
        print(f"An error as occured : {e}")


if __name__ == "__main__":
    main()
