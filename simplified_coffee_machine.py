from datetime import datetime
class CoffeeMachine:
    state = 'OFF'


    machine_levels = {
        'water': 400,
        'milk': 540,
        'beans': 120,
        'cups': 9,
        'money': 550}

    def __init__(self):
        if self.state == 'OFF':
            self.startup()

    def status(self):
        time_now = datetime.now()
        time_stamp = time_now.strftime('%H:%M:%S')
        with open('machine_state_log.txt', 'a+') as log:
            if self.state != 'OFF':
                log.write(self.state)
                log.write(' - ')
                log.write(time_stamp)
                log.write('\n')

    def startup(self):
            self.state = 'ON'
            self.status()
            self.action_menu()

    def display_levels(self):
        self.state = 'ON - display_levels'
        self.status()
        print()
        print('The coffee machine has:')
        print('{} of water'.format(self.machine_levels['water']))
        print('{} of milk'.format(self.machine_levels['milk']))
        print('{} of coffee beans'.format(self.machine_levels['beans']))
        print('{} of disposable cups'.format(self.machine_levels['cups']))
        print('${} of money'.format(self.machine_levels['money']))
        self.action_menu()

    def action_menu(self):
        self.state = "ON - action_menu"
        self.status()
        print()
        print('Write action (buy, fill, take, remaining, exit):')
        actions = {'buy': self.coffee_menu,
                   'fill': self.fill_machine,
                   'take': self.take_money,
                   'remaining': self.display_levels,
                   'exit': self.switch_off
                   }
        actions[input()]()

    def coffee_menu(self):
        self.state = "ON - coffee_menu"
        self.status()
        coffee = {'1': self.espresso_prep,
                  '2': self.latte_prep,
                  '3': self.cappuccino_prep,
                  'back': self.action_menu
                  }

        coffee[input('What do you want to buy? '
                     '1 - espresso, '
                     '2 - latte, '
                     '3 - capuccino, '
                     'back - to main menu:\n')]()

    def espresso_prep(self):
        self.state = "ON - espresso_prep"
        self.status()
        self.espr_recip = {
            'water': 250,
            'milk': 0,
            'beans': 16,
            'cups': 1,
            'money': 4}
        self.coffee_preparation(self.espr_recip)

    def latte_prep(self):
        self.state = "ON - latte_prep"
        self.status()
        self.latte_recip = {
            'water': 350,
            'milk': 75,
            'beans': 20,
            'cups': 1,
            'money': 7}
        self.coffee_preparation(self.latte_recip)

    def cappuccino_prep(self):
        self.state = "ON - cappuccino_prep"
        self.status()
        self.capp_recip = {
            'water': 200,
            'milk': 100,
            'beans': 12,
            'cups': 1,
            'money': 6}
        self.coffee_preparation(self.capp_recip)

    def fill_machine(self):
        self.state = 'ON - fill_machine'
        self.status()
        print()
        self.machine_levels['water'] += int(input('Write how many ml of water do you want to add:\n'))
        self.machine_levels['milk'] += int(input('Write how many ml of milk do you want to add:\n'))
        self.machine_levels['beans'] += int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.machine_levels['cups'] += int(input('Write how many disposable cups of coffee do you want to add:\n'))
        self.action_menu()

    def take_money(self):
        self.state = 'ON - take_money'
        self.status()
        print('I gave you ${}'.format(self.machine_levels['money']))
        self.machine_levels['money'] -= self.machine_levels['money']
        self.action_menu()

    def switch_off(self):
        self.state = 'Switching OFF - machine'
        self.status()
        exit()

    def coffee_preparation(self, recip):
        self.state = 'ON - coffee_preparation'
        self.status()
        for key in recip:
            if recip[key] > self.machine_levels[key]:
                print('Sorry, not enough ' + key + '!')
                self.action_menu()
            else:
                print('I have enough resources, making you a coffee!')
                for key in recip:
                    if key == 'money':
                        self.machine_levels['money'] += recip['money']
                    else:
                        self.machine_levels[key] -= recip[key]
                self.action_menu()

CoffeeMachine()
# Cheers t.
