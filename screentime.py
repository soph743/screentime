import matplotlib.pyplot as plt

class bcolors:
    HEADER = '\033[95m'
    YELLOW = '\033[33m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'

def main():
    national_avg = 5.26
    print("enter your daily average screen time")
    current_avg = float(input())

        if current_avg < national_avg:
        print(bcolors.GREEN + "your average is " + str(round(national_avg-current_avg, 2)) + " hours less than the national average" + bcolors.ENDC)
    elif current_avg > national_avg:
        print(bcolors.RED + "your average is " + str(round(current_avg-national_avg, 2)) + " hours greater than the national average" + bcolors.ENDC)
    else:
        print(bcolors.YELLOW + "your average is equal to the national average" + bcolors.ENDC)

    print(bcolors.BOLD + "enter your goal screen time" + bcolors.ENDC)
    goal_avg = float(input())
    print(bcolors.BOLD + "enter the days until you reach your goal screen time" + bcolors.ENDC)
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


    print(bcolors.UNDERLINE + bcolors.BOLD + "screentime reduction schedule: " + bcolors.ENDC)
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
