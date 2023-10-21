from urllib.request import urlopen

print("NandyDarkEye")
print("Created by Arbaz")

print("https://github.com/arbazfareed")
print()

target = input("Enter The IP Here...It Can Be IPv4 Or IPv6 :\033[1;32m ")
url = "http://ip-api.com/json/" + target
data = urlopen(url).read().decode("utf-8")
data2 = eval(data)

print("\033[1;36m[ # ] \033[1;32mHERE WE GO!! >>>\033[0m")
print()

# Check if the 'as' key exists in the data before trying to access it.
if "as" in data2:
    print("\033[1;36m[ $ ] \033[0mAS:\033[1;32m ", str(data2["as"]))
else:
    print("AS information not available for this IP.")

# Check and print other fields in a similar manner.
if "country" in data2:
    print("\033[1;36m[ $ ] \033[0mCOUNTRY:\033[1;32m ", str(data2["country"]))
else:
    print("Country information not available for this IP.")

if "city" in data2:
    print("\033[1;36m[ $ ] \033[0mCITY:\033[1;32m ", str(data2["city"]))
else:
    print("City information not available for this IP.")

# Add similar checks for other fields...

print("\033[1;36m[ $ ] \033[0mSAY THANKS TO NANDYDARK FOR MAKING THIS TOOL\033[0m")

