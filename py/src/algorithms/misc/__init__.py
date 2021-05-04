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


def powerfulIntegers( x: int, y: int, bound: int) -> list[int]:
    ret = []
    for i in range(bound):
        for j in range(bound):
            powerful = x**i + y**j
            if powerful > bound: break
            if powerful not in ret: ret.append(powerful)
    return ret


def findMissing(arr, left, right, diff):
    if (right <= left):
        return 10**5
    mid = left + (right - left) // 2

    if (arr[mid + 1] - arr[mid] != diff):
        return (arr[mid] + diff)

    if (mid > 0 and
            arr[mid] - arr[mid - 1] != diff):
        return (arr[mid - 1] + diff)

    if (arr[mid] == arr[0] + mid * diff):
        return findMissing(arr, mid + 1, right, diff)

    return findMissing(arr, left, mid - 1, diff)