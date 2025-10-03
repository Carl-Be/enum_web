#!/usr/bin/env python3
import argparse
import webserver
import toolwrapper as tw
import os
    
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
                
            cmd_name="whatweb"
            tw.run_cmd( [cmd_name,"-v","-a","3",port.url],
                cmd_name,port.url,srv_dir,file_name_prefix)
            
            cmd_name="ffuf"
            wordlist = "/usr/share/seclists/Discovery/Web-Content/common.txt"
            tw.run_cmd( [cmd_name,"-w",wordlist,"-u",f"{port.url}/FUZZ"],
                cmd_name,port.url,srv_dir,file_name_prefix)
            
            cmd_name="hakrawler"
            tw.run_cmd( ["bash", "-c", f"echo {port.url} | {cmd_name}"],
                cmd_name,port.url,srv_dir,file_name_prefix)

            cmd_name="nuclei"
            tw.run_cmd( [cmd_name,"-u",port.url,"-t","http/technologies"],
                f"{cmd_name}_tech",port.url,srv_dir,file_name_prefix) 

            cmd_name="nuclei"
            tw.run_cmd( [cmd_name,"-u",port.url,"-t","http/misconfiguration"],
                f"{cmd_name}_misconfig",port.url,srv_dir,file_name_prefix)  

            cmd_name="nuclei"
            tw.run_cmd( [cmd_name,"-u",port.url,"-t","http/tokens"],
                f"{cmd_name}_tokens",port.url,srv_dir,file_name_prefix)  
            
            cmd_name="dalfox"
            tw.run_cmd( [cmd_name,"url",port.url],
                cmd_name,port.url,srv_dir,file_name_prefix) 

            cmd_name = "corsy"
            tw.run_cmd( [f"{cmd_name}.py","-u",port.url],
                cmd_name,port.url,srv_dir,file_name_prefix) 
            
    for key, websrv in servers.items():
        srv_dir = str(websrv.host).replace(".", "_")
        for port in websrv.ports:
            cmd_name = "nikto"
            tw.run_cmd( [cmd_name,"-h",port.url],
                cmd_name,port.url,srv_dir,file_name_prefix)  
