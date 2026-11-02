sentence = input("Enter a sentence: ")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

total = len(sentence)
letters = vowels + consonants

if letters > 0:
    percentage = (vowels / letters) * 100
else:
    percentage = 0

print("\n==========================================")
print("       DOCUMENT ANALYSIS REPORT")
print("==========================================")

print("Sentence:", sentence)
print("Total characters:", total)

print("\n--- Character Breakdown ---")
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

print("\n--- Summary ---")
print("Total letters:", letters)
print("Vowel percentage: {:.1f}%".format(percentage))

print("\n==========================================")
print("Analysis Complete!")
print("==========================================")