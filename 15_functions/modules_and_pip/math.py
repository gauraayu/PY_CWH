import math
# https://docs.python.org/3/py-modindex.html
print(math.sqrt(16))  # Output: 4.0

import mymodule
import requests
print(mymodule.greet("Alice"))  # Output: Hello, Alice!
req=requests.get('https://docs.python.org/3/py-modindex.html')
print(req.text)
print(req.status_code)