#The function of the program that would print the variables fed to it
def cheeseAndCrackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d boxes of crackers!" %boxes_of_crackers
    print "Man that's enough for a party"
    print "Get a blanket.\n"


#First try to fetching variables into the function by giving it numbers directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)  #variables fetched

# by fetching variables from a script
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# and then feeding them to the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#Doing math insid the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# Why not both
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

