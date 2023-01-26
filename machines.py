from datetime import datetime
import math


class Machine:
    type = None
    empty = True
    start_time = None
    cycle_duration = None

    def available(self):
        return self.minutes_to_end() == 0 and self.empty is True

    def __init__(self, id_number):
        self.id_number = id_number
        self.display_name = 'Machine ' + str(id_number)

    def start_cycle(self, minutes):
        if self.available() is False:
            print('This machine is already in use :c')
            return
        self.cycle_duration = minutes
        self.start_time = datetime.now()
        self.empty = False

    def take_out(self):
        if self.minutes_to_end() > 0:
            print('The cycle has not finished yet. Sorry!')
            return
        if self.empty is True:
            print('This machine is already empty.')
            return
        self.empty = True
        print('Thank you for taking your laundry out :>')

    def state(self):
        result = self.display_name
        if self.available() is True:
            result += ' is free!'
        elif self.minutes_to_end() > 0:
            postfix = "s" if self.minutes_to_end() > 1 else ""
            result += f" will finish in {str(self.minutes_to_end())} minute{postfix}."
        else:
            result += " finished the cycle but hasn't been unloaded :c"
        return result

    def minutes_to_end(self):
        if self.start_time is None:
            return 0
        now = datetime.now()
        elapsed = now - self.start_time
        elapsed_minutes = math.floor(elapsed.seconds / 60)
        remaining_minutes = self.cycle_duration - elapsed_minutes
        if remaining_minutes <= 0:
            self.start_time = None
            return 0
        return remaining_minutes


class Washer(Machine):
    def __init__(self, id_number):
        super().__init__(id_number)
        self.display_name = 'Washer ' + str(id_number)
        self.type = '🧺'


class Dryer(Machine):
    def __init__(self, id_number):
        super().__init__(id_number)
        self.display_name = 'Dryer ' + str(id_number)
        self.type = '🔥'

