# Variable/Input

print "Please enter a thing, it can be anything."
thing = raw_input()
if thing == "":
        thing = "iPhone"

print "Please enter an adjective."
adjective = raw_input()
if adjective == "":
        adjective = "on roam"

print "Please enter an accessory."
accessory = raw_input()
if accessory == "":
    accessory = "case"

print "Please enter a noun."
display = raw_input()
if display == "":
    display = "face"

print "Please enter an emotion."
emotion = raw_input()
if emotion == "":
    emotion = "lighted"

print "Please enter any type of action."
action = raw_input()
if action == "":
    action = "ring"

print "Please enter another adjective."
spin = raw_input()
if spin == "":
    spin = "rotate"

print "Please enter another noun."
screen = raw_input()
if screen == "":
    screen = "display"

print "Please enter a type of emoji."
icon = raw_input()
if icon == "":
    icon = "emoji"

# Poem
print("I'm a little " + thing + ",")
print("Short and " + adjective + ",")
print("Here is my " + accessory + ",")
print("Here is my " + display + ",")
print("When I get all " + emotion + ",")
print("Hear me " + action + ",")
print("Tip me over and " + spin + " " + screen + ",")
print("Here's an " + icon + " of what I can do,")
print("I can turn my " + accessory + " into a " + display + ",")
print("Tip me over and " + spin + " " + screen + ".")
