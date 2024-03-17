#!/usr/bin/env python
with open('targets.txt', 'r') as targets_file:
    targets = targets_file.read().splitlines()

with open('parameters.txt', 'r') as params_file:
    parameters = params_file.read().splitlines()

new_urls = []
for target in targets:
    params_str = '&'.join([f"{param}=x" for param in parameters])
    new_url = f"{target}/?{params_str}"
    new_urls.append(new_url)

with open('output_XUnifedParams.txt', 'w') as output_file:
    for url in new_urls:
        output_file.write(url + '\n')
