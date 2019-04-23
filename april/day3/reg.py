#匹配任意数字 \d
#匹配任意一个  .
#匹配多个  *
#全是小写'^[a-z]+$'
#匹配ip   '(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}'

import re


key = r'[1-9]?\d$'
#key = r'[1-9]?[0-9]$|100'
with open('sou.txt') as f:
    lines = f.readlines()
    for line in lines:
        line.strip('\n')
        result = re.findall(key,line)
        print(result)

