import csv

def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            
            # parse each of the commment lines 
            commit_details = data[index+2:data.index(sep,index+1)]
            
            # commit text
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': (details[2][0:11]).strip(),
                'year': (details[2][0:5]).strip(),
                'month': (details[2][36:40]).strip(),
                'time_stamp': (details[2][11:20]).strip(),
                'number_of_lines': (details[3].strip().split(' ')[0]), 
                'commit_details': commit_details[-1]
            }
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.txt'
    data = read_file(changes_file)
    commits = get_commits(data)

    # print the number of lines read
    # print(len(data))
    # print(commits)
    print(commits)
    # print(commits[1]['author'])
    # print(len(commits))
    
with open("CA_output.csv",'wb') as f:
   # Using dictionary keys as fieldnames for the CSV file header
   writer = csv.DictWriter(f, commits[0].keys())
   writer.writeheader()
   for d in commits:
      writer.writerow(d)
    
    
    
    