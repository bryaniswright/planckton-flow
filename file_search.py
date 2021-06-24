import signac
from termcolor import colored
import sys
import os
import pyperclip


arguments={}
for i,x in enumerate(sys.argv[1:]):
    if i%2 == 0:
        key = str(x)
    else:
        try:
            arguments[key] = int(x)
        except:
            try:
                arguments[key] = float(x)
            except:
                arguments[key] = x

project=signac.get_project()
results= project.find_jobs(filter = arguments)
#if len(results) == 1:
#    for job in results:
#        dir_path = os.path.dirname(job.ws)
#        dir_path = os.path.dirname(os.path.realpath(job.ws))
#        os.system(f"cd {dir_path}")
#        os.chdir(job.ws)
#        os.system('pwd')
#        os.system(f"cd {dir_path} | ls")
#        print(os.listdir(job.ws))
#        os.chdir(job.ws)
#        os.listdir()
#else:
for job in results:
    print(colored(job, "green"))
    print(colored(job.sp, "blue"))
    print("")

