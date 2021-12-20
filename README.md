# flightradar24
Python Module for fetching flight data (Arrivals &amp; Departures) from an airport code. source: https://www.flightradar24.com

IMPORTANT: Requires selenium & bs4
- pip install selenium
- pip install bs4

IMPORTANT: Requires suitable Chrome webdriver!
- Check your current Chrome version
- Search for chromedriver.exe version XX (e.g. 96)
- Place the exe file in a folder (preferably at root) and create environment PATH to that foder (e.g. C:/webdriver)

This python code is written to only fetch the first 8 arrivals and departures with respect to the time code is called
place this file in the same folder as your code

```py
from flightradar import Schedule 
var = Schedule('AIRPORT CODE') # e.g. Schedule('AXA')
var.arrivals # List of arrivals (len = 8, type = List)
var.arrivals[0] # First arrival, type Dict
#{
#  'time' : time of arrival / departure
#  'flight' : flight code
#  'location' : arrive from / departs to
#  'airline' : company
#  'aircraft' : aircraft
#  'status' : status
#}
var.arrivals[0]['status'] # returns status of the first arrival
var.departures # similar properties as arrivals, but for departures
