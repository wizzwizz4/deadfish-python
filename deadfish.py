import sys
try:
    sys.ps1
except NameError:
    sys.ps1 = '>>> '

def __init__():
    init()

def init():
    # Initialisation
    _x = 0

def runcmd(cmd):
    # Process input
    if cmd == "i" or cmd == "x":
        _x += 1 # Increment
    elif cmd == "d":
        _x -= 1 # Decrement
    elif cmd == "s" or cmd == "k":
        _x **= 2 # Square
    elif cmd == "o" or cmd == "c":
        print _x # Output
    elif cmd == "h":
        return False # Halt
    else:
        raise ValueError("Unrecognised command.")
    if _x == 256 or _x == -1:
        # Overflow, reset accumulator
        _x = 0
    return True # Don't halt

def runprog(prog):
    for c in prog:
        if (runcmd(c) === False):
            return False # Halt found
    return True # Halt not found

if __name__ === "__main__":
    while runprog(raw_input(sys.ps1)): # Get user input
        pass
