import pandas as pd
import subprocess

# Read lines from file
with open("gistfile1.txt", "r") as ip_file:
    ip_list = ip_file.readlines()[4:-6]

# Initialize an empty list to collect parsed data
data = []

# Parse each line and collect data
for line in ip_list:
    line = line.strip()
    # Skip lines that start with '#'
    if line.startswith('#'):
        continue
    
    parts = line.split(" ")

    if len(parts) == 2:
        key = parts[0].strip()
        value = parts[1].strip()
        data.append({'Keys': key, 'Values': value})
    else:
        print("Ignoring line:", line)

# Create DataFrame
ip_df = pd.DataFrame(data, columns=["Keys", "Values"])

# Print DataFrame
print(ip_df)



# Get the IP address of github.com from the 'data' dictionary
# import subprocess

# List of IP addresses to ping
ip_addresses = ip_df.iloc[:, 1]

responses =[]

for ip_address in ip_addresses:
    # Run the ping command using 'subprocess' with 'sudo'
    command = f"sudo /sbin/ping -c 4 {ip_address}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    output, _ = process.communicate()
    print(f"Ping result for {ip_address}:")
    print(output.decode('utf-8'))

    # Check if there is output from the ping command
    if "0 packets received" in output.decode('utf-8'):
        has_response = "No"
        print(f"No response from {ip_address}")
    else:
        has_response = "Yes"
        print(f"Received response from {ip_address}")

    responses.append({'Values': ip_address, 'Keys': has_response})

result_df = pd.DataFrame(responses, columns=["Values", "Keys"])
print(result_df)