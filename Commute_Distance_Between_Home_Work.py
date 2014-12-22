import urllib
import json as simplejson
import csv

# This is a function that will use the google api to calculate distance b/w two points on the earth!
# Input to this function are the source antenna ID, the destination antenna ID, source latitude, source longitude, destination latitude and destination longitude.

def calculateDistance(sourceID,destID,sourceLatitude,sourceLongitude,destinationLatitude,destinationLongitude):
	identities = sourceID,destID
	sourceCoordinates = sourceLatitude,sourceLongitude
	destinationCoordinates = destinationLatitude,destinationLongitude
	if sourceID!=destID:
		print "Calculating the distance from " +str(tuple(sourceCoordinates))+ "to " +str(tuple(destinationCoordinates))
		url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(sourceCoordinates),str(destinationCoordinates))
		#print (url)
		result= simplejson.load(urllib.urlopen(url))
		#print result
		if result['rows'][0]['elements'][0]['distance']['value']:
			resulting_distance = (result['rows'][0]['elements'][0]['distance']['value'])/1000
		#print ("The distance from "+ str(tuple(sourceCoordinates))+" to "+ str(tuple(destinationCoordinates))+" is "+resulting_distance)
		return (int(sourceID),int(destID),resulting_distance)

def distForAllPoints():
	
	dataList = []
	cleanList = []
	flattenedList = []
	identity = []
	lat = []
	longi = []
	result = []

	with open('data.tsv','r') as f:
        	reader = csv.reader(f,delimiter='\t')
        	for source in reader:
                	identity.append((source[0]))
                	longi.append(float(source[1]))
                	lat.append(float(source[2]))
                	dataList=zip(identity,longi,lat)

	result=[[calculateDistance(sID,dID,sLa, sLo, dLa, dLo) for (dID,dLo,dLa) in dataList] for (sID,sLo,sLa) in dataList]

	flattened_list = [y for dataList in result for y in dataList]
	cleanList=filter(None,flattened_list)

	with open('output.csv', 'w') as out:
		for t in cleanList:
			out.write(str(t)+",\n")

distForAllPoints()
