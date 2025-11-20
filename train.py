import csv


def estimated_price(mileage, theta0, theta1):
	""""""
	return theta0 + theta1 * mileage


def train(path: str, learning_rate=5e-12, iterations=10000):
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

	for _ in range(iterations):
		sum_error_theta0 = 0.0
		sum_error_theta1 = 0.0

		for i in range(m):
			pred = estimated_price(x[i], theta0, theta1)
			error = pred - y[i]

			sum_error_theta0 += error
			sum_error_theta1 += error * x[i]

		tmp0 = theta0 - learning_rate * (1 / m) * sum_error_theta0
		tmp1 = theta1 - learning_rate * (1 / m) * sum_error_theta1

		theta0 = tmp0
		theta1 = tmp1
	
	with open("theta.csv", "w") as f:
		f.write(f"{theta0},{theta1}")
	
	print("TRAINING DONE")
	print(f"Theta0 = {theta0}")
	print(f"Theta1 = {theta1}")


def main():
	""""""
	try:
		train("data.csv")
	except Exception as e:
		print(f"An error as occured : {e}")


if __name__ == "__main__":
	main()