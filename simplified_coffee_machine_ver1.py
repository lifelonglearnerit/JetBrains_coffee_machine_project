"""
This is the original version of code submitted for grading on JetBrains Academy
Cheers t.
"""
class CoffeeMachine: state = 'OFF'

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
    print(self.state)

def startup(self):
        self.state = 'ON'
        self.action_menu()

def display_levels(self):
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
    self.espr_recip = {
        'water': 250,
        'milk': 0,
        'beans': 16,
        'cups': 1,
        'money': 4}

    for key in self.espr_recip:
        if self.espr_recip[key] > self.machine_levels[key]:
            print('Sorry, not enough ' + key + '!')
            self.action_menu()
        else:
            print('I have enough resources, making you a coffee!')
            for key in self.espr_recip:
                if key == 'money':
                    self.machine_levels['money'] += self.espr_recip['money']
                else:
                    self.machine_levels[key] -= self.espr_recip[key]
            self.action_menu()

def latte_prep(self):
    self.state = "ON - latte_prep"
    self.latte_recip = {
        'water': 350,
        'milk': 75,
        'beans': 20,
        'cups': 1,
        'money': 7}

    for key in self.latte_recip:
        if self.latte_recip[key] > self.machine_levels[key]:
            print('Sorry, not enough ' + key + '!')
            self.action_menu()
        else:
            print('I have enough resources, making you a coffee!')
            for key in self.latte_recip:
                if key == 'money':
                    self.machine_levels['money'] += self.latte_recip['money']
                else:
                    self.machine_levels[key] -= self.latte_recip[key]
            self.action_menu()

def cappuccino_prep(self):
    self.state = "ON - cappuccino_prep"
    self.capp_recip = {
        'water': 200,
        'milk': 100,
        'beans': 12,
        'cups': 1,
        'money': 6}

    for key in self.capp_recip:
        if self.capp_recip[key] > self.machine_levels[key]:
            print('Sorry, not enough ' + key + '!')
            self.action_menu()
        else:
            print('I have enough resources, making you a coffee!')
            for key in self.capp_recip:
                if key == 'money':
                    self.machine_levels['money'] += self.capp_recip['money']
                else:
                    self.machine_levels[key] -= self.capp_recip[key]
            self.action_menu()

def fill_machine(self):
    self.state = 'ON - fill_machine'
    print()
    self.machine_levels['water'] += int(input('Write how many ml of water do you want to add:\n'))
    self.machine_levels['milk'] += int(input('Write how many ml of milk do you want to add:\n'))
    self.machine_levels['beans'] += int(input('Write how many grams of coffee beans do you want to add:\n'))
    self.machine_levels['cups'] += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    self.action_menu()
def take_money(self):
    self.state = 'ON - take_money'
    print('I gave you ${}'.format(self.machine_levels['money']))
    self.machine_levels['money'] -= self.machine_levels['money']
    self.action_menu()

def switch_off(self):
    self.state = 'Switching OFF - machine'
    exit()