import re
import urllib.request
arrayofStocks = ["FB", "GOOG", "DATA", "BABA"]
url = "https://www.google.com/finance?q="    #In google stocks for all the stocks, this link is common in the beginning
stock = input("Enter your stock: ")
url = url + stock                            #This will ad our stock name that we wanna search
data= urllib.request.urlopen(url).read()     #This line requests to open the url(above link + our stock name) and read the data from it
data1 = data.decode("utf-8")                 #This line decodes the data into the language in which page was written in (utf-8) format
m = re.search('meta itemprop="price"', data1) #In google stock page we've to find (meta itemprop="price") here the price of the stock will be mentioned, we're searching this in data1
start = m.start()  #This is a starting variable, in above code we'll get to know about the location of the searched text in data1(page decoded) 
end = start + 50                             #This is end variable aka position 50 char after start
newString = data1[start:end]                 #We create a newString that starts and ends at the conditions provided in above 2 lines
m = re.search('content="', newString)        #We search (content") within newString
start = m.end()                              #starting variable is it's end
newString1 = newString[start:]               #we create a newString1 in which the string starts from the starting variable(start = m.end() ) to so on until the end of string newString
m = re.search("/", newString1)               #now we search for (/) in string newSrting1
start = 0                                    #starting from very beginning
end = m.end()-3                              #end position at -3 unit places from /
final = newString1[0:end]                    #prints newString1 from beginning to end 
print("The value of " + stock.upper() + " is " + final)   