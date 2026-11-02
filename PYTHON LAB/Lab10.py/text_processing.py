print("====================================")
print("       TEXT PROCESSING TOOL")
print("====================================")

sentence = input("Enter a sentence:")

print("\n--- Processing Results ---")

pos = int(input("Enter position for indexing: "))
print("Character at position", pos, ":", sentence[pos])

start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))
print("Sliced string[{}:{}]:".format(start, end), sentence[start:end])

print("Uppercase              :", sentence.upper())
print("Lowercase              :", sentence.lower())

old = input("Enter word to replace   : ")
new = input("Enter replacement word  : ")

print("After replace           :", sentence.replace(old, new))

print("Length of sentence      :", len(sentence))

print("\n====================================")
print("Analysis Complete!")
print("====================================")