# Repetitive-Sentence-Filling-in-Every-Language
A tiny script, written in every language.


In python it looks like this:
```python
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
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~%s: \n%s\n"% (entry, comment.replace("<*>", student)))
    uinput("Press Enter to continue...")

print("That's it folks!")
```

the aim of this repository is to host this script in every programming language we can think of.

## The Rules:

* Console applications only.
* The Strings which are hardcoded in the above example most remain the same.

Happy Coding
