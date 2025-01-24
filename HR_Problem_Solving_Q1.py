def decryptPassword(s):
    # Convert the string into a list for easier manipulation
    w = list(s)
    i = 0

    while i < len(w):
        # Case 1: If the character is a digit
        if w[i].isdigit():
            j = len(w) - 1
            flag = False
            while j >= 0:
                if w[j] == '0':
                    w[j] = w[i]  # Replace '0' with the current digit
                    w.pop(i)  # Remove the digit from its original position
                    flag = True
                    break
                j -= 1

            if flag:
                # If we modified the list, move on to the next character
                continue

        # Case 2: If the character is an uppercase letter followed by a lowercase letter
        elif i + 1 < len(w) and w[i].isupper() and w[i + 1].islower():
            # Swap the uppercase and lowercase letters
            w[i], w[i + 1] = w[i + 1], w[i]
            # Remove the next character after the swap
            w.pop(i + 2)
            # Skip to the next valid character after the swap
            i += 2
            continue

        # Move to the next character if no changes were made
        i += 1

    # Return the modified string
    return ''.join(w)


# Input the password string
s = input("Enter the password to decrypt: ")
result = decryptPassword(s)
print("Decrypted password:", result)
