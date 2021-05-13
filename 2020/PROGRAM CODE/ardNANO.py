import urllib2
import json
import serial
import time

PORT = "COM5"
ser = serial.Serial(PORT, 9600)
time.sleep(2)
writefile = open('WCData2.txt', 'w')
writefile2 = open('WCData_Keys.csv', 'w')


api_key = "xxx"
url = "http://worldcup.kimonolabs.com/api/players?apikey=" + \
    api_key  # + "&kimlimit=1000"
json_obj = urllib2.urlopen(url)
readable_json = json.load(json_obj)
list_of_attributes = readable_json[0].keys()

print(list_of_attributes)
print("\n")
attributes = raw_input("What attributes would you like to print?")

with writefile as file_output:
    for i in readable_json:
        message = i[str(attributes)].encode('utf-8') + ','
        print(message)
        file_output.write(message)
with writefile2 as file_output2:
    file_output2.write(str(list_of_attributes))

# HERE is where I am trying to set a VAL so the Arduino script sees it's greater than 0 and therefore lights my LED
time.sleep(1.5)
val = "5"
written = ser.write(val)

ser.close()
