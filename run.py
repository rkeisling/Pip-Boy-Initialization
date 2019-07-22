import sys, time
from playsound import playsound
import random
from threading import Thread
from convert_image_to_ascii import print_ascii

def main():
    display_starting_junk()
    disply_intro()
    play_success_sound()
    display_vault_boy()


def display_starting_junk():
    for i in range(40):
        print('\n')
        time.sleep(0.05)
    print_one_by_one_some_sound(make_starting_junk())
    for i in range(40):
        print('\n')
        time.sleep(0.05)

def disply_intro():
    lines = ['*************** PIP-OS(R) V1.0 ***************\n',
    ' \n', ' \n', ' \n',
    'COPYRIGHT 2075 ROBCO(R)\n',
    'LOADER V1.1\n',
    'EXEC VERSION 41.10\n',
    '64k RAM SYSTEM\n',
    '38911 BYTES FREE\n',
    'NO HOLOTAPE FOUND\n',
    'LOAD ROM(1): DEITRIX 303\n']

    for line in lines:
        print_one_by_one_with_sound(line, delay=0.1)

    for i in range(30):
        print('\n')
        time.sleep(0.05)

def display_vault_boy():
    img = 'vault_boy.jpeg'
    print_ascii(img)

def print_one_by_one_with_sound(text, delay=0.25):
    for char in text:
        if char != ' ' and char != '\n':
            thread = Thread(target=play_random_sound)
            thread.start()
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def print_one_by_one_some_sound(text, delay=0.001):
    for char in text:
        roll_for_sound = random.randrange(1,51)
        if roll_for_sound == 7:
            thread = Thread(target=play_random_sound)
            thread.start()
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def play_random_sound():
    sounds = ['short_type.wav', 'short_type2.wav',
              'short_type3.wav', 'short_type4.wav',
              '', '', '', '', '', '', '']
    sound_to_play = random.choice(sounds)
    if sound_to_play == '':
        return
    playsound(sound_to_play)

def play_success_sound():
    playsound('ui_hacking_passgood.wav')

def make_starting_junk():
    keyphrases = [' start memory discovery', ' CPUO starting cell relocation',
                  ' CPUO launch EFIO', ' CPUO starting EFIO']
    middle_pieces = [' 1', ' 0', ' 0x0000A4', ' 0x00000000000000000',
                     ' 0x000014', ' 0x000009', ' 0x000000000000E003D']
    # get 3-7 of middle pieces to put in between keyphrases
    # begin large string with *
    huge_string = '*'
    for i in range(70):
        num_middle_pieces = random.randrange(3,8)
        middle_piece = ''
        for i in range(num_middle_pieces):
            middle_piece += random.choice(middle_pieces)
        huge_string += middle_piece
        huge_string += random.choice(keyphrases)

    return huge_string

if __name__ == '__main__':
    main()
