"""
A modified Kaprekar number is a positive whole number with a special property.
If you square it, then split the number into two integers and sum those integers, you have the same
value you started with.
Consider a positive whole number n with d digits. We square n to arrive at a number that is either
2 x d digits long or (2 x d) - 1
digits long. Split the string representation of the square into two parts, l and r.
The right hand part, r must be d digits long. The left is the remaining substring.
Convert those two substrings back to integers, add them and see if you get n.

Example
-------
n = 5
d = 1
First calculate that n^2 = 25. Split that into two strings and convert them back to integers 2 and 5. Test 2 + 5 = 7 is != 5, so this is not a
modified Kaprekar number. If n = 9, still d = 1, and n^2 = 81. This gives us 1 + 8  = 9, the original n.

Note: r may have leading zeros.
-----

Here's an explanation from Wikipedia about the ORIGINAL Kaprekar Number (spot the difference!):

In mathematics, a Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can
be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 45^2 = 2025 and
20+25 = 45. """


def kaprekarNumbers(p, q):  # find the kaprekar numbers in between this two values
    # Write your code here
    result = []
    for i in range(p, q + 1):
        if i == 1:
            result.append(i)
        # elif i == 9 or i == 99 or i == 999 or i == 9999 or i == 99999:
        #     result.append(i)
        #     continue
        square = str(i ** 2)
        length = len(str(i))
        ans = 0
        if 2 * length == len(square):
            ans += (int(square[0:length]) + int(square[length:]))
            if ans == i:
                result.append(i)
        elif length > 1 and 2 * length != len(square):
            ans += (int(square[0:(length - 1)]) + int(square[(length - 1):]))
            if ans == i:
                result.append(i)
    if result:
        for i in result:
            print(i, end=" ")
    else:
        print("INVALID RANGE")


first_multiple_input = input().rstrip().split()
lower_limit = int(first_multiple_input[0])
upper_limit = int(first_multiple_input[1])
print(kaprekarNumbers(lower_limit, upper_limit))
