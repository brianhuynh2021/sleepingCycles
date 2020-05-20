import datetime

#currentDT = datetime.datetime.now()
#print('Now is: '+ str(currentDT))


def convertCycleToHours(cycles):
    return (cycles*90)/60

def validatetime(expected_time):
    try:
        valid_time = datetime.datetime.strptime(expected_time,'%H %M')
        print(type(valid_time))
        return True
    except :
        print('Please input the correct timeformat %H %M')
        return False

def check_cycles():
    try:
        cycles = int(input('Please enter your circles: \n'))
        return cycles
    except ValueError:
        print('This is not a whole cycle')

def wake_up_now(cycles):
    n_hours = convertCycleToHours(cycles)
    wakeup_time_now = datetime.datetime.now() + datetime.timedelta(hours = n_hours)
    print('You need to take ' + str(n_hours) + ' hours for sleeping '+ 'and wake up at '+ str(wakeup_time_now))
    return wake_up_now

def wake_up_later(cycles, later_time):
    n_hours = convertCycleToHours(cycles)
    wakeup_time_later = datetime.datetime.strptime(later_time,'%H %M') + datetime.timedelta(hours = n_hours)
    print('You need to take ' + str(n_hours) + ' hours for sleeping '+ 'and wake up at '+ str(wakeup_time_later))
    return wake_up_later

print("Please type Y if you'd like to sleep now. Otherwise, type any key if you want to sleep later")
choice = input().lower()
if choice == "y":
    wake_up_now(check_cycles())
else:
    while True:
        t = input('What time would you like to go to bed?: ')
        if validatetime(t) == True:
            circles = check_cycles()
            wake_up_later(circles,t)
            break
            

# a cycle of sleeping is 90 minutes
# create a function
# Here I want to current time plus with total hours I need to sleep
# example now is 0 hours, I want to sleep 2 circles = 180 mins = 3 hours - the restult will say: you need to
# wake up at 4.00 o'clock