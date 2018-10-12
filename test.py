import os
environment_variables = os.environ

for key,value in environment_variables :
  if key.startswith('GIT'):
    print(key)
    print(value)
