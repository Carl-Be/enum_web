# initwebenum (v0.1)
```sh
initwebenum.py -w </path/to/url/lst>
```

## Info
Run this command against a list of webservers for quick initial enumeration while you 
happy path the sites. This script takes care of the dir structure and file names of 
the output files for the commands. 

## wordlist structure 
The wordlist must include one URL per line. For now the script does not handel the '/' char  
that might be at the end of an URL. Below are exmples of what a good and bad URL looks like. 

Good URLs:
http://evil.corp.com:8080
http://evil.corp.com
https://evil.corp.com:8433
https://evil.corp.com

Bad URLs:
evil.corp.com
evil.corp.com/
https://evil.corp.com:8433/

## Commands 
initwebenum runs the following commands against a web server: 

FFuF with common.txt
nuclei for token,misconfig,and tech templates 
nikto
hakrawler
dalfox
corsy
whatweb

## TODO
- [ ] Add threading
- [ ] Handel '/' at the end of urls gracefully
