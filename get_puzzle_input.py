###
# Run pip-sync to install dependencies (if pip-sync is missing, run pip install pip-tools first)
# pip-sync --upgrade --requirement requirements.txt
#
# Browse to adventofcode.com, log in using your preferred auth method.
# Open your browsers development tools, and find the Cookie named 'session'.
# For Chrome / Edge that is: F12 > Application > Storage > Cookies > https://adventofcode.com > session
# Store its value in a file named Cookie in the same folder as this script.

import datetime
import os
import requests
import subprocess
import webbrowser
import shutil

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
try: 
    with open(currentWorkingDir + '\\Cookie') as f:
        sessionCookie = f.readline().strip()
except FileNotFoundError:
    print("No cookie file found. Please open your browser's developer tools and find the Cookie named 'session', copy its contents to a file named Cookie and store it in the root of the repo.")
    exit()

if sessionCookie == '':
    print("Please save the value of the 'session' cookie from your browser and store it in a file named 'Cookie' in this directory. More info in the comments of this script.")
    exit()

date = datetime.datetime.now()
year = date.year
day = date.day
month = date.month
baseUrl = "https://adventofcode.com"

fileTemplate = """
import os

currentWorkingDir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(currentWorkingDir + '\input.txt') as f:
    lines = f.readlines()

"""

#region functions

def try_grab_and_save_input(year, d):
    fileName = get_day_path(d, 'input.txt')

    if os.path.exists(fileName):
        print("Found puzzle input in file for day '{d}', no need to grab from url.".format(d=d))
    else:
        uri = "{baseUrl}/{year}/day/{d}/input".format(baseUrl=baseUrl,year=year, d=d)

        try:
            input = requests.get(uri, cookies={"session": sessionCookie}).text
            print("Grabbed puzzle input for day '{d}' from url.".format(d=d))
        except Exception as e:
            print("Could not get puzzle input for day '{d}' from url.".format(d=d))
            print(e)
        else:
            try:
                with open(fileName, 'w') as f:
                    f.write(input)
                print("Saved puzzle input for day '{d}' to file.".format(d=d))
            except:
                print("Could not save puzzle input for day '{d}' to file.".format(d=d))

def get_day_path(d, fileName):
    path = '\\'.join([currentWorkingDir, 'day{d}'.format(d=d)])
    if fileName == '':
        return path
    else:
        return '\\'.join([path, fileName])

def setup():
    print('Setting up default folders and files for each puzzle.')
    for i in range(1, 25):
        day = "day{i}".format(i=i)

        folderToCreate = get_day_path(i, '')

        if not os.path.exists(folderToCreate):
            os.makedirs(folderToCreate)

        for fileName in [day + '-1.py', day + '-2.py', 'input.txt', 'exampleinput.txt']:
            fileToCreate = get_day_path(i, fileName)
            if not os.path.exists(fileToCreate):
                with open(fileToCreate, 'w') as f:
                    f.write('')

        puzzle_1_script = get_day_path(i, day + '-1.py')
        with open(puzzle_1_script, 'r') as f:
            fileContent= f.read()

        if fileContent == '':
            with open(puzzle_1_script, 'w') as f:
                f.write("# {baseUrl}/{year}/day{i} \n\n".format(baseUrl=baseUrl,year=year,i=i) + fileTemplate)

#endregion functions

if month < 12:
    year = year - 1
    days = range(1, 26)
    print("Fetching puzzle input for last year: {year}, days 1-25.".format(year=year))
else:
    days = range(1, day+1)
    print("Fetching puzzle input for this year: {year}, days 1-{day}.".format(year=year, day=day))

# get parent directory name from current workind directory

parent_dir_name = os.path.basename(currentWorkingDir)
if parent_dir_name != 'adventofcode{year}'.format(year=year):
    print("Parent dir must be named 'adventofcode{year}', but is {parent_dir_name}.".format(year=year, parent_dir_name=parent_dir_name))
    exit()

if not os.path.exists(get_day_path(25, '')):
    setup()

for d in days:
    try_grab_and_save_input(year, d)

daypath = get_day_path(day,'')

subprocess.run([(shutil.which("code")), '{daypath}\\day{day}-1.py'.format(daypath=daypath,day=day)])
os.chdir('{daypath}\\'.format(daypath=daypath))
webbrowser.open('{baseUrl}/{year}/day/{day}'.format(baseUrl=baseUrl,year=year,day=day))
