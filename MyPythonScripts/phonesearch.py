import re

message = ('sdfjawegj 234-574-2345 234-234-234 743-527-2315 krj23 23kdj 522-135-6321')

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.findall(message)
print(mo)
