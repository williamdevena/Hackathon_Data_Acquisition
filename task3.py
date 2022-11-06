'''
Solves task 3 of the Hackathon
'''

from src.costants import *
from src.reading import *
from src.storing import *
from src.acquisition import *
import os

ISSUE_NUMBER = 5501

def solve_task3_1():
    '''
    Solves subtask 3.1 of the Hackathon
    '''    
    base_url = os.path.join(GITHUB_API_ENTRYPOINT, "repos", "google", "jax", "issues")
    retrieve_conditions = ["state=all"]
    data = retrieve_data_from_url(base_url, retrieve_conditions, 1, 1000)
    store_collection_into_db(CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME_JAX_ISSUES, data)
    collection = read_collection(CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME_JAX_ISSUES_CLOSED)
    df = pd.DataFrame(list(collection))
    issue = df.loc[df['number'] == ISSUE_NUMBER]
    
    return issue

def solve_task3_2():
    '''
    Solves subtask 3.2 of the Hackathon
    '''
    base_url = os.path.join(GITHUB_API_ENTRYPOINT, "repos", "google", "jax", "issues", str(ISSUE_NUMBER), "comments")
    retrieve_conditions = []
    comments = retrieve_data_from_url(base_url, retrieve_conditions, 1, 1000)
    print(type(comments))
    lambda_sorter = lambda dict: dict['reactions']['hooray'] + dict['reactions']['heart'] + dict['reactions']['rocket'] 
    sorted_comments = a = sorted(comments, key=lambda_sorter, reverse=True)
    best_comment = sorted_comments[0]
    
    return best_comment

def solve_task3():
    '''
    Solves the entire task 3 of the Hackathon
    '''
    issue = solve_task3_1()
    best_comment = solve_task3_2()
    
    return issue, best_comment


def main():
    issue, best_comment = solve_task3_2()
    print(issue, best_comment)
    
if __name__=="__main__":
    main()