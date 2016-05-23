# deadfish-python

An implementation of [Deadfish](http://esolangs.org/wiki/Deadfish), an esoteric programming language, in Python.

## Commands included

All the commands in the original Deadfish are included:

| Command | Action    |
|:--------|----------:|
| `i`     | Increment |
| `d`     | Decrement |
| `s`     | Square    |
| `o`     | Output    |

There are also commands in the xkcd variation:

| Command | Action    |
|:--------|----------:|
| `x`     | Increment |
| `k`     | Square    |
| `c`     | Output    |
| `d`     | Decrement |

There is also the non-standard command `h`, which halts the program.

## Use as a module

Importing this module gives access to the following functions:

** `init()` **  
Initilises the interpreter.

** `runcmd(cmd)` **  
Interprets the character `cmd` as a command. Returns `False` for the halt command, `True` otherwise.

** `runprog(prog)` **
Interprets the string `prog` as a program. Returns `False` if the program encountered the halt command, `True` otherwise.
