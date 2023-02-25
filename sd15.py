from  sys import argv
#argvs are imported
script, filename = argv
#argv is a argument variable. This command unpacks the argv and assign it to all the variables.
txt = open(filename)
#This command is for opening the text file that we enter.
print(f"Here's your file {filename}:")
#A format string used for printing a text line with a variable.
print(txt.read())
#txt.read() this command is used to print all the text lines that is inside the text file we have asked to open.
print("Type the filename again:")
file_again = input("> ")
#Input command to ask the user to enter the file name again.
txt_again = open(file_again)
#again open() command to open the text file.
print(txt_again.read())
txt.close()

