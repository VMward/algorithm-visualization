'''
    Check if two strings are anagrams of one another
'''
def isAnagram(s: str, t: str) -> bool:
    return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')

'''
    On an infinite plane, a robot initially stands at (0, 0) and faces north. 
    The robot can receive one of three instructions:
        "G": go straight 1 unit;
        "L": turn 90 degrees to the left;
        "R": turn 90 degrees to the right.
    The robot performs the instructions given in order, and repeats them forever.
    
    Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''
def isRobotBounded(instructions: str) -> bool:
    x, y, dx, dy = 0, 0, 0, 1
    for i in instructions:
        if i == 'R': dx, dy = dy, -dx
        if i == 'L': dx, dy = -dy, dx
        if i == 'G': x, y = x + dx, y + dy
    return (x, y) == (0, 0) or (dx, dy) != (0, 1)

def multOverflowStrings(num1: str, num2: str) -> str:
    pass

'''
    TODO: Left and right balance + variants
'''
def balanceParentheses():
    pass