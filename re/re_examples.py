import re

words = ["kk","ajy","l"]
result = [i for i in words if re.match(r"[djlk]{2}$", i)]

print(result)

words2 = ["asd", "aei", "a"]
result2 = [w for w in words2 if re.match(r"[aeiou]{3}$", w)]

print(result2)

import keyword
#lsta słów zarezerwoanych dla pythona
print(keyword.kwlist)
