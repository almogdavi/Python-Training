print("task number 1")

servers = ["nginx", "docker", "kubernetes"]
for server in servers:
    print("the server now is:" ,server)

print("python types task number ")

server_id = 103
cpu_usage = 50.5
status_msg = "Server is running"
is_ready = True

print(f"server {server_id} is of type {type(server_id)}")
print(f"the cpu is {cpu_usage} is of type {type(cpu_usage)}")
print(f"{status_msg} is of type {type(status_msg)}")
print(f"the server is running? {is_ready} {type(is_ready)}")
