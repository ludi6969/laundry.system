from machines import Dryer, Washer


class Laundry:
    def __init__(self, n_washers, n_dryers):
        self.washers = []
        self.dryers = []

        for id_number in range(1, n_dryers + 1):
            self.dryers.append(Dryer(id_number))

        for id_number in range(1, n_washers + 1):
            self.washers.append(Washer(id_number))

        self.all_machines = self.washers + self.dryers

    def list_free(self):
        print('Free machines:')
        for machine in self.all_machines:
            if machine.available() is True:
                print('* ' + machine.display_name)

    def list_all(self):
        print('All machines:')
        for machine in self.all_machines:
            print('* ' + machine.state())

    def find_next_free(self):
        best_washer = None
        best_dryer = None
        for machine in self.all_machines:
            if machine.type == '🧺':
                if (
                        best_washer is None or
                        (machine.available() is True and best_washer.available() is not True) or
                        (machine.minutes_to_end() < best_washer.minutes_to_end())
                ):
                    best_washer = machine

            elif machine.type == '🔥':
                if (
                        best_dryer is None or
                        (machine.available() is True and best_dryer.available() is not True) or
                        (machine.minutes_to_end() < best_dryer.minutes_to_end())
                ):
                    best_dryer = machine

        print('Next available machines:')
        print('* ' + best_washer.state())
        print('* ' + best_dryer.state())

    def get_machine(self, type, id_number):
        for machine in self.all_machines:
            if machine.type == type and machine.id_number == id_number:
                return machine
        raise Exception('Machine not found :c')