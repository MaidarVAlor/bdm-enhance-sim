# currently, there are no success boosting parameters (e.g. Advice of Valks) because that would require a rewrite
# however, you can restore instead

# Milky, if you are seeing this, have a good day!
# Royanka, I am very sorry that I wrote this in python lol

import random
import time

input_command = 0 # technical values
exit_command = 0
exit_function = 0


# value input functions
def input_level():
    while True:
        try:
            target = int(input("target enhancement level (integer, from 1 to 40): "))
            if 1 <= target <= 40:
                return target
            else:
                print(f"value '{target}' is out of range")
        except:
            print("this value cannot be used")


def awak_input_level():
    while True:
        try:
            target = int(input("target enhancement level (integer, from 1 to 10): "))
            if 1 <= target <= 10:
                return target
            else:
                print(f"value '{target}' is out of range")
        except:
            print("this value cannot be used")


def stone_input_level():
    while True:
        try:
            target = int(input("target enhancement level (integer, from 1 to 20): "))
            if 1 <= target <= 20:
                return target
            else:
                print(f"value '{target}' is out of range")
        except:
            print("this value cannot be used")


def acc_input_level():
    while True:
        try:
            target = int(input("target enhancement level (integer, from 1 to 10): "))
            if 1 <= target <= 10:
                return target
            else:
                print(f"value '{target}' is out of range")
        except:
            print("this value cannot be used")


def soul_input_level():
    while True:
        try:
            target = int(input("target enhancement level (integer, from 1 to 13): "))
            if 1 <= target <= 13:
                return target
            else:
                print(f"value '{target}' is out of range")
        except:
            print("this value cannot be used")


def soul_input_starting(tar):
    while True:
        try:
            s_starting = int(input("starting level (integer, from 0 to 12): "))
            if 0 <= s_starting <= 12:
                if s_starting >= tar:
                    print(f"value '{s_starting}' is the same as, or higher than target level")
                else:
                    return s_starting
            else:
                print(f"value '{s_starting}' is out of range")
        except:
            print("this value cannot be used")


def input_starting(tgt):
    while True:
        try:
            starting = int(input("starting level (integer, from 0 to 39): "))
            if 0 <= starting <= 39:
                if starting >= tgt:
                    print(f"value '{starting}' is the same as, or higher than target level")
                else:
                    return starting
            else:
                print(f"value '{starting}' is out of range")
        except:
            print("this value cannot be used")


def input_chance():
    while True:
        try:
            chance = int(input("success rate (integer, from 1 to 1000): "))
            if 1 <= chance <= 1000:
                return chance
            else:
                print(f"value '{chance}' is out of range")
        except:
            print("this value cannot be used")


def input_restoration():
    while True:
        try:
            restoration = int(input("restore item? "))
            if restoration in [0, 1, 2]:
                return restoration
            else:
                print(f"value '{restoration}' is out of range")
        except:
            print("this value cannot be used")


def enhancement_type():
    while True:
        try:
            e_type = int(input("enhancement type: "))
            if e_type in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return e_type
            elif e_type in [0]:
                print("exiting...")
                break
            elif e_type in [10]:
                print(" ")
                print("values available:")
                print("1 = enhancement at chosen rate (configured at the start)",
                      "2 = enhancement at chosen rate, reset on fail (configured at the start)",
                      sep='\n')
                print("3 = chaos gear enhancement", "4 = awakened Mys/Aby/Pri gear enhancement",
                      "5 = relic enhancement", sep='\n')
                print("6 = chaos alchemy stone enhancement", "7 = soul stone enhancement", sep='\n')
                print("8 = Pri/Cha/Ete accessory enhancement", "9 = rift totem enhancement", sep='\n')
                print("0 = go to exit menu", "10 = open this list again", sep='\n')
            else:
                print(f"value '{e_type}' is out of range")
        except:
            print("this value cannot be used")


# POLSKA GUROM TIME!
# 1. in Elden Ring, if you defeat Malenia, you will be welcomed with a victory text "ZABITO BOGA". that's because...
#    ...tłumacz przetłumaczył to zbyt dosłownie z języka angielskiego, and it became a meme in the r/EldenRing subreddit
# 2. in the Polish WW2-themed series "Czterej pancerni i pies", załoga walczyła w dwóch czołgach: T-34...
#    ...i T-34/85. the 2nd one can be easily distinguished by having larger turret and fuel tanks on the sides

# enhancement functions
def enhance_adjustable(x):
    att = 0  # attempts
    while x != target:
        time.sleep(0.625)  # comment this in order to skip the "realistic" enhancement intervals
        y = random.randint(0, 1000)
        if 0 <= y <= rate:  # upgrade success
            att += 1
            x += 1
            print(f"successful! +{x}")
        else:  # upgrade failure
            att += 1
            if x > 0:
                x -= 1
                if z == 0:  # checks if restoration is used
                    print(f"failed. +{x}")
                elif z == 1:
                    x += 1
                    print(f"restored! +{x}")
                else:
                    z_resto = random.randint(0, 1)
                    if z_resto == 1:  # restoration attempt
                        x += 1
                        print(f"restored! +{x}")
                    else:
                        print(f"failed. +{x}")
            else:
                print(f"failed. +{x}")
    return x, att


def enhance_rt_adjustable(x):
    att = 0
    while x != target:
        time.sleep(0.625)
        y = random.randint(0, 1000)
        if 0 <= y <= rate:
            att += 1
            x += 1
            print(f"successful! +{x}")
        else:
            att += 1
            if x > 0:
                if z == 0:  # reset on failure, if restoration was disabled
                    x = 0
                    print(f"failed. +{x}")
                else:  # if you type 1 or 2, both options function as "guaranteed restoration"
                    print(f"restored! +{x}")
            else:
                print(f"failed. +{x}")
    return x, att


def chaos_enhance():
    rates = [700, 600, 400, 200, 100, 70, 50, 30, 10, 5]  # dynamic rate depending on current enhancement level
    x = 0
    cch = 0
    att = 0  # attempts
    while x != ch_target:
        #time.sleep(0.75)
        y = random.randint(0, 1000)
        if 0 <= y <= rates[cch]:
            att += 1
            x += 1
            cch += 1
            print(f"successful! +{x}")
        else:
            att += 1
            if x > 0:
                x -= 1
                if z == 0:
                    cch -= 1
                    print(f"failed. +{x}")
                else:
                    z_resto = random.randint(0, 1)
                    if z_resto == 1:  # if you type 1 or 2, both function as "50% restoration chance"
                        x += 1
                        print(f"restored! +{x}")
                    else:
                        cch -= 1
                        print(f"failed. +{x}")
            else:
                print(f"failed. +{x}")
    return x, att


def awak_enhance():
    rates = [700, 600, 400, 200, 100, 70, 50, 30, 10, 5]
    level_name = ["+40", "PRI", "DUO", "TRI", "TET",
                  "PEN", "HEX", "HEP", "OCT", "ENE", "DEC"]  # dynamic enhancement level name
    x = 0
    cch = 0
    att = 0
    while x != awak_target:
        #time.sleep(0.75)
        y = random.randint(0, 1000)
        if 0 <= y <= rates[cch]:
            att += 1
            x += 1
            cch += 1
            print(f"successful! {level_name[x]}")
        else:
            att += 1
            if x > 0:
                x -= 1
                if z == 0:
                    cch -= 1
                    print(f"failed. {level_name[x]}")
                else:
                    z_resto = random.randint(0, 1)
                    if z_resto == 1:
                        x += 1
                        print(f"restored! {level_name[x]}")
                    else:
                        cch -= 1
                        print(f"failed. {level_name[x]}")
            else:
                print(f"failed. {level_name[x]}")
    return level_name[x], att


def relic_enhance():
    rates = [500, 300, 100, 100, 100, 80, 50, 30, 10, 5]
    x = 0
    cch = 0
    att = 0
    while x != relic_target:
        #time.sleep(0.625)
        y = random.randint(0, 1000)
        if 0 <= y <= rates[cch]:
            att += 1
            x += 1
            cch += 1
            print(f"successful! +{x}")
        else:
            att += 1
            if x > 0:
                if z == 0:
                    x = 0
                    cch = 0
                    print(f"failed. +{x}")
                else:
                    print(f"restored! +{x}")
            else:
                print(f"failed. +{x}")
    return x, att


def stone_enhance():
    rates = [1000, 1000, 1000, 600, 510, 280, 90, 40, 10, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1]
    level_name = ["+0", "+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8", "+9", "+10",
                  "PRI", "DUO", "TRI", "TET", "PEN",
                  "HEX", "HEP", "OCT", "ENE", "DEC"]  # that one took a solid minute to write all the levels
    x = 0
    cch = 0
    att = 0
    while x != stone_target:
        #time.sleep(0.625)
        y = random.randint(0, 1000)
        if 0 <= y <= rates[cch]:
            att += 1
            x += 1
            cch += 1
            print(f"successful! {level_name[x]}")
        else:
            att += 1
            if x > 0:
                if z == 0:
                    x = 0
                    cch = 0
                    print(f"failed. {level_name[x]}")
                else:
                    print(f"restored! {level_name[x]}")
            else:
                print(f"failed. {level_name[x]}")
    return level_name[x], att


def soul_enhance(x):
    att = 0
    while x != soul_target:
        time.sleep(0.625)
        y = random.randint(0, 1000)
        if 0 <= y <= 510:  # Soul Stones have a fixed success rate of 51%
            att += 1
            x += 1
            print(f"successful! +{x}")
        else:
            att += 1
            if x > 0:
                if z == 0:
                    x = 0
                    print(f"failed. +{x}")
                else:
                    print(f"restored! +{x}")
            else:
                print(f"failed. +{x}")
    return x, att


def acc_enhance():
    rates = [1000, 1000, 1000, 600, 410, 280, 90, 40, 10, 3]
    x = 0
    cch = 0
    att = 0
    while x != acc_target:
        #time.sleep(0.625)
        y = random.randint(0, 1000)
        if 0 <= y <= rates[cch]:
            att += 1
            x += 1
            cch += 1
            print(f"successful! +{x}")
        else:
            att += 1
            if x > 0:
                if z == 0:
                    x = 0
                    cch = 0
                    print(f"failed. +{x}")
                else:
                    print(f"restored! +{x}")
            else:
                print(f"failed. +{x}")
    return x, att

def rift_enhance():
    rates = [700, 600, 500, 300, 150, 100, 50, 30, 20, 10]
    x = 0
    cch = 0
    att = 0
    while x != rift_target:
        #time.sleep(0.625)
        y = random.randint(0, 1000)
        if 0 <= y <= rates[cch]:
            att += 1
            x += 1
            cch += 1
            print(f"successful! +{x}")
        else:
            att += 1
            if x > 0:
                if z == 0:
                    x = 0
                    cch = 0
                    print(f"failed. +{x}")
                else:
                    if 1 <= x <= 7:
                        print(f"restored! +{x}")
                    else:
                        x = 0
                        cch = 0
                        print(f"failed. +{x}")
            else:
                print(f"failed. +{x}")
    return x, att

# CAUTION: HUGE LOOP WALL OF TEXT AHEAD

while input_command != "EXIT" or input_command != "exit":
    target = input_level()  # get user's preferences
    ce_lvl = input_starting(target)
    print(" ")
    print("input example: 472 = 47.2%")
    rate = input_chance()
    print(" ")
    print("values: 0 = no restoration, 1 = guaranteed restoration, 2 = restoration at 50% rate")
    z = input_restoration()
    print(" ")
    print("values available:")
    print("1 = enhancement at chosen rate (configured at the start)",
          "2 = enhancement at chosen rate, reset on fail (configured at the start)",
          sep='\n')
    print("3 = chaos gear enhancement", "4 = awakened Mys/Aby/Pri gear enhancement", "5 = relic enhancement", sep='\n')
    print("6 = chaos alchemy stone enhancement", "7 = soul stone enhancement", sep='\n')
    print("8 = Pri/Cha/Ete accessory enhancement", "9 = rift totem enhancement", sep='\n')
    print("0 = go to exit menu", "10 = open enhancement list", sep='\n')

    while exit_command != "QUIT" or exit_command != "quit":
        ft = enhancement_type()  # enhancement selection
        if ft == 1:
            confirm = input("selected 'enhancement at chosen rate', proceed? (Y/'N or anything else') ")
            if confirm == "Y" or confirm == "y":
                while exit_function != "STOP" or exit_function != "stop":
                    end_result = enhance_adjustable(ce_lvl)  # initialize the function
                    print(f"reached enhancement level {end_result[0]} (from {ce_lvl}) within {end_result[1]} attempts")
                    exit_function = input("repeat or type 'STOP' to exit this enhancement: ")
                    print(" ")
                    if exit_function == "STOP" or exit_function == "stop":
                        break
            else:
                continue
        elif ft == 2:
            confirm = input("selected 'enhancement at chosen rate, reset on fail', proceed? (Y/'N or anything else') ")
            if confirm == "Y" or confirm == "y":
                print("NOTE: restoration is guaranteed, regardless of choosing 1 or 2 as restoration option...")
                print("      unless you have typed 0 to not do restorations at all...")
                while exit_function != "STOP" or exit_function != "stop":
                    end_result = enhance_rt_adjustable(ce_lvl)
                    print(f"reached enhancement level {end_result[0]} (from {ce_lvl}) within {end_result[1]} attempts")
                    exit_function = input("repeat or type 'STOP' to exit this enhancement: ")
                    print(" ")
                    if exit_function == "STOP" or exit_function == "stop":
                        break
            else:
                continue
        elif ft == 3:
            confirm = input("selected 'chaos gear enhancement', proceed? (Y/'N or anything else') ")
            if confirm == "Y" or confirm == "y":
                print(" ", "NOTE: this enhancement requires separate target level data", sep='\n')
                print("CAUTION: this function has intervals disabled. to enable intervals, uncomment 'time.sleep' line")
                print(" ")
                ch_target = awak_input_level()
                print(" ")
                print("values: 0 = no restoration, 1 or 2 = restoration at 50% rate")
                z = input_restoration()
                while exit_function != "STOP" or exit_function != "stop":
                    end_result = chaos_enhance()
                    print(f"reached enhancement level {end_result[0]} within {end_result[1]} attempts")
                    exit_function = input("repeat or type 'STOP' to exit this enhancement: ")
                    if exit_function == "STOP" or exit_function == "stop":
                        break
            else:
                continue
        elif ft == 4:
            confirm = input("selected 'awakened Mys/Aby/Pri gear enhancement', proceed? (Y/'N or anything else') ")
            if confirm == "Y" or confirm == "y":
                print(" ", "NOTE: this enhancement requires separate target level data", sep='\n')
                print("CAUTION: this function has intervals disabled. to enable intervals, uncomment 'time.sleep' line")
                print(" ")
                awak_target = awak_input_level()
                print(" ")
                print("values: 0 = no restoration, 1 or 2 = restoration at 50% rate")
                z = input_restoration()
                while exit_function != "STOP" or exit_function != "stop":
                    end_result = awak_enhance()
                    print(f"reached enhancement level {end_result[0]} within {end_result[1]} attempts")
                    exit_function = input("repeat or type 'STOP' to exit this enhancement: ")
                    if exit_function == "STOP" or exit_function == "stop":
                        break
            else:
                continue
        elif ft == 5:
            confirm = input("selected 'relic enhancement', proceed? (Y/'N or anything else') ")
            if confirm == "Y" or confirm == "y":
                print(" ", "NOTE: this enhancement requires separate target level data", sep='\n')
                print("CAUTION: this function has intervals disabled. to enable intervals, uncomment 'time.sleep' line")
                print(" ")
                relic_target = awak_input_level()
                print(" ")
                print("values: 0 = no restoration, 1 or 2 = guaranteed restoration")
                z = input_restoration()
                while exit_function != "STOP" or exit_function != "stop":
                    end_result = relic_enhance()
                    print(f"reached enhancement level {end_result[0]} within {end_result[1]} attempts")
                    exit_function = input("repeat or type 'STOP' to exit this enhancement: ")
                    if exit_function == "STOP" or exit_function == "stop":
                        break
            else:
                continue
        elif ft == 6:
            confirm = input("selected 'chaos alchemy stone enhancement', proceed? (Y/'N or anything else') ")
            if confirm == "Y" or confirm == "y":
                print(" ", "NOTE: this enhancement requires separate target level data", sep='\n')
                print("CAUTION: this function has intervals disabled. to enable intervals, uncomment 'time.sleep' line")
                print(" ")
                stone_target = stone_input_level()
                print(" ")
                print("values: 0 = no restoration, 1 or 2 = guaranteed restoration")
                z = input_restoration()
                while exit_function != "STOP" or exit_function != "stop":
                    end_result = stone_enhance()
                    print(f"reached enhancement level {end_result[0]} within {end_result[1]} attempts")
                    exit_function = input("repeat or type 'STOP' to exit this enhancement: ")
                    if exit_function == "STOP" or exit_function == "stop":
                        break
            else:
                continue
        elif ft == 7:
            confirm = input("selected 'soul stone enhancement', proceed? (Y/'N or anything else') ")
            if confirm == "Y" or confirm == "y":
                print(" ", "NOTE: this enhancement requires separate target/starting level data", sep='\n')
                print(" ")
                soul_target = soul_input_level()
                soul_ce_lvl = soul_input_starting(soul_target)
                print(" ")
                print("values: 0 = no restoration, 1 or 2 = guaranteed restoration")
                z = input_restoration()
                while exit_function != "STOP" or exit_function != "stop":
                    end_result = soul_enhance(soul_ce_lvl)
                    print(f"reached enhancement level {end_result[0]} within {end_result[1]} attempts")
                    exit_function = input("repeat or type 'STOP' to exit this enhancement: ")
                    if exit_function == "STOP" or exit_function == "stop":
                        break
            else:
                continue
        elif ft == 8:
            confirm = input("selected 'Pri/Cha/Ete accessory enhancement', proceed? (Y/'N or anything else') ")
            if confirm == "Y" or confirm == "y":
                print(" ", "NOTE: this enhancement requires separate target level data", sep='\n')
                print("CAUTION: this function has intervals disabled. to enable intervals, uncomment 'time.sleep' line")
                print(" ")
                acc_target = acc_input_level()
                print(" ")
                print("values: 0 = no restoration, 1 or 2 = guaranteed restoration")
                z = input_restoration()
                while exit_function != "STOP" or exit_function != "stop":
                    end_result = acc_enhance()
                    print(f"reached enhancement level {end_result[0]} within {end_result[1]} attempts")
                    exit_function = input("repeat or type 'STOP' to exit this enhancement: ")
                    if exit_function == "STOP" or exit_function == "stop":
                        break
            else:
                continue
        elif ft == 9:
            confirm = input("selected 'rift totem enhancement', proceed? (Y/'N or anything else') ")
            if confirm == "Y" or confirm == "y":
                print(" ", "NOTE: this enhancement requires separate target level data", sep='\n')
                print("CAUTION: this function has intervals disabled. to enable intervals, uncomment 'time.sleep' line")
                print(" ")
                rift_target = acc_input_level()
                print(" ")
                print("values: 0 = no restoration, 1 or 2 = restoration at levels 1-7")
                z = input_restoration()
                while exit_function != "STOP" or exit_function != "stop":
                    end_result = rift_enhance()
                    print(f"reached enhancement level {end_result[0]} within {end_result[1]} attempts")
                    exit_function = input("repeat or type 'STOP' to exit this enhancement: ")
                    if exit_function == "STOP" or exit_function == "stop":
                        break

        else:
            exit_command = "QUIT"  # quit enhancement selection and reset enhancement configuration
            target = 0
            ce_lvl = 0
            rate = 0
            z = 0
            break
    input_command = input("type 'EXIT' to quit or leave this input and proceed to enhancing again: ")
    if input_command == "EXIT" or input_command == "exit":
        break  # exit when user wants it...
    else:
        continue  # ...or continue it

print('\n' * 100)
print("heyyyyy, thank you for using my enhancement simulator!", " ", "you can find me in other places too!", sep='\n')
print("> BDM - Mairad",
      "> discord - mvathemage",
      "> twitch - maidarthevalor (can find me on Whizkid05's and JonathanGD's stream chats, rarely anywhere else)",
      "> github - MaidarVAlor", sep='\n')
