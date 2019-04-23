#匹配任意数字 \d
#匹配任意一个  .
#匹配多个  *
#全是小写'^[a-z]+$'

import re


key = r'(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}'
data = ''
with open('sou.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line.strip('\n')
        result = re.sub(key,'2.2.2.2',line)
        data += result
        #print(data)

with open('sou.txt','w') as f:
    f.writelines(data)

