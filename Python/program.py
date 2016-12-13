import sys

def uinput(text = ""):
    majorVersion = sys.version.split(".")[0]
    if majorVersion == "3":
        return input(text)
    else:
        return raw_input(text)

print("To get started please enter a comma seperated list of the data to insert. e.g. Steve, Jim, King John IIV")
data = uinput("Please enter the list: ")
print("Now please enter the sentence to fill in, inserting a <*> where the previously entered data should go")
comment = uinput("Please enter the comment: ")

if ", " in data:
    data_list = data.split(", ")
else:
    data_list = data.split(",")

for entry in data_list:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~%s: \n%s\n"% (entry, comment.replace("<*>", entry)))
    uinput("Press Enter to continue...")

print("That's it folks!")
