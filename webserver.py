class Port:
    def __init__(self, url, proto, port_number):
        self.url = url         
        self.proto = proto
        self.port_number = port_number

    def __str__(self) -> str:
        return f"{self.proto}/{self.port_number}"

class Server:
    def __init__(self,host):
        self.host = host
        self.ports: Port = []

    def __str__(self) -> str:
        output = f"{self.host}:\n"
        for port in self.ports:
            output += f"\t{str(port)}\n"
        return output
    
def parse_url(url: str):
    proto = url.split(":")[0]
    host = url.split(":")[1].split("/")[2]
    try:
        port_number = url.split(":")[2]
    except:
        if proto == "https":
            port_number = '443'
        else:
            port_number = '80'
    
    return (proto,host,port_number)

def set_servers(wordlist):
    servers : Server = {}
    try:
        with open(wordlist) as file:
            while url := file.readline():
                proto, host, port_number = parse_url(url.strip())
                server = servers.get(host, None)
                this_port = Port(url.strip(), proto, port_number)
                if server == None:
                    servers[host] = Server(host)
                    servers[host].ports.append(this_port) 
                else:
                    servers[host].ports.append(this_port) 
                pass 
    except Exception as e:
        print(e)
        exit(1)

    return servers
