import random

THING_LIST = ['butterfly',
              'toothpaste',
              'raincoat',
              'harmonica',
              'trampoline',
              'gargoyle',
              'macaroni',
              'buffalo',
              'thunder',
              'literature'
              ]

PERSON_LIST = ['ballerina',
               'Madonna',
               'Obama',
               'Einstein',
               'Napoleon',
               'governor',
               'astronaut',
               'Rihanna',
               'Pocahontas',
               'author'
               ]

PLACE_LIST = ['London',
              'Paris',
              'Russia',
              'Toledo',
              'Antarctica',
              'Aruba',
              'Paraguay',
              'Cairo',
              'Mongolia',
              'Seoul',
              ]


def choose_ppt():
    """Generates a random person, place, or thing using APIs."""
    ppt_choice = random.randrange(0, 3)
    index = random.randrange(0, 10)
    if ppt_choice == 0:
        return 'thing', THING_LIST[index]
    elif ppt_choice == 1:
        return 'place', PLACE_LIST[index]
    else:
        return 'person', PERSON_LIST[index]


while True:
    with open('SpinToWinInput.txt', 'r+') as input_file:
        user_input = input_file.readline()
        if user_input == 'get':
            input_file.seek(0)
            input_file.truncate()
            input_file.close()
            return_value = choose_ppt()
            with open('SpinToWinOutput.txt', 'w') as output_file:
                output_file.write(str(return_value))
                output_file.close()
        input_file.close()
