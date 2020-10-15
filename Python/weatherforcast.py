import re
import urllib.request
#http://www.weather-forecast.com/locations/Srinagar/forecasts/latest
city = input("Enter your city: ")
url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m = re.search('span class="phrase">', data1)
start = m.end()                                #start is end of the above line (i.e span class="phrase)
end = start + 300
newString = data1[start:end]
m = re.search("</span>", newString)
end = m.start() - 2                            #end of the above line (i.e </span>) is -2 units from the beginning of it.
final = newString[0:end]                       #from start(0,0) to end (mentioned in above line) specific positions
print(final)



#start and end give us specific position of the cursor at time