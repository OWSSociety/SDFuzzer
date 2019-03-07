# Import the socket
import socket

# Make array
with open("sdlist.txt") as f:
    sd_array = f.read().splitlines() 

# Welcome message:

# Welcome message:
print("")      
print("")                                                                     
print("   ▄██████▄   ▄█     █▄     ▄████████         ▄████████  ▄██████▄   ▄████████  ▄█     ▄████████     ███     ▄██   ▄   ")
print("  ███    ███ ███     ███   ███    ███        ███    ███ ███    ███ ███    ███ ███    ███    ███ ▀█████████▄ ███   ██▄")
print("  ███    ███ ███     ███   ███    █▀         ███    █▀  ███    ███ ███    █▀  ███▌   ███    █▀     ▀███▀▀██ ███▄▄▄███ ")
print("  ███    ███ ███     ███   ███               ███        ███    ███ ███        ███▌  ▄███▄▄▄         ███   ▀ ▀▀▀▀▀▀███ ")
print("  ███    ███ ███     ███ ▀███████████      ▀███████████ ███    ███ ███        ███▌ ▀▀███▀▀▀         ███     ▄██   ███ ")
print("  ███    ███ ███     ███          ███               ███ ███    ███ ███    █▄  ███    ███    █▄      ███     ███   ███ ")
print("  ███    ███ ███ ▄█▄ ███    ▄█    ███         ▄█    ███ ███    ███ ███    ███ ███    ███    ███     ███     ███   ███ ")
print("   ▀██████▀   ▀███▀███▀   ▄████████▀        ▄████████▀   ▀██████▀  ████████▀  █▀     ██████████    ▄████▀    ▀█████▀  ")
print(" ")                                                                                    
print("                                    SDFuzzer coded by OWSSociety | Galletita Oreo")      
print("                                      Visit: https://www.github.com/owssociety/")
print("")                                                                              
                                                                               
# Instructions
print("[SDFuzzer] Please, enter a target without using subdomain (example: google.com)")

# Get value
ip_value = input("[SDFuzzer] Target >> ")

# Empty line
print(" ")  

for t_founded in sd_array:
    try:
       results = str(t_founded) + "." + str(ip_value)
       ip_result = socket.gethostbyname(str(results))
       new_result = "[SDFuzzer] New result >> " + str(t_founded) + "." + str(ip_value) + " << IP >> " + str(ip_result)
       print (new_result)

    except IOError:
            pass