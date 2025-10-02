import argparse
import webserver   
import os
import subprocess

def run_whatweb(url,parent_dir,file_name_prefix):
    print(f"Running whatweb on {url}")
    this_dir = f"{parent_dir}/whatweb"
    try:
        os.mkdir(this_dir)
    except:
        pass

    cmd = ["whatweb","-v","-a","3",url]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            timeout=15
        )

        with open(f"{this_dir}/{file_name_prefix}_whatweb.out", "w") as f:
            f.write(result.stdout)
        pass
    except subprocess.CalledProcessError as e:
        return f"Scan failed: {e.stderr}"
    except subprocess.TimeoutExpired:
        return "Scan timed out"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w","--wordlist",help="Wordlist of webservers.",required=True)
    args = parser.parse_args()
    wordlist = args.wordlist

    servers = webserver.set_servers(wordlist)
    servers: dict
    for key, websrv in servers.items():
        srv_dir = str(websrv.host).replace(".", "_")
        try:
            os.mkdir(srv_dir) 
        except:
            pass
        for port in websrv.ports: 
            file_name_prefix = f"{port.proto}_{srv_dir}_{port.port_number}"
            run_whatweb(port.url,srv_dir,file_name_prefix)

