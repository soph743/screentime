import sys


def main():
    print('input your average daily screen time (rounded to nearest hour)')
    daily_avg = sys.stdin.readline()
    print('inputted value: ' + daily_avg)
    print('what is your goal screen time?')
    goal = sys.stdin.readline()
    print('inputted value: ' + goal)
    print('generating plan to decrease screentime by ', end="")
    print(float(daily_avg) - float(goal), end=""),
    print(' hours...')
    print(reductionPlan(float(daily_avg), float(goal)))


def reductionPlan(daily_avg, goal):

    if daily_avg <= 2:
        duration = 7
    elif 4 >= daily_avg > 2:
        duration = 14
    elif 8 >= daily_avg > 4:
        duration = 21
    elif 12 >= daily_avg > 8:
        duration = 28
    elif 16 >= daily_avg > 12:
        duration = 35
    elif 20 >= daily_avg > 16:
        duration = 42
    elif 24 >= daily_avg > 16:
        duration = 49
    else:
        return ('please input daily average as an integer or float between 0 and 24, and goal that is smaller than '
                'daily average')

    plan = []

    daily_reduction = (daily_avg - goal) / (duration - 1)

    for day in range(1, duration + 1):
        if day == duration:
            daily_avg = goal

        else:
            daily_avg = daily_avg - daily_reduction

        final = '{0:02.0f}:{1:02.0f}'.format(*divmod(round(daily_avg, 2) * 60, 60))
        plan.append(final)

    return plan


if __name__ == "__main__":
    main()







