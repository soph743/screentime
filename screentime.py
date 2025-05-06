import matplotlib.pyplot as plt

def main():
    print("enter your daily average screen time")
    current_avg = float(input())
    print("enter your goal screen time")
    goal_avg = float(input())
    print("enter the days until you reach your goal screen time")
    days = int(input())

    x_values = []
    y_values = []

    a = -(goal_avg/(days**2)) + (current_avg/(days**2))

    for i in range(days):
        if i == 0:
            x_values.append(0)
            y_values.append(current_avg)
        x_values.append(i)
        y_values.append(-a*(i**2) + current_avg)


    print("screentime reduction schedule: ")
    for i in range(1, len(x_values)):
        result = '{0:02.0f}:{1:02.0f}'.format(*divmod(y_values[i] * 60, 60))
        print("day " + str(i-1) + " allotted screen time: ")
        print(result)
    print("day " + str(days) + ": ")
    print(str(goal_avg))

    plt.plot(x_values, y_values)

    plt.xlabel("screen time (hours)")
    plt.ylabel("daily screen time")
    plt.title("Screen Time Reduction Plan")

    plt.show()

if __name__ == '__main__':
    main()
