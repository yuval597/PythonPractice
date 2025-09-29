servers = []
for i in range(3):
    inputA = input('Enter server names \n')
    servers.append(inputA)
    
print(f"The servers are = {servers}")

server_ips = {}
for server in servers:
    ip = input(f"enter your ip adress for {server}\n")
    server_ips[server] = ip 

print("\nServer IP:")
for server, ip in server_ips.items():
    print(f"{server} : {ip}")

var = input("Enter server name here\n")
if var in server_ips:
    print(f"The IP address of {var} is {server_ips[var]}")
else:
    print("Server not found")

change_ip = input("Do you want to change any IP address? (yes/no)\n")
if change_ip.lower() != 'no':
    server_to_change = input("Enter the server name whose IP you want to change:\n")
    if server_to_change in server_ips:
        new_ip = input(f"Enter the new IP address for {server_to_change}:\n")
        server_ips[server_to_change] = new_ip
        print(f"IP address for {server_to_change} has been updated to {new_ip}.")
        print(f"Updated configuartions {server_ips}")

del_server = input("Do you wanna delete any server? (yes/no)\n")
if del_server.lower() == 'yes':
    server_to_delete = input("Enter the server name you want to delete:\n")
    if server_to_delete in server_ips:
        del server_ips[server_to_delete]
        print(f"{server_to_delete} has been deleted.")
    else:
        print("Server not found.")

print("The updated configuration is:")
for server, ip in server_ips.items():
    print(f"{server} -> {ip}")