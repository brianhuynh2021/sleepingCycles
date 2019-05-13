import datetime

currentDT = datetime.datetime.now()
print('Now is: '+ str(currentDT))

def convertCircleToHours(circles):
    return (circles*90)/60 # a circle of sleeping is 90 minutes

try:
    circles = int(input('Please enter your circles: \n'))
except ValueError:
    print('This is not a whole circle')

n_hours = convertCircleToHours(circles)
print('You need to take ' + str(n_hours) + ' hours\n')
date = currentDT + datetime.timedelta(hours = n_hours)

print('You need to wake up at: ' + str(date))
# Here I want to current time plus with total hours I need to sleep
#example now is 0 hours, I want to sleep 2 circles = 180 mins = 3 hours - the restult will say: you need to
# wake up at 4.00 o'clock
