# help(str.split)

import re
# :이나 |를 ,로 치환: 자연어 처리할 때 많이 사용
# testStr = "apple:samsung google|kakao"
# result = re.sub("[:|]", ",",testStr)
# print(result)

# email 형식인지 검사.
p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

emails = [' abc@abc.com', 'fsfsa@afsd.','afsd@asfsdf.com']

for email in emails :
    print(p.match(email) != None, end=' ')