username = input("Enter your username: ")
password = input("Enter your password: ")

length = len(password) >= 8
digit = any(ch.isdigit() for ch in password)
uppercase = any(ch.isupper() for ch in password)

print("\n========================================")
print("       PASSWORD VALIDATION REPORT")
print("========================================")

print("Username:", username)
print("Password:", "*" * len(password))

print("\n--- Validation Rules ---")

if length:
    print("[PASS] Minimum 8 characters ({} characters)".format(len(password)))
else:
    print("[FAIL] Minimum 8 characters")

if digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if uppercase:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print("\n--- Result ---")

if length and digit and uppercase:
    print("Password is VALID!")
    print("Account created successfully for", username + "!")
else:
    print("Password is INVALID.")

print("\n========================================")
