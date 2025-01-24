"""
1678. Goal Parser Interpretation
--------------------------------

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
The interpreted strings are then concatenated in the original order.
Given the string command, return the Goal Parser's interpretation of command.

Example 1:
----------
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Example 2:
----------
Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:
----------
Input: command = "(al)G(al)()()G"
Output: "alGalooG"
"""


def interpret(command):
    """
    :type command: str
    :rtype: str
    """
    result = ""
    command = list(command)
    words = ""
    for i in range(0, len(command)):
        if command[i] == 'G':
            result += command[i]
        else:
            words += command[i]
            if words == "()":
                result += "o"
                words = ""
            elif words == "(al)":
                result += "al"
                words = ""
    return result


String = input()
print(interpret(String))
