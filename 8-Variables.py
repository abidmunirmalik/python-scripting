# Variables in Python
# In Python variables normally defined in lower case with underscore
my_name = "Abid M. Malik."
my_age = 35 # Not my real age
my_height = 74
my_weight = 180
eye_color = "Blue"
hair_color = "Brown"
teeth_color = "White"

print "Let's talk about", my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print("Actually that's not too heavy")
print "He's got %s eyes and %s hair." % (eye_color, hair_color)
print "His teeth are usually %s depending on the coffee." % teeth_color
print "If I add %d, %d, and %d I get %d." % (my_age,my_height,my_weight, my_age + my_height + my_weight)
print "=" * 10
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)
print x
print y
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with the right side."
print w + e
print "=" * 10
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 #what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
print "=" * 10
formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
print "=" * 10
# More Stuff
days   = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months
print """
Ther's something going on here.
With the three double-quotes.
We'll be able to type as much as we lik.
Even 4 lines if we want. or 5. or 6.
"""

# Exercise
first_name = "NAFEESA"
last_name = "ABID"
age = 36
birth_date = "12/02/1982"

print "My name is " + first_name + " " + last_name + "."
print "I was born on " + birth_date + " and I'm " + str(36) + " years old."
# OR
print "My name is %s %s.\nI was born on %s and I'm %d years old." % (first_name,last_name,birth_date,age)
# OR
print("My name is %s %s.\nI was born on %s and I'm %d years old." % (first_name,last_name,birth_date,age))
