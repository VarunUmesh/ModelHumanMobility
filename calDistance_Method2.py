import urllib
import json as simplejson
import csv

# This is a function that will use the google api to calculate distance b/w two points on the earth!
# Input to this function are the source antenna ID, the destination antenna ID, source latitude, source longitude, destination latitude and destination longitude.

def calculateDistance(sourceLatitude,sourceLongitude,destinationLatitude,destinationLongitude):
	sourceCoordinates = sourceLatitude,sourceLongitude
	destinationCoordinates = destinationLatitude,destinationLongitude
	print "Calculating the distance from " +str(tuple(sourceCoordinates))+ "to " +str(tuple(destinationCoordinates))
	url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(sourceCoordinates),str(destinationCoordinates))
	#print (url)
	result= simplejson.load(urllib.urlopen(url))
	#print result
	if result['rows'][0]['elements'][0]['distance']['value']:
		resulting_distance = (result['rows'][0]['elements'][0]['distance']['value'])/1000
	#print ("The distance from "+ str(tuple(sourceCoordinates))+" to "+ str(tuple(destinationCoordinates))+" is "+resulting_distance)
		return (resulting_distance)

def distForAllPoints():
	with open('data.tsv','r') as f:
		reader1 = list(csv.reader(f,delimiter='\t'))
	f.close()

	with open('data.tsv','r') as f:
		reader = csv.reader(f,delimiter='\t')
		for source in reader:
			for dest in reader1:
				if source[0]!=dest[0]:
					sourceLati=float(source[2])
					sourceLong=float(source[1])
					destLati=float(dest[2])
					destLong=float(dest[1])
					print("The source id is: " +source[0])
					print("The source long is: " +source[1])
					print("The source lati is: " +source[2])
					print("The dest id is: " +dest[0])
					print("The dest long is: " +dest[1])
					print("The dest lati is: " +dest[2])
					dist=calculateDistance(sourceLati,sourceLong,destLati,destLong)
					writeRes=source[0],dest[0],dist
					with open('NewFile.csv', 'a') as csvFile:
                                                writer=csv.writer(csvFile, delimiter=',',)
						writer.writerows([writeRes])
distForAllPoints()
