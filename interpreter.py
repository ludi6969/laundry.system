from laundry import Laundry
from machines import Machine


class Interpreter:
    def __init__(self, laundry):
        self.laundry = laundry

    def run(self):
        print('Hello!')
        quit = False
        while quit is False:
            begin_colour = '\x1b[95m'
            end_colour = '\x1b[0m'
            print(f"{begin_colour}Please type in your command: {end_colour}", end="")
            command = input()
            if command == 'quit':
                handle_quit()
                quit = True
            elif command == 'start':
                handle_start(self.laundry)
            elif command == 'list':
                handle_list(self.laundry)
            elif command == 'free':
                handle_free(self.laundry)
            elif command == 'find':
                handle_find(self.laundry)
            elif command == 'out':
                handle_empty(self.laundry)
            elif command == 'help':
                handle_help()
            else:
                print(f"I don't understand '{command}'. Please try typing 'help'.")


def ask(question):
    print(question)
    return input()


def handle_quit():
    answer = ask('Are you satisfied with the Laundry System?')
    if answer == 'yes':
        print('Thank you!')
    elif answer == 'no':
        print('Sorry :c')
    print('Goodbye!')


def handle_start(laundry):
    machine_type = None
    machine = None
    cycle_time = None
    answer = ask('Do you want to wash (w) or dry (d) your clothes?')
    if answer == 'w':
        machine_type = '🧺'
    elif answer == 'd':
        machine_type = '🔥'
    else:
        print('Unrecognised action :c')
        return

    answer = ask('Please enter machine number.')
    try:
        machine_id = int(answer)
        machine = laundry.get_machine(machine_type, machine_id)
    except ValueError:
        print('Failed to parse number')
        return
    except Exception:
        print('Failed to find requested machine.')
        return

    answer = ask('How many minutes will the programme run for?')
    try:
        cycle_time = int(answer)
    except ValueError:
        print('Failed to parse number')
        return
    machine.start_cycle(cycle_time)


def handle_list(laundry):
    laundry.list_all()


def handle_free(laundry):
    laundry.list_free()


def handle_find(laundry):
    laundry.find_next_free()


def handle_empty(laundry):
    machine_type = None
    machine = None
    answer = ask('Do you want to empty washer(w) or dryer(d)?')
    if answer == 'w':
        machine_type = '🧺'
    elif answer == 'd':
        machine_type = '🔥'
    else:
        print('Unrecognised action :c')
        return

    answer = ask('Please enter machine number.')
    try:
        machine_id = int(answer)
        machine = laundry.get_machine(machine_type, machine_id)
    except ValueError:
        print('Failed to parse number')
        return
    except Exception:
        print('Failed to find requested machine.')
        return
    machine.take_out()


def handle_help():
    print("""All available commands are:
    list  - to see all machines
    free  - to see all free machines
    find  - to find machine that finishes the cycle soonest
    start - to start the cycle
    out   - to empty the machine
    quit  - to exit the Laundry System""")