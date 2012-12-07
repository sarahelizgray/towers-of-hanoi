# -*- coding: utf-8 -*-
# Sarah Gray
# Towers of Hanoi
# python version 2.7

import random
import copy


def int_to_base_two(number):
    '''Returns a binary array. The number argument is a positive integer.
This method converts number to base two as a list of
integers in reverse order. For example, int_to_base_two(6) = [0, 1, 1]. '''

    power_of_two = 0
    binary_array = []

    while number > 0:
        remainder = number % 2
        number = int(number / 2)
        if remainder != 0:
            binary_array.append(1)
        else:
            binary_array.append(0)

        power_of_two += 1

    return binary_array


def rand_location_rollcall(puzzle_size):
    '''Returns a location (in rollcall format) within a Hanoi puzzle of integer
puzzle_size. This is returned as a list of length puzzle_size containing
random digits between 0 and 2 inclusive.'''

    placement =[]
    for i in range(puzzle_size):
        placement.append(random.randint(0,2))
    return placement


def rollcall_to_list(rollcall):
    '''Returns a list of 3 lists, representing the physical Hanoi puzzle.
The integers 1 through R are distributed throughout the three sublists,
and they are stored in increasing order within each sublist. For example,
rollcall = [[1, 3, 5], [2, 4], [6]] represents discs 1, 3, and 5 on the
ﬁrst post,  discs 2 and 4 on the second post, and disc 6 (the largest)
on the last post. Note that disc one is always on the top of some post.'''

    disk_value = len(rollcall)
    post0 = []
    post1 = []
    post2 = []
    for i in range(0, len(rollcall)):
        if rollcall[i] == 0:
            post0.append(disk_value)
        if rollcall[i] == 1:
            post1.append(disk_value)
        if rollcall[i] == 2:
            post2.append(disk_value)
        disk_value -= 1
    post0.reverse()
    post1.reverse()
    post2.reverse()
    return [post0, post1, post2]


def is_legal_move(lists, post_a, post_b):
    '''Returns True if it is legal to move a disc from post a to post b.
The lists is the list-of-lists as described in the rollcall_to_list method.
Returns False if move is illegal. If a==b, this returns True.'''

    if len(lists[post_a]) == 0:
        return False
    if len(lists[post_b]) == 0:
        return True

    if lists[post_a][0] > lists[post_b][0]:
        return False
    if lists[post_a][0] < lists[post_b][0]:
        return True
    if lists[post_a][0] == lists[post_b][0]:
        return True


def make_move(lists, post_a, post_b):
    '''Returns new list-of-lists after a disc has been moved. If it is legal to
move the top disc from post a to post b, this method makes that move happen,
otherwise it does nothing. The actual list structure is changed.
Nothing is explictly returned.'''

    if is_legal_move(lists, post_a, post_b):
         k = lists[post_a].pop(0)
         lists[post_b].append(k)
         lists[post_b].sort()
    return lists


def print_list(L):
    '''This prints the list of lists to the screen in a useful way for game
play. The posts are labeled “1”, “2”, and “3”'''

    #find the length of the longest subarray
    longest = 0
    for i in range(len(L)):
        if len(L[i]) > longest:
            longest = len(L[i])
    matrix = []

    #now put place holders in the empty spaces
    for i in range(len(L)):
        while len(L[i]) < longest:
            L[i].append(-1)

    #now sort those subarrays and
    for i in range(len(L)):
        L[i].sort()

    #make an empty container matrix
    for i in range(longest):
        matrix.append([])

    #now reverse the subarrays
    for i in range(len(L)):
        L[i].reverse()

    #now iterate through the subarrays an populate the matrix accordingly
    for i in range(len(L)):
        for j in range(0, longest):
            ring = L[i][j]
            matrix[j].append(ring)
    matrix.reverse()

    #now make the sub arrays into strings
    new_matrix =[]
    spacing = " " * 3

    for i in range(longest):
        string = ""
        for j in range(len(L)):
            if str(matrix[i][j]) == "-1":
                ring = " "
            else:
                ring = str(matrix[i][j])
            if len(ring) == 2 and j != len(L) - 1:
                string = string + ring + spacing
            elif len(ring) == 2 and j == len(L) - 1:
                string = string + ring
            elif len(ring) < 2 and j != len(L) - 1:
                string = string + " " + ring + spacing
            elif len(ring) < 2 and j == len(L) - 1:
                string = string + " " + ring

        new_matrix.append(string)


    bottom_line = "-" * (2 * len(spacing) + (3 * 2))
    post_markers = ' 1' + spacing + ' 2' + spacing + ' 3'
    new_matrix.append(bottom_line)
    new_matrix.append(post_markers)

	#now print the final matrix
    for i in range(len(new_matrix)):
        print new_matrix[i]


def list_to_rollcall(lists):
    '''This method takes in a list of lists and converts that list into
rollcall format  -- identifying which disc goes on which post in
reverse order. For example,  lists = [[1, 3, 5], [2, 4], [6]] as input
would return [2, 0, 1, 0, 1, 0]'''

    #find total number of discs
    num_discs = 0
    for i in range(len(lists)):
        num_discs += len(lists[i])

    result_list = [None] * num_discs

	#find which post each disk is on and note it in the results_list
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            result_list[lists[i][j] - 1] = i
    result_list.reverse()

    return result_list

def rollcall_to_sierpinski(rollcall):
    '''This method takes in a Hanoi puzzle conﬁguration in rollcall
format and converts it to Sierpinski address format.'''

    if len(rollcall) % 2 == 0:
        start_point = [2, 1, 0]
    else:
        start_point = [0, 1, 2]

    sierpinksi = [None] * len(rollcall)
    for i in range(len(rollcall)):
        for j in range(len(start_point)):
            if rollcall[i] == start_point[j]:
                sierpinksi[i] = j
                current_value = j
                #now swap the start point
                if current_value == 0:
                    swap = start_point[1]
                    start_point[1] = start_point[2]
                    start_point[2] = swap

                elif current_value == 1:
                    swap = start_point[0]
                    start_point[0] = start_point[2]
                    start_point[2] = swap

                elif current_value == 2:
                    swap = start_point[0]
                    start_point[0] = start_point[1]
                    start_point[1] = swap

    return sierpinksi

def sierpinkski_to_rollcall(sierpinski_address):
    '''This method is takes in a Hanoi puzzle configuration in Sierpinski
address format and converts it to rollcall format.'''

    if len(sierpinski_address) % 2 == 0:
        start_point = [2, 1, 0]
    else:
        start_point = [0, 1, 2]

    rollcall = [None] * len(sierpinski_address)
    for i in range(len(sierpinski_address)):

        rollcall [i] = start_point[sierpinski_address[i]]
        current_value = sierpinski_address[i]

        #now swap start point
        if current_value == 0:
            swap = start_point[1]
            start_point[1] = start_point[2]
            start_point[2] = swap

        elif current_value == 1:
            swap = start_point[0]
            start_point[0] = start_point[2]
            start_point[2] = swap

        elif current_value == 2:
            swap = start_point[0]
            start_point[0] = start_point[1]
            start_point[1] = swap

    return rollcall

def sierpinkski_to_ternary(sierpinski_address):
    '''This method takes in a Hanoi puzzle conﬁguration in Sierpinski
address format and returns a ternary address for it.'''

    first = 0
    second = 0
    third = 0
    exp = len(sierpinski_address) - 1

    for i in range(len(sierpinski_address)):
        if sierpinski_address[i] == 0:
            first += 0 * 2 ** exp
            second += 1 * 2 ** exp
            third += 1 * 2 ** exp

        elif sierpinski_address[i] == 1:
            first += 1 * 2 ** exp
            second += 0 * 2 ** exp
            third += 1 * 2 ** exp

        elif sierpinski_address[i] == 2:
            first += 1 * 2 ** exp
            second += 1 * 2 ** exp
            third += 0 * 2 ** exp
        exp = exp - 1
    if 2 ** (len(sierpinski_address) + 1) - 2 == first + second + third:
        return [first, second, third]

def ternary_to_sierpinkski(ternary_address):
    '''This method takes in a Hanoi puzzle configuration in ternary address
format and returns a Sierpinsi address for it.'''

    results = []
    max_len = 0

    #find the base 2 versions of the numbers and max length of each value
    for i in range(len(ternary_address)):
        if max_len < len((int_to_base_two(ternary_address[i]))):
            max_len = len((int_to_base_two(ternary_address[i])))
        results.append(int_to_base_two(ternary_address[i]))

    #now make the arrays all the same length and reverse them
    for j in range(len(ternary_address)):
        while len(results[j]) < max_len:
            results[j].append(0)
        results[j].reverse()

    sierpinski = [None] * max_len

    #now find the zeros!
    for k in range(max_len):
        for l in range(len(ternary_address)):
            if results[l][k] == 0:
                if l == 0:
                    sierpinski[k] = 0
                elif l == 1:
                    sierpinski[k] = 1
                elif l == 2:
                    sierpinski[k] = 2
    return sierpinski


def reduce_ternary(puzzle_a, puzzle_b):
    '''this method takes in two Hanoi puzzle conﬁgurations in ternary address
format and reduces it by “removing” any large dics which are in
common. For example, if the 4 largest discs in both conﬁgurations are in
the same locations, they are irrelevant to the problem. The two inputs
are directly changed, and nothing is explicitly returned by this method.
Thus, the resulting two conﬁgurations will have their largest discs
on two different posts.'''

    if puzzle_a==puzzle_b:
        for i in range(3):
            puzzle_a[i]=0
            puzzle_b[i]=0
        return

    config_a = ternary_to_sierpinkski(puzzle_a)
    config_b = ternary_to_sierpinkski(puzzle_b)

    length = len(config_b)
    for i in range(length):
        if config_a[i] == config_b[i]:
            config_a[i] = -1
            config_b[i] = -1
        else:
            break

    new_config_a = []
    new_config_b = []
    for i in range(length):
        if config_a[i] == -1 and config_b[i] == -1:
            continue
        else:
            new_config_a.append(config_a[i])
            new_config_b.append(config_b[i])

    temp_config_b = sierpinkski_to_ternary(new_config_b)
    temp_config_a = sierpinkski_to_ternary(new_config_a)

    #cheat out python, copy over existing input puzzles with no return
    for i in range(3):
        puzzle_a[i] = temp_config_a[i]
        puzzle_b[i] = temp_config_b[i]


def distance_ternary(a_in,b_in):
    '''Returns the distance between two configuration
-- the goal config and the current config. If
the two inputs are identical, 0 is immediately returned.
Otherwise, the problem is reduced using the reduce_ternary method.'''

    copy_a = []
    copy_b = []
    for i in range(len(a_in)):
            copy_a.append(a_in[i])
            copy_b.append(b_in[i])

    #reduce the distances
    reduce_ternary(copy_a, copy_b)

    #see if the TA's are identical
    for i in range(len(copy_a)):
        if copy_a[i] == copy_b[i] and i == len(copy_a)-1:
            return 0
        elif copy_a[i] == copy_b[i]:
            continue
        else:
            break

    #find the quadrant where each coordinate is located
    location_a = min(copy_a)
    location_b = min(copy_b)
    index_a = 0
    index_b = 0
    for i in range(len(copy_a)):
        if copy_a[i]  == location_a:
            index_a = i
        if copy_b[i] == location_b:
            index_b = i

    #get the size of the puzzle
    puzzle_size = len(ternary_to_sierpinkski(copy_a))

    #now find the distances to the bridges
    dist_a_array = []
    dist_b_array = []

    for i in range(len(copy_a)):
        if i == index_a:
            dist_a_array.append(0)
        else:
            dist_a_array.append(copy_a[i] - 2 ** (puzzle_size - 1))

    for i in range(len(copy_b)):
        if i == index_b:
            dist_b_array.append(0)
        else:
            dist_b_array.append(copy_b[i] - 2 ** (puzzle_size - 1))

    #try using one bridge
    one_bridge = dist_a_array[index_b] + dist_b_array[index_a] + 1

    #figure out which quadrant contains neither the current config or destination
    not_quadrant = 3 - index_a - index_b

    #get two bridge value
    two_bridge = dist_a_array[not_quadrant] + dist_b_array[not_quadrant] + 2 + (2 ** (puzzle_size - 1) - 1)

    #figure out if it is shorter to go over one bridge or two
    if one_bridge < two_bridge:
        return one_bridge
    elif two_bridge < one_bridge:
        return two_bridge
    else:
        return one_bridge


def play(number):
    '''This method plays the game. The number parameter indicates
how many discs will be used in game play.'''

	#make a random, legal distribution of disks
    get_start_values = rand_location_rollcall(number)
    make_tower = rollcall_to_list(get_start_values)

    #set up the ternary address of the end goal
    goal = []
    for i in range(number):
        goal.append(2)
    goal = rollcall_to_sierpinski(goal)
    goal = sierpinkski_to_ternary(goal)


    while True:
        print
        print "###################"
        print "The Towers of Hanoi "
        print "###################"
        print

        #print the tower, but keep a good copy for later use
        print_tower = copy.deepcopy(make_tower)
        print_list(print_tower)
        print

        #get the distance to the goal
        print
        current_config = list_to_rollcall(make_tower)
        current_config = rollcall_to_sierpinski(current_config)
        current_config = sierpinkski_to_ternary(current_config)
        distance = distance_ternary(current_config, goal)
        if distance == 0:
            print "You win!"
            print "Bye, bye!"
            break
        print "Only %s moves to success!" % distance
        print


        #get the user's input
        quit_dialogue = raw_input("Too intimdated are you? Want to quit? If so, type yes.")

        if quit_dialogue.lower() == "yes":
            print
            print "Another opponent defeated by the mighty towers!"
            play = False
            break

        print
        print "Make a Move, Sucka!"
        print
        start_pillar = raw_input("Enter a start pillar: ")
        while start_pillar != "1" and start_pillar != "2" and start_pillar != "3":
            print "Bad pillar choice, try again."
            print
            start_pillar = raw_input("Enter a start pillar: ")
        start_pillar = int(start_pillar)
        print
        dest_pillar = raw_input("Enter a destination pillar: ")
        while dest_pillar != "1" and dest_pillar != "2" and dest_pillar != "3":
            print "Bad pillar choice, try again."
            print
            dest_pillar = raw_input("Enter a destination pillar:")
        dest_pillar = int(dest_pillar)
        print

        #see if it's legal before executing the move
        legal = is_legal_move(make_tower, start_pillar - 1, dest_pillar - 1)
        if legal:
            new_values = make_move(make_tower,start_pillar - 1, dest_pillar - 1)
            make_tower = new_values
        else:
            print
            print"Nice try pal, that's an illegal move!"
            print
