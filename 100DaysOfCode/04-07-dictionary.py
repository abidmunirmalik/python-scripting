# dictionaries are indexed by 'keys'
# keys can be any immutable types i.e string, int can always be dictionary key
# a list cannot be a key as it is mutable
# tuple can be a key if it contains only strings, numbers
# think of a dictionary as a set of key:value pair  
# keys are unique within one dictionary
# A pair of braces {} creates an empty dictionary
# The main purpose of dictinary is storing a value with key
# If a key already exists and new value is provided, it will override old value
from collections import defaultdict, namedtuple, Counter
import csv

books = {"oracle":9.99, "mysql":10.99, "python":12.99, "NodeJs" : 0}

# How to set a value to a key?
books["NodeJs"] = 14.99 # old value overwritten
print(books)

# How to get all the keys from dictionary?
keys  = list(books)
print(type(keys), len(keys))

# Given we know the keys, how to get corresponding values?
for k in keys:
    print(k, books[k])

# Remove all dictionary items where price is less than 10
for k in keys:
    if books[k] < 10:
        del books[k]
print(books)   

# How can I add an key:value pair in dictionary?
books["oracle"] = 9.99
print(books)

# How many items are in dictionary?
print("Number of key:value items in books: {}".format(len(keys)))

# dict() constructor to create dictionary
a = dict(one=1, two=2, three=3)
print(a)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e) # True

# How can we define  dictionary using dict()? 
major_cities = {"usa" : "NYC", "pakisan" : "LAHORE", "india" : "Dehli"}
major_capitals = dict([("usa","Washington DC"),("Pakistan","Islamabad")])
teams = dict(peshawar='zalmi',lahore='kalandars', karachi='kings', queta='gladiators', multan='sultans')
print(major_cities) 
print(major_capitals)
print(teams)

# Looping through dictionary always through items()
for donga, bonga in major_cities.items():
    print(donga,bonga)

print('-'*50)
NUM_TOP_EMPLOYEES = 3

Score = namedtuple('Score', ['avg', 'count','employment'])
Jobs = namedtuple('Jobs', ['title','state','tenure','rating'])


def get_employee_data(): 
    employee_data = defaultdict(list)
    with open('sample.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        #print("CSV FILE METADATA")
        #print("Field Names:",reader.fieldnames)
        for row in reader:
            try:
                name  = row['name']
                state = row['state']
                title = row['title']
                tenure = row['tenure']
                rating = row['rating'] 
            except ValueError:
                continue
            jobs = Jobs(title=title, state=state, tenure=tenure, rating=rating)
            employee_data[name].append(jobs)
    return employee_data
     
def get_average_scores(employees):
    scores = defaultdict(list)
    for employee, employment in employees.items():
        if len(employment) > 2:
            scores[employee] = Score(avg=_calc_mean(employment),count=len(employment),employment=employment)
    return scores           


def print_results(employees):
    fmt_employee_entry = '{counter:02}. {employee:<52} {avg:3.1f}'
    fmt_employment_entry = '{year}] {title:<50} {score:3.1f}'
    sep_line = '-' * 60
    for rank, employee in enumerate(sorted(employees.values(), key=lambda d: d.avg, reverse=True)[:NUM_TOP_EMPLOYEES]):
        print(fmt_employee_entry.format(counter=rank+1, employee=employee.name, avg=employee.avg))
        print(sep_line)
        # for movie in sorted(director.movies, key=lambda m: m.score, reverse=True):
        #     print(fmt_movie_entry.format(year=movie.year, title=movie.title[:50], score=movie.score))
        # print()

def employee_info(employees):
    # Keys
    print("Employees Keys\n----------\n")
    print(employees.keys())
    # Values
    print("Employees Values\n----------\n")
    print(employees.values())
    # Items
    print("Employees Items\n----------\n")
    print(employees.items())
    # Give me those employees who's job title is SysAdmin
    employees_with_onejob = []
    for employee,jobs in employees.items():
        e, j = employee,len(jobs)
        if j == 1:
            employees_with_onejob.append(e) 
    for _ in employees_with_onejob:
        del employees[_]
    return employees          

def employee_jobs(employees):
    print("Employees Jobs\n----------\n")
    print(employees.items())
    print("-----------")
    for employee,jobs in employees.items():
        print(employee,[j.rating for j in jobs],_calc_mean(jobs))

def _calc_mean(jobs):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(sum([float(j.rating) for j in jobs]) / len(jobs), 1)


def main():
    employees = get_employee_data()
    #employees = get_average_scores(employees)
    employees = employee_info(employees)
    employees = employee_jobs(employees)
    #print("Employees with more than one job\n----------\n")
    #print(employees.keys())


if __name__ == '__main__':
    main()            
  
