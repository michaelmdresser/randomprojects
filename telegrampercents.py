import sys

filename = sys.argv[1]
f = open(filename)
people = {}
finalPeople = []
totalMessages = 0

for line in f:
    if line.find(",") == 19:
        line = line[line.find(",") + 2:]
        colon = line.find(":")
        person = line[:colon]
        message = line[colon + 2:]
        if person not in people.keys():
            people[person] = 1
        else:
            people[person] = people[person] + 1

        totalMessages = totalMessages + 1

for key in people:
    if (len(key) < 30 and "<" not in key and "Gamee" not in key and "I can't wake" not in key and "I'm sure we can" not in key):
        #print(key + ": " + str(float(people[key]) * 100.0 / float(totalMessages))[:5] + " percent")
        finalPeople.append( (key, float(people[key]) * 100.0 / float(totalMessages)))

finalPeople = sorted(finalPeople, key=lambda tup: tup[1], reverse=True)

for entry in finalPeople:
    print(entry[0] + ": " + str(entry[1])[:5] + "%")
