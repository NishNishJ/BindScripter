__author__ = "kenish25"
import pyperclip
import math

# Gets the string from user input
inputFileName = input("Enter your filename(without the .txt):")

inputFile = open(inputFileName + ".txt", "r")

inputStr = inputFile.read()

# Gets rid of all the characters that make things difficult
inputStr = inputStr.replace("\n", " ")
inputStr = inputStr.replace(";", ",")
inputStr = inputStr.replace('"', "'")

print("Your string is '%s'" % inputStr)
# Gets the length of inputStr then finds out the fewest messages you need to say all of it
inputLength = len(inputStr)
inputSections = math.ceil(-(-inputLength // 126) * 1.1)

print("The string is %d characters long which will be approximately %d messages" % (inputLength, inputSections))

i = 0
outputSections = []
for i in range(inputSections):
    outputLength = 0
    # Sets the length of outputLength to the sum of the parts of outputSections
    for z in range(len(outputSections)):
        outputLength += len(outputSections[z])
    print("There are %d characters in outputLength" % outputLength)
    # Checks whether or not you're at the end of the text, if you are then it just adds the rest to inputTemp
    # Otherwise it writes up to the last space from the next 126 characters.
    if inputLength - outputLength < 126:
        inputTemp = inputStr[outputLength:inputLength]
    else:
        inputTemp = inputStr[outputLength:126 + outputLength]
        lastSpace = 126 - inputTemp.rfind(" ")
        inputTemp = inputTemp[:-lastSpace]
    # Write inputTemp to a new index of the list outputSections
    outputSections.append(inputTemp)
    print(inputTemp + "\n")
    print(outputSections)

# Gets rid of whitespace at the ends of messages as well as empty messages

x = 0
for x in range(len(outputSections)):
    outputSections[x] = outputSections[x].rstrip()
    outputSections[x] = outputSections[x].lstrip()
outputSections = list(filter(None, outputSections))
print(outputSections)

bindName = inputFileName
c = 0
preFinal = ["alias %s %s%d \n" % (bindName, bindName, c)]
final = ""
# Writes outputSections into a bind usable in source games
for c in range(len(outputSections)):
    preFinal.append(
        """alias "%s%d" "say %s; alias %s %s%d" \n""" % (bindName, c, outputSections[c], bindName, bindName, c + 1))
print(preFinal)
for v in range(len(preFinal)):
    final += preFinal[v]
final += '''alias "%s" "%s0"''' % (bindName, bindName)
print(final)
# Copies the entire bind to the clipboard
pyperclip.copy(final)
