import os
import json
environment_variables = os.environ
build_number = environment_variables['BUILD_NUMBER']
print(build_number)
number_of_repositories=0
for environment_variable in environment_variables:
  if environment_variable.startswith('GIT_URL'):
    number_of_repositories+=1
print(number_of_repositories)
initial=""
for i in range(0,number_of_repositories):
  if i==0:
    print(environment_variables['GIT_URL'])
    print(environment_variables['GIT_BRANCH'])
    print(environment_variables['GIT_COMMIT'])
  else:
    print(environment_variables['GIT_URL_'+str(initial)])
    print(environment_variables['GIT_BRANCH_'+str(initial)])
    print(environment_variables['GIT_COMMIT_'+str(initial)])
  initial=i+1
 
