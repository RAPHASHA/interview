import json


class readTweets:

    @staticmethod
    def readData(dataread):
        data = json.loads(dataread)

        someData = "Kyle's Time line: "

        someData = someData + "\n"
        for kile in data['Kyle']:
            someData = someData + " status " + kile['status'] + " time " + kile['time'] + "\n"
        someData = someData + "\n"

        someData = someData + "Franc's timeline: \n"
        for frank in data['Franc']:
            someData = someData + " status " + frank['status'] + " time " + frank['time'] + "\n"
        someData = someData + "\n"

        someData = someData + "Richard's timeline\n"
        for kile in data['Richard']:
            someData = someData + " status " + kile['status'] + " time " + kile['time'] + "\n"
        someData = someData + "\n"

        return someData