import os
import json
environment_variables = json.load(os.environ)
print(type(environment_variables))
for key,value in environment_variables:
  if key.startswith('GIT'):
    print(key)
    print(value)