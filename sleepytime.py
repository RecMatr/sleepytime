# SleepyTime :: Sleep Cycle Calculator :: Time Your Sleep

from datetime import datetime, timedelta
import sys

print('\nSleepyTime :: What time should you go to bed?')
print('-' * 45)


class SleepyTime:

    def __init__(self):
        """
        Inspired by sleepyti.me
        example: python sleepytime.py 8:00 AM
        or run sleepytime.py and set the time
        http://github.com/recmatr
        """
        if len(sys.argv) < 2:
            self.timeInput = input(
                'What time do you need to wake up? (ex: 9:00 AM): ')
        else:
            self.timeInput = (' '.join(sys.argv[1:3]))
        try:
            self.timeToWake = datetime.strptime(self.timeInput, '%H:%M %p')
            if 'pm' in self.timeInput.lower():
                self.timeToWake = self.timeToWake + timedelta(hours=12)
        except:
            print('Error:\n' +
                  'Please input a bedtime in the proper format (ex: 10:00 AM)')
            sys.exit()
        print('Optimal times to close your eyes:')
        print('-' * 45)
        self.firstTime = self.timeToWake - timedelta(hours=7.5, minutes=14)
        self.secondTime = self.timeToWake - timedelta(hours=6, minutes=14)
        self.thirdTime = self.timeToWake - timedelta(hours=4.5, minutes=14)
        self.fourthTime = self.timeToWake - timedelta(hours=3, minutes=14)
        self.firstTime = datetime.strftime(self.firstTime, '%I:%M %p')
        self.secondTime = datetime.strftime(self.secondTime, '%I:%M %p')
        self.thirdTime = datetime.strftime(self.thirdTime, '%I:%M %p')
        self.fourthTime = datetime.strftime(self.fourthTime, '%I:%M %p')
        print('{} :: {} :: {} :: {}'.format(
            self.firstTime,
            self.secondTime,
            self.thirdTime,
            self.fourthTime))
SleepyTime()
