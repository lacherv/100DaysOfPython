#*******************************#
# Python code to retrieve TTL   #
# Time on ping command          #
# Created by lacherv            #
#*******************************#
#!/usr/bin/python3

# Import the operating System
import os

#  Function to get the TTL

def get_ttl_from_ping(url):
    command = "ping " + url + " -c 1"
    process = os.popen(command)
    response = str(process.read())
    ttl_begin = response.find('ttl=') + 4
    ttl_end = response.find('time')
    return response[ttl_begin:ttl_end].splitlines()[0]

def get_time_from_ping(url):
    command = "ping " + url + " -c 1"
    process = os.popen(command)
    response = str(process.read())
    time_begin = response.find('time=') + 5
    time_end = response.find('ms')
    return response[time_begin:time_end].splitlines()[0]


print(get_ttl_from_ping('google.com'))
print(get_time_from_ping('google.com'))

