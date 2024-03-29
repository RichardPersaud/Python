# # importing subprocess 
# import subprocess 

# # getting meta data of the wifi network 
# meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']) 

# # decoding meta data from byte to string 
# data = meta_data.decode('utf-8', errors ="backslashreplace") 

# # spliting data by line by line 
# # string to list 
# data = data.split('\n') 

# # creating a list of wifi names 
# names = [] 

# # traverse the list 
# for i in data: 
	
# 	# find "All User Profile" in each item 
# 	# as this item will have the wifi name 
# 	if "All User Profile" in i : 
		
# 		# if found split the item 
# 		# in order to get only the name 
# 		i = i.split(":") 
		
# 		# item at index 1 will be the wifi name 
# 		i = i[1] 
		
# 		# formatting the name 
# 		# first and last chracter is use less 
# 		i = i[1:-1] 
		
# 		# appending the wifi name in the list 
# 		names.append(i) 

# # printing the wifi names 
# print("All wifi that system has connected to are ") 
# print("-----------------------------------------") 
# for name in names: 
# 	print(name) 


# -----------------------------------------------------------------------------
# import subprocess

# results = subprocess.check_output(["netsh", "wlan", "show", "network"])
# results = results.decode("ascii")
# results = results.replace("\r","")
# ls = results.split("\n")
# ls = ls[4:]
# ssids = []
# x = 0
# while x < len(ls):
#     if x % 5 == 0:
#         ssids.append(ls[x])
#     x += 1
# print(ssids)

# ====================================================================================


# # Import modules
# import subprocess
# import ipaddress

# # Prompt the user to input a network address
# net_addr = input("Enter a network address in CIDR format(ex.192.168.1.0/24): ")

# # Create the network
# ip_net = ipaddress.ip_network(net_addr)

# # Get all hosts on that network
# all_hosts = list(ip_net.hosts())

# # Configure subprocess to hide the console window
# info = subprocess.STARTUPINFO()
# info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
# info.wShowWindow = subprocess.SW_HIDE

# # For each IP address in the subnet, 
# # run the ping command with subprocess.popen interface
# for i in range(len(all_hosts)):
#     output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
#     if "Destination host unreachable" in output.decode('utf-8'):
#         print(str(all_hosts[i]), "is Offline")
#     elif "Request timed out" in output.decode('utf-8'):
#         print(str(all_hosts[i]), "is Offline")
#     else:
#         print(str(all_hosts[i]), "is Online")
# ================================================================================================




# import os

# result =os.system('ping 192.168.0.15')

# if(result):
#     print('connected!')
# else:
#     print('no connection...')



# =========================
import subprocess 
  
for ping in range(1,20): 
    address = "192.168.0." + str(ping) 
    res = subprocess.call(['ping', address]) 
    if res == 0: 
        print( "ping to", address, "OK")
        print(res)
    else:
        print(res)
    # elif res == 2: 
    #     print("no response from", address) 
    # else: 
    #     print("ping to", address, "failed!") 