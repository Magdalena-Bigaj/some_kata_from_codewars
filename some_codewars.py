
# https://www.codewars.com/users/Magdalena-code/

############################################################################
# You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given.
# If you reach the end point before all your moves have gone, you should return Finish. If you hit any walls or go
# outside the maze border, you should return Dead. If you find yourself still in the maze after using all the moves,
# you should return Lost.
# The Maze array will look like
# maze = [[1,1,1,1,1,1,1],
#         [1,0,0,0,0,0,3],
#         [1,0,1,0,1,0,1],
#         [0,0,1,0,0,0,1],
#         [1,0,1,0,1,0,1],
#         [1,0,0,0,0,0,1],
#         [1,2,1,0,1,0,1]]
# ..with the following key
# 0 = Safe place to walk
# 1 = Wall
# 2 = Start Point
# 3 = Finish Point
# direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
# Rules
# 1. The Maze array will always be square i.e. N x N but its size and content will alter from test to test.
#
# 2. The start and finish positions will change for the final tests.
#
# 3. The directions array will always be in upper case and will be in the format of N = North, E = East, W = West and S = South.
#
# 4. If you reach the end point before all your moves have gone, you should return Finish.

def maze_runner(maze, directions):
    for x1 in maze:
        for y1 in x1:
            if y1 == 2:
                y = (x1.index(y1))
                x = (maze.index(x1))

    for d in directions:
        if d == "N":
            x -= 1
        elif d == "S":
            x += 1
        elif d == "E":
            y += 1
        else:
            y -= 1
        try:
            if (maze[x][y]) == 3:
                return "Finish"
            if (maze[x][y] == 1) or 0 < x >= len(maze) or 0 < y >= len(maze):
                return "Dead"
            if (maze[x][y]) == 0 and d != directions[-1]:
                pass

        except IndexError:
            return "Dead"
    if (maze[x][y] == 0 or 2) and d == directions[-1]:
        return "Lost"
    print(maze)
    print(directions)


##############################################################################
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
# You will be passed a string and you must return that string in an array where an uppercase letter is
# a person standing up.
# Rules
# 1.  The input string will always be lower case but maybe empty.
# 2.  If the character in the string is whitespace then pass over it as if it was an empty seat
# Example
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(people):
    people = list(people)
    nowa_lista = list()
    x = 0
    for l in people:
        if l.isalpha():
            people[x] = l.upper()
            nowa_lista.append("".join((l) for l in people), )
            people[x] = l.lower()
        else:
            pass
        x += 1
    return (nowa_lista)


##############################################################################

# Background
# In another dimension, there exist two immortal brothers: Solomon and Goromon. As sworn loyal subjects to the time
# elemental, Chronixus, both Solomon and Goromon were granted the power to create temporal folds. By sliding through
# these temporal folds, one can gain entry to parallel dimensions where time moves relatively faster or slower.
#
# Goromon grew dissatisfied and one day betrayed Chronixus by stealing the Temporal Crystal, an artifact used to
# maintain the time continuum. Chronixus summoned Solomon and gave him the task of tracking down Goromon and retrieving
# the Temporal Crystal.
#
# Using a map given to Solomon by Chronixus, you must find Goromon's precise location.
#
# Mission Details
# The map is represented as a 2D array. See the example below:
#
# map_example = [[1,3,5],[2,0,10],[-3,1,4],[4,2,4],[1,1,5],[-3,0,12],[2,1,12],[-2,2,6]]
# Here are what the values of each subarray represent:
#
# Time Dilation: With each additional layer of time dilation entered, time slows by a factor of 2. At layer 0,
# time passes normally. At layer 1, time passes at half the rate of layer 0. At layer 2, time passes at half the rate
# of layer 1, and therefore one quarter the rate of layer 0.
# Directions are as follow: 0 = North, 1 = East, 2 = South, 3 = West
# Distance Traveled: This represents the distance traveled relative to the current time dilation layer. See below:
# The following are equivalent distances (all equal a Standard Distance of 100):
# Layer: 0, Distance: 100
# Layer: 1, Distance: 50
# Layer: 2, Distance: 25
# For the mapExample above:
#
# mapExample[0] -> [1,3,5]
# 1 represents the level shift of time dilation
# 3 represents the direction
# 5 represents the distance traveled relative to the current time dilation layer
#
# Solomon's new location becomes [-10,0]
#
# mapExample[1] -> [2,0,10]
# At this point, Solomon has shifted 2 layers deeper.
# He is now at time dilation layer 3.
# Solomon moves North a Standard Distance of 80.
# Solomon's new location becomes [-10,80]
#
# mapExample[2] -> [-3,1,4]
# At this point, Solomon has shifted out 3 layers.
# He is now at time dilation layer 0.
# Solomon moves East a Standard Distance of 4.
# Solomon's new location becomes [-6,80]
# Your function should return Goromon's [x,y] coordinates.
#
# For mapExample, the correct output is [346,40].
#
# Additional Technical Details
# Inputs are always valid.
# Solomon begins his quest at time dilation level 0, at [x,y] coordinates [0,0].
# Time dilation level at any point will always be 0 or greater.
# Standard Distance is the distance at time dilation level 0.
# For given distance d for each value in the array: d >= 0.
# Do not mutate the input

def solomons_quest(coordinates):
    a = 0
    b = 0
    location = [a, b]
    direction_unpack = {0: 1, 1: 1, 2: -1, 3: -1}
    previous_dilation = 0
    for coordinate in coordinates:
        dilation = coordinate[0]
        direction = coordinate[1]
        distance = coordinate[2]
        distance = distance * 2 ** (dilation + previous_dilation)
        previous_dilation = previous_dilation + dilation
        if direction == 1 or direction == 3:
            a += distance * direction_unpack[direction]
        else:
            b += distance * direction_unpack[direction]
        location = [a, b]
    return location
