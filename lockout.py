# Store the correct password in a variable at the top of the file, and set a maximum number of attempts to 3.
# Use a while loop that keeps prompting for the password while attempts remain. Count the attempts with a counter variable.
# When the password is correct, report access granted and use break to leave the loop immediately — do not use up the remaining attempts.
# When it is wrong, tell the user how many attempts remain. After the last one, do not offer another.
# After the loop, report either ACCESS GRANTED with the number of attempts used, or ACCOUNT LOCKED with the number of failures.
# If access was granted, use a second loop — a for loop over the characters of the password — to count how many digits it contains, and print that alongside its length.

CORRECT_PASSWORD = "PASSWORD0!"
MAX_ATTEMPTS = 3

counter = 0
password_success = False

while counter < MAX_ATTEMPTS:

    counter = counter +1
    password = input("Please enter your password: ")

    #checks password
    if password == CORRECT_PASSWORD:
        print("ACCESS GRANTED")
        password_success = True
        break

    else:
        print("Access denied!" , MAX_ATTEMPTS - counter, "attempt(s) remaining.")

if password_success:
    print("Access Granted:", counter)

    digits = 0

    for char in password:
        if char in "0123456789":
            digits = digits + 1

    print("Password length:", len(password) , "Number of digits:", digits)

else:
    print("ACCOUNT LOCKED: ", counter)

print("End of program.")
