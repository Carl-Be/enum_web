# initwebenum (v0.1)

## Usage

```sh
initwebenum.py -w </path/to/url.lst>
```
## Info
Run this command against a list of webservers for quick initial enumeration while you 
happy path the sites. This script takes care of the dir structure and file names of 
the output files for the commands. 

## Wordlist Structure 
The wordlist must include one URL per line. For now the script does not handel the '/' char  
that might be at the end of an URL. Below are exmples of what a good and bad URL looks like. 

### Good URLs:

http://evil.corp.com:8080

http://evil.corp.com

https://evil.corp.com:8433

https://evil.corp.com

### Bad URLs:

evil.corp.com

evil.corp.com/

https://evil.corp.com:8433/

## Commands ran by initwebenum
Make sure these tools are in your PATH env var. For corsy.py make sure to "chmod +x corsy.py"

- [FFuF](https://github.com/ffuf/ffuf) with [SecList](https://github.com/danielmiessler/SecLists) common.txt
- [nuclei](https://github.com/projectdiscovery/nuclei) with token,misconfig,and tech templates 
- [nikto](https://github.com/sullo/nikto)
- [hakrawler](https://github.com/hakluke/hakrawler)
- [dalfox](https://github.com/hahwul/dalfox/releases) 
- [corsy.py](https://github.com/s0md3v/Corsy)
- [whatweb](https://github.com/urbanadventurer/WhatWeb)

## TODO
- [ ] Add threading
- [ ] Handel '/' at the end of urls gracefully
- [ ] Modular rate limiting
