"""
1108. Defanging an IP Address
-----------------------------

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
---------
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
----------
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""


def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    defanged_IP = ""
    for i in address:
        if i == ".":
            defanged_IP += "[.]"
        else:
            defanged_IP += i
    return defanged_IP


Address = input()
print(defangIPaddr(Address))
