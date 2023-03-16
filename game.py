"""
Strategy type guessing game for player vs computer."""

import random
import sys
import copy

ships_undamaged = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
ships_damaged = ["a'", "b'", "c'", "d'", "e'", "f'", "g'", "h'", "i'", "j'"]
ships_ = {"a": 4, "b": 3, "c": 3, "d": 2, "e": 2, "f": 2, "g": 1, "h": 1, "i": 1, "j": 1}

ships = {"a": {"cells_left": 4, "ship_coordinates": [], "ship_areola": []},
         "b": {"cells_left": 3, "ship_coordinates": [], "ship_areola": []},
         "c": {"cells_left": 3, "ship_coordinates": [], "ship_areola": []},
         "d": {"cells_left": 2, "ship_coordinates": [], "ship_areola": []},
         "e": {"cells_left": 2, "ship_coordinates": [], "ship_areola": []},
         "f": {"cells_left": 2, "ship_coordinates": [], "ship_areola": []},
         "g": {"cells_left": 1, "ship_coordinates": [], "ship_areola": []},
         "h": {"cells_left": 1, "ship_coordinates": [], "ship_areola": []},
         "i": {"cells_left": 1, "ship_coordinates": [], "ship_areola": []},
         "j": {"cells_left": 1, "ship_coordinates": [], "ship_areola": []},
         }

target_data = {"found_coordinates": [], "directions": [], "start_from": []}

player = copy.deepcopy(ships)  # stores data for player's ships
enemy = copy.deepcopy(ships)  # stores data for enemy's ships
enemy_hits = []  # stores data about enemy's hits

player_field_secret = {}  # stores all the data about player's field
player_field_open = {}  # displays player's field in user-friendly way
enemy_field_secret = {}  # stores all the data about enemy's field
enemy_field_open = {}  # displays enemy's field hidden until it's explored by the player

# populating battlefields
line_x_s = ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
for i in range(0, 10):
    player_field_secret[i] = line_x_s.copy()
    player_field_open[i] = line_x_s.copy()
    enemy_field_secret[i] = line_x_s.copy()
    enemy_field_open[i] = line_x_s.copy()


def checking(ship_p, aux, field):
    """ Function checks if provided cell are empty to place ship """
    counter = 0
    for ind in ship_p:
        if ind[0] in range(0, 10) and ind[1] in range(0, 10):  # ship cells in range
            x = ind[0]
            y = ind[1]
            if field[y][x] == "w":
                counter += 1
            else:
                counter += 0
        else:
            counter += 0

    for ind in aux:
        if ind[0] in range(0, 10) and ind[1] in range(0, 10):  # ship cells in range
            x = ind[0]
            y = ind[1]
            if field[y][x] == "w":
                counter += 1
            else:
                counter += 0
        elif ind[0] not in range(0, 10) or ind[1] not in range(0, 10):
            counter += 1  # ?

    return counter == len(ship_p) + len(aux)  # True when all ship and surrounding cells are free


def points(x, y, num, direction):
    """ Function generates cells for ship depending on ship length and nesting direction """
    while True:
        ship_p = []

        if direction == "up":
            for i in range(0, num):
                if y in range(0, 10) and x in range(0, 10):
                    ship_p.append([x, y])
                    y = y - 1
                else:
                    break

            if len(ship_p) == num:
                return ship_p

            else:
                return ship_p

        if direction == "down":
            for i in range(0, num):
                if y in range(0, 10) and x in range(0, 10):
                    ship_p.append([x, y])
                    y = y + 1
                else:
                    break

            if len(ship_p) == num:
                return ship_p

            else:
                return ship_p

        if direction == "right":
            for i in range(0, num):
                if y in range(0, 10) and x in range(0, 10):
                    ship_p.append([x, y])
                    x = x + 1
                else:
                    break
            if len(ship_p) == num:
                return ship_p

            else:
                return ship_p

        if direction == "left":
            for i in range(0, num):
                if y in range(0, 10) and x in range(0, 10):
                    ship_p.append([x, y])
                    x = x - 1
                else:
                    break
            if len(ship_p) == num:
                return ship_p

            else:
                return ship_p


def surround(x, y, num, direction):
    """ Function generates ship surrounding cells """
    while True:
        aux = []

        if direction == "up":
            aux.append([x, y + 1])  # below target point
            aux.append([x + 1, y + 1])
            aux.append([x - 1, y + 1])

            aux.append([x, y - num])  # above end point
            aux.append([x + 1, y - num])
            aux.append([x - 1, y - num])

            for i in range(0, num):
                if y in range(0, 10) and x in range(0, 10):
                    aux.append([x + 1, y])
                    aux.append([x - 1, y])

                    y = y - 1
                else:
                    break

            return aux

        if direction == "down":
            aux.append([x, y - 1])  # above target point
            aux.append([x + 1, y - 1])
            aux.append([x - 1, y - 1])

            aux.append([x, y + num])  # below end point
            aux.append([x + 1, y + num])
            aux.append([x - 1, y + num])

            for i in range(0, num):
                if y in range(0, 10) and x in range(0, 10):
                    aux.append([x + 1, y])
                    aux.append([x - 1, y])

                    y = y + 1
                else:
                    break

            return aux

        if direction == "right":

            aux.append([x - 1, y])  # left from target point
            aux.append([x - 1, y + 1])
            aux.append([x - 1, y - 1])

            aux.append([x + num, y])  # right from end point
            aux.append([x + num, y + 1])
            aux.append([x + num, y - 1])

            for i in range(0, num):
                if y in range(0, 10) and x in range(0, 10):
                    aux.append([x, y + 1])
                    aux.append([x, y - 1])

                    x = x + 1
                else:
                    break

            return aux

        if direction == "left":

            aux.append([x + 1, y])  # right from target point
            aux.append([x + 1, y + 1])
            aux.append([x + 1, y - 1])

            aux.append([x - num, y])  # left from end point
            aux.append([x - num, y + 1])
            aux.append([x - num, y - 1])

            for i in range(0, num):
                if y in range(0, 10) and x in range(0, 10):
                    aux.append([x, y + 1])
                    aux.append([x, y - 1])
                    x = x - 1
                else:
                    break

            return aux


def place_ship(num, field, name):
    """ Function nests ships """
    while True:
        directions = []
        ship_coordinates = []
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        up_s = points(x, y, num, "up")
        up_a = surround(x, y, num, "up")
        if len(up_s) == num and checking(up_s, up_a, field) == True:
            directions.append("up")
        else:
            pass

        down_s = points(x, y, 4, "down")
        down_a = surround(x, y, 4, "down")
        if len(down_s) == num and checking(down_s, down_a, field) == True:
            directions.append("down")
        else:
            pass

        left_s = points(x, y, 4, "left")
        left_a = surround(x, y, 4, "left")
        if len(left_s) == num and checking(left_s, left_a, field) == True:
            directions.append("left")

        right_s = points(x, y, 4, "right")
        right_a = surround(x, y, 4, "right")
        if len(right_s) == num and checking(right_s, right_a, field) == True:
            directions.append("right")

        if len(directions) == 0:
            continue
        else:

            choice = random.choice(directions)

            if choice == "up":
                ship_coordinates = up_s
                if field == player_field_secret:
                    player[name]["ship_coordinates"] = up_s
                    player[name]["ship_areola"] = up_a
                elif field == enemy_field_secret:
                    enemy[name]["ship_coordinates"] = up_s
                    enemy[name]["ship_areola"] = up_a

            if choice == "down":
                ship_coordinates = down_s
                if field == player_field_secret:
                    player[name]["ship_coordinates"] = down_s
                    player[name]["ship_areola"] = down_a
                elif field == enemy_field_secret:
                    enemy[name]["ship_coordinates"] = down_s
                    enemy[name]["ship_areola"] = down_a

            if choice == "left":
                ship_coordinates = left_s
                if field == player_field_secret:
                    player[name]["ship_coordinates"] = left_s
                    player[name]["ship_areola"] = left_a
                elif field == enemy_field_secret:
                    enemy[name]["ship_coordinates"] = left_s
                    enemy[name]["ship_areola"] = left_a

            if choice == "right":
                ship_coordinates = right_s
                if field == player_field_secret:
                    player[name]["ship_coordinates"] = right_s
                    player[name]["ship_areola"] = right_a
                elif field == enemy_field_secret:
                    enemy[name]["ship_coordinates"] = right_s
                    enemy[name]["ship_areola"] = right_a

            for cell in ship_coordinates:
                field[cell[1]][cell[0]] = name
            break


def transfer_field(field_from, field_to):
    """ Function translate data about battlefields in userfriendly view"""

    if field_from == player_field_secret:
        for y in field_from:
            for x in range(0, 10):
                if field_from[y][x] == "w":
                    field_to[y][x] = " "
                elif field_from[y][x] == "x":
                    field_to[y][x] = "x"
                elif field_from[y][x] in ships_damaged:
                    field_to[y][x] = "⊗"
                elif field_from[y][x] in ships_undamaged:
                    field_to[y][x] = "●"
    elif field_from == enemy_field_secret:
        for y in field_from:
            for x in range(0, 10):
                if field_from[y][x] == "w":
                    field_to[y][x] = "░"
                elif field_from[y][x] == "x":
                    field_to[y][x] = "~"
                elif field_from[y][x] == "*":
                    field_to[y][x] = "~"
                elif field_from[y][x] in ships_damaged:
                    field_to[y][x] = "⊗"
                elif field_from[y][x] in ships_undamaged:
                    field_to[y][x] = "░"


def player_hit(field_to_check=enemy_field_secret):
    """ Function processing player's turns """
    if field_to_check == enemy_field_secret:
        while True:
            # logic for player's hits
            x = input("\n\tWaiting for coordinate X or (q) for quit: ")
            if x.lower() == "q":
                sys.exit()
            if x.isdigit() and int(x) in range(0, 10):
                x = int(x)
            else:
                print("Please input digit in range 0...9 for X.")
                continue

            y = input("\tWaiting for coordinate Y or (q) for quit: ")
            if y.lower() == "q":
                sys.exit()
            if y.isdigit() and int(y) >= 0 in range(0, 10):
                y = int(y)
            else:
                print("Please input digit in range 0...9 for Y.")
                continue

            if field_to_check[y][x] == "w":
                field_to_check[y][x] = "x"
                print("You've missed! ", end="")
                break


            elif field_to_check[y][x] == "*":
                field_to_check[y][x] = "x"
                print("You've missed! ", end="")
                break

            elif field_to_check[y][x] == "x":
                print("Lightning does not strike twice. But you do! ", end="")
                break

            elif field_to_check[y][x] in ships_damaged:
                print("Lightning does not strike twice. But you do! ", end="")
                break

            elif field_to_check[y][x] in ships_undamaged:
                enemy[field_to_check[y][x]]['cells_left'] = enemy[field_to_check[y][x]][
                                                                'cells_left'] - 1  # minus 1 life
                if enemy[field_to_check[y][x]]['cells_left'] > 0:
                    print("Hit! Enemy's ship was damaged but still afloat. You have another shot to make! ")
                    field_to_check[y][x] = f"{field_to_check[y][x]}'"  # a becomes a'
                    display_fields_(player_field_open, enemy_field_open)
                    continue

                if enemy[field_to_check[y][x]]['cells_left'] <= 0:
                    print("Hit! Enemy's ship sunk. You have another shot to make! ")
                    if check_score("player") >= 20:
                        print("\nGAME OVER. You won!")
                        sys.exit()
                    for point in enemy[field_to_check[y][x]]['ship_areola']:
                        if point[1] in range(0, 10) and point[0] in range(0, 10):
                            field_to_check[point[1]][point[0]] = "*"
                    field_to_check[y][x] = f"{field_to_check[y][x]}'"  # a becomes a'
                    display_fields_(player_field_open, enemy_field_open)
                    continue


def display_fields_(field_1, field_2):
    """ Function displays battlefields"""

    transfer_field(player_field_secret, player_field_open)
    transfer_field(enemy_field_secret, enemy_field_open)
    plsc = str(check_score("player"))
    ensc = str(check_score("enemy"))
    print(" ")
    print(
        f"YOUR SCORE ({plsc.rjust(2)}) _________________________          ENEMY'S SCORE ({ensc.rjust(2)}) _____________________")
    print(f"    0   1   2   3   4   5   6   7   8   9             0   1   2   3   4   5   6   7   8   9")
    for y in range(0, 10):
        print(f"{y}:  {field_1[y][0]}   {field_1[y][1]}   {field_1[y][2]}   {field_1[y][3]}   {field_1[y][4]}"
              f"   {field_1[y][5]}   {field_1[y][6]}   {field_1[y][7]}   {field_1[y][8]}   {field_1[y][9]}"
              f"    |    {y}:  {field_2[y][0]}   {field_2[y][1]}   {field_2[y][2]}   {field_2[y][3]}   {field_2[y][4]}"
              f"   {field_2[y][5]}   {field_2[y][6]}   {field_2[y][7]}   {field_2[y][8]}   {field_2[y][9]}")
    print(f"___________________________________________________________________________________________")


def check_score(who):
    """ Function computing scores"""
    if who == "player":
        player_score = 0
        for ship in ships_undamaged:
            player_score = player_score + enemy[ship]["cells_left"]
        player_score = 4 + 3 + 3 + 2 + 2 + 2 + 1 + 1 + 1 + 1 - player_score
        return player_score

    if who == "enemy":
        enemy_score = 0
        for ship in ships_undamaged:
            enemy_score = enemy_score + player[ship]["cells_left"]
        enemy_score = 4 + 3 + 3 + 2 + 2 + 2 + 1 + 1 + 1 + 1 - enemy_score
        return enemy_score


def enemy_hit():
    """ Function processing enemy's turns """
    while True:
        # OPTION #0 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if len(target_data["found_coordinates"]) == 0:
            x = random.randint(0, 9)
            y = random.randint(0, 9)

            if [x, y] in enemy_hits:
                continue  # go back to get new coordinates
            else:
                enemy_hits.append([x, y])

            pcell = player_field_secret[y][x]

            if pcell == "w":
                player_field_secret[y][x] = "x"
                target_data["directions"] = []
                print(f"Enemy's missed at [{x},{y}].")
                break

            elif pcell in ships_undamaged:
                player[pcell]['cells_left'] = player[pcell]['cells_left'] - 1  # - 1 life

                if player[pcell]['cells_left'] > 0:
                    target_data["found_coordinates"].append([x, y])

                    print(f"Enemy hits at [{x},{y}]! Next chance for enemy. ", end="")
                    player_field_secret[y][x] = f"{player_field_secret[y][x]}'"  # a becomes a'
                    continue

                if player[pcell]['cells_left'] <= 0:
                    print(f"Enemy hits at [{x},{y}]! Your ship sunks! Next chance for enemy. ", end="")
                    target_data["directions"] = []
                    target_data["found_coordinates"] = []
                    target_data["start_from"] = []
                    for point in player[pcell]['ship_areola']:
                        enemy_hits.append(point)
                    player_field_secret[y][x] = f"{player_field_secret[y][x]}'"  # a becomes a'
                    if check_score("enemy") >= 20:
                        print(f"\nGAME OVER. Enemy wins getting {check_score('enemy')} points.")
                        sys.exit()
                    continue
        # OPTION #1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif len(target_data["found_coordinates"]) == 1:  # calculating possible directions for attack
            cell = target_data["found_coordinates"][0]  # first hit cell
            ly = cell[1]
            lx = cell[0]

            pu = [lx, ly - 1]
            pd = [lx, ly + 1]
            pl = [lx - 1, ly]
            pr = [lx + 1, ly]

            if pu[1] in range(0, 10):
                if player_field_secret[pu[1]][pu[0]] != "x":
                    target_data["directions"].append("up")
                else:
                    pass
            else:
                pass

            if pd[1] in range(0, 10):
                if player_field_secret[pd[1]][pd[0]] != "x":
                    target_data["directions"].append("down")
                else:
                    pass
            else:
                pass

            if pl[0] in range(0, 10):
                if player_field_secret[pl[1]][pl[0]] != "x":
                    target_data["directions"].append("left")
                else:
                    pass
            else:
                pass

            if pr[0] in range(0, 10):
                if player_field_secret[pr[1]][pr[0]] != "x":
                    target_data["directions"].append("right")
                else:
                    pass
            else:
                pass

            choice = random.choice(target_data["directions"])  # randomly choosing direction to hit

            if choice == "up":
                p = pu
                if "down" in target_data["directions"]:  # finding complimentary direction
                    compl = "down"
                else:
                    compl = ""

            elif choice == "down":
                p = pd
                if "up" in target_data["directions"]:  # finding complimentary direction
                    compl = "up"
                else:
                    compl = ""

            elif choice == "left":
                p = pl
                if "right" in target_data["directions"]:  # finding complimentary direction
                    compl = "right"
                else:
                    compl = ""

            elif choice == "right":
                p = pr
                if "left" in target_data["directions"]:  # finding complimentary direction
                    compl = "left"
                else:
                    compl = ""

            pcell = player_field_secret[p[1]][p[0]]
            enemy_hits.append(p)

            if pcell == "w":  # miss
                player_field_secret[p[1]][p[0]] = "x"
                target_data["directions"] = []
                print(f"Enemy misses at [{p[0]},{p[1]}]!")  # direction wasn't removed as it will be recalculated anyway
                break

            if pcell in ships_undamaged:  # player's ship hit
                player[pcell]['cells_left'] = player[pcell]['cells_left'] - 1  # minus 1 life

                if player[pcell]['cells_left'] > 0:
                    print(f"Enemy hits at [{p[0]},{p[1]}]! Next chance for enemy. ", end="")
                    target_data["directions"] = []

                    target_data["directions"].append(choice)
                    if compl != "":
                        target_data["directions"].append(compl)
                    target_data["found_coordinates"].append(p)
                    player_field_secret[p[1]][p[0]] = f"{player_field_secret[p[1]][p[0]]}'"  # a becomes a'
                    continue

                if player[pcell]['cells_left'] <= 0:
                    print(f"Enemy hits at [{p[0]},{p[1]}]! Your ship sunks! Next chance for enemy. ", end="")
                    target_data["directions"] = []
                    target_data["found_coordinates"] = []
                    target_data["start_from"] = []
                    for point in player[pcell]['ship_areola']:
                        enemy_hits.append(point)

                    player_field_secret[p[1]][p[0]] = f"{player_field_secret[p[1]][p[0]]}'"  # a becomes a'
                    if check_score("enemy") >= 20:
                        print(f"\nGAME OVER. Enemy wins getting {check_score('enemy')} points.")
                        sys.exit()
                    continue
        # OPTION #2 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif len(target_data["found_coordinates"]) > 1 and len(target_data["start_from"]) == 0:
            choice = target_data["directions"][0]  # last successful direction
            cell = target_data["found_coordinates"][-1]  # last hit cell
            ly = cell[1]
            lx = cell[0]

            pu = [lx, ly - 1]
            pd = [lx, ly + 1]
            pl = [lx - 1, ly]
            pr = [lx + 1, ly]

            if choice == "up":
                p = pu
            elif choice == "down":
                p = pd
            elif choice == "left":
                p = pl
            elif choice == "right":
                p = pr

            pcell = player_field_secret[p[1]][p[0]]

            enemy_hits.append(p)

            if pcell == "w":  # miss
                player_field_secret[p[1]][p[0]] = "x"
                print(f"Enemy misses at [{p[0]},{p[1]}]!")
                target_data['directions'].remove(choice)  # remove wrong direction
                target_data["start_from"] = target_data["found_coordinates"][0]  # changing direction and starting
                # from 1 point
                break

            if pcell in ships_undamaged:  # player's ship hit
                player[pcell]['cells_left'] = player[pcell]['cells_left'] - 1  # minus 1 life

                if player[pcell]['cells_left'] > 0:
                    print(f"Enemy hits at [{p[0]},{p[1]}]! Next chance for enemy. ", end="")
                    target_data["found_coordinates"].append(p)
                    player_field_secret[p[1]][p[0]] = f"{player_field_secret[p[1]][p[0]]}'"  # a becomes a'
                    continue

                if player[pcell]['cells_left'] <= 0:
                    print(f"Enemy hits at [{p[0]},{p[1]}]! Your ship sunks! Next chance for enemy. ", end="")
                    target_data["directions"] = []
                    target_data["found_coordinates"] = []
                    target_data["start_from"] = []
                    for point in player[pcell]['ship_areola']:
                        enemy_hits.append(point)

                    player_field_secret[p[1]][p[0]] = f"{player_field_secret[p[1]][p[0]]}'"  # a becomes a'
                    if check_score("enemy") >= 20:
                        print(f"\nGAME OVER. Enemy wins getting {check_score('enemy')} points.")
                        sys.exit()

                    continue
                    # OPTION #3 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif len(target_data["found_coordinates"]) > 1 and len(target_data["start_from"]) > 0:
            choice = target_data["directions"][0]
            cell = target_data["start_from"]

            ly = cell[1]
            lx = cell[0]

            pu = [lx, ly - 1]
            pd = [lx, ly + 1]
            pl = [lx - 1, ly]
            pr = [lx + 1, ly]

            if choice == "up":
                p = pu

            elif choice == "down":
                p = pd

            elif choice == "left":
                p = pl

            elif choice == "right":
                p = pr

            """print(f"STEP4:DIR -{target_data['directions']}, CHOSEN - '{choice}',"
                  f" PREV - {target_data['found_coordinates'][-1]}, TO HIT {p}")  # DELETE"""

            pcell = player_field_secret[p[1]][p[0]]
            enemy_hits.append(p)

            if pcell == "w":  # miss
                player_field_secret[p[1]][p[0]] = x
                print("CHECK STRANGE!")
                break

            if pcell in ships_undamaged:  # player's ship hit
                player[pcell]['cells_left'] = player[pcell]['cells_left'] - 1

                if player[pcell]['cells_left'] > 0:
                    print(f"Enemy hits at [{p[0]},{p[1]}]! Next chance for enemy. ", end="")
                    target_data["found_coordinates"].append(p)
                    player_field_secret[p[1]][p[0]] = f"{player_field_secret[p[1]][p[0]]}'"  # a becomes a'
                    continue

                if player[pcell]['cells_left'] <= 0:
                    print(f"Enemy hits at [{p[0]},{p[1]}]! Your ship sunks! Next chance for enemy. ", end="")
                    target_data["directions"] = []
                    target_data["found_coordinates"] = []
                    target_data["start_from"] = []
                    for point in player[pcell]['ship_areola']:
                        enemy_hits.append(point)

                    player_field_secret[p[1]][p[0]] = f"{player_field_secret[p[1]][p[0]]}'"  # a becomes a'
                    if check_score("enemy") >= 20:
                        print(f"\nGAME OVER. Enemy wins getting {check_score('enemy')} points.")
                        sys.exit()
                    continue


while True:  # game's main loop

    print("\nBattleship, by Dmytro Ievdokymov yedmitry@gmail.com who started to learn Phyton less than 2 months ago")
    input("\nPress 'Enter' to begin...")

    for key, value in ships_.items():
        place_ship(value, player_field_secret, key)
        place_ship(value, enemy_field_secret, key)

    print("\nAll the ships arrived to the battlefield!")
    display_fields_(player_field_open, enemy_field_open)

    n = 0
    while True:
        n += 1
        print(f"Round #{n}")

        player_hit()
        if check_score("player") >= 20:
            print("\nGAME OVER. You won!")
            sys.exit()

        enemy_hit()
        if check_score("enemy") >= 20:
            print(f"\nGAME OVER. Enemy wins getting {check_score('enemy')} points.")
            sys.exit()
        display_fields_(player_field_open, enemy_field_open)

