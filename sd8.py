formatter = "{} {} {} {} {}"
#here a variable formatter is defined using 5 empty dictionary
print(formatter.format(1, 2, 3, 4, 5))
print(formatter.format("one", "two", "three", "four", "five"))
print(formatter.format(True, False,False, True, True))
#using command .format() required values and strings are assigned to each empty dictionary
print(formatter.format(formatter, formatter, formatter, formatter, formatter))
#in this each formatter is assigned with another formatter.Thus each 5 formatter is replaced with 5 formatters.ie; totally 25 empty dictionaries.
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear",
	"Or a slogan"
))
print(formatter.format(formatter*2, formatter*2, formatter*2, formatter*2, formatter*2))
