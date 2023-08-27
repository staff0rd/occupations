from api import run
import json
import time

def read_categories():
    with open("datasets/occupation_categories.txt", "r") as file:
        categories = file.readlines()
    return categories

def create_prompt(category):
    return f'''Job title list. From the category, produce a list of job titles. 
Provide job titles as a json encoded array of strings.

Category: Accountants, Auditors
Job Title(s): ["Accountant", "Auditor"]

Category: {category}
Job Title(s):'''

def get_result(line):
    result = run(create_prompt(line))
    try:
        parsed = json.loads(result)
    except:
        print(f"Could not parse {result}")
        return None
    return parsed


start_time = time.time()
categories = read_categories()
occupations = set()
for category in categories:
    result = get_result(category)
    if result is None:
        continue
    lower_case = list(map(str.lower, result))
    print(lower_case)
    occupations.update(lower_case)

with open("datasets/occupations7B-again.txt", "w") as file:
    for x in occupations:
        file.write(x + "\n")

end_time = time.time()
elapsed_time = end_time - start_time
print('Execution time:', elapsed_time, 'seconds')
