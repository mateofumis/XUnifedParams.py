# XUnifedParams.py

  This script is focused to be used with [Dalfox](https://github.com/hahwul/dalfox)

## 🔨 Usage and examples

##### 1. Collect subdomains with [subfinder](https://github.com/projectdiscovery/subfinder) and probe all of them with [httpx](https://github.com/projectdiscovery/httpx): 

```bash
subfinder -d tesla.com -silent | httpx -o targets.txt
```

##### 2. **Crawl URLs in `targets.txt` with Katana, Gau, hakrawler, waybackurls, etc**... Unify all endpoints in a file "targets.txt"

##### 3. Collect all parameters one per line in a file "parameters.txt"

##### 4. Execute **XUnifedParams.py**. (Keep in mind that this script Read the file targets.txt and parameters.txt, then save the output as "output_XUnifedParams.txt")

##### 5. **Finally look for XSS in the output file with Dalfox**:

```bash
dalfox file output_XUnifedParams.txt -o Loot_XSS.txt
```

![https://raw.githubusercontent.com/mateofumis/XUnifedParams.py/main/preview.png](https://raw.githubusercontent.com/mateofumis/XUnifedParams.py/main/preview.png)

**I hope you find this script useful !!**

~ *Happy Hacking!!*
