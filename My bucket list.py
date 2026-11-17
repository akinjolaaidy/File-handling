file =open("My bucket list.txt", "w")
file.write("1. Travel to Japan\n")
file.write("2. Learn to play the guitar\n")
file.write("3. Code my own game\n")
file.close()
print("My bucket list has been created and saved to 'My bucket list.txt'.")


file = open("My bucket list.txt", "r")
content = file.read()
print("\n=== My Bucket list ===")
print(content)
file.close()

file = open("My bucket list.txt" , "r")
lines = file.readlines()
print(f"You have {len(lines)} items in your bucket list.")
file.close()

file = open("My bucket list.txt", "a")
file.write("4. Travel to Japan\n")
file.write("5. Run a 5K marathon\n")
file.close()
print("\n2 more items added!")


file = open("My bucket list.txt", "r")
print("\n=== Updated Bucket List ===")
print(file.read())
file.close()
