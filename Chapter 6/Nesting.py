# Nesting is storing multiple dictionaries in a list or list of items as a value.
# Dictionary can have information about one alien but if you want to have info of a fleet of aliens. you can
# make a list of aliens in which each alien is a dictionary of information about that alien.


rapper_1 = {"Name":"Travi$ Scott",
            "Best rap song":"Wake Up",
            "Best featured song":"Sky walker",
            "Age":"29",
            "website":"www.travisscott.com.au",
            "Children":"Stormi Webster"}

rapper_2 = {"Name":"ASAP Rocky",
            "Best rap song":"Wild for the life",
            "Best featured song":"Ghost town",
            "Age":"28",
            "website":"www.asaprocky.com.au",
            "Children":"Tyler the creator"}
rappers = [rapper_1, rapper_2]

for rapper in rappers:
    print(rapper)

