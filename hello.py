import os

print("hello")

env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("ERR_CODE=0")
