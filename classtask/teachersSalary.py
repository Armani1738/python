teachername = input("Enter the teacher name: ")
period = int(input("Enter number of period: "))
rate_per_period = int(input("Enter the rate per period: "))
def teacher_salary(username):
    username = ""
    monthly_rate = 20
    overtime = 25
    number_of_period = ""
    for name in username:
        if number_of_period > 100:
            number_of_period = number_of_period * overtime + monthly_rate
            print(number_of_period)
        else:
            number_of_period  < 100
            number_of_period = number_of_period * 20
            print(number_of_period)

