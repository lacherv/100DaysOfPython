# Import the functionality of your Operating System
import os 

hostname = "google.com"
# Executing a shell command 
# -c 1 print just one line 
response = os.system("ping -c 1 " + hostname)

# And check the response ...
if response == 0: 
    print(hostname, ' is up!');
else:
    print(hostname, ' is down!')
