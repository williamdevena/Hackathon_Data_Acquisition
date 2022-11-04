from src.acquisition import *
from src.storing import *
from src.statistics import *

ORG = "google"
CLUSTER_NAME = "daps2022"
DATABASE_NAME = "hackathon_DAPS"
COLLECTION_NAME = "google_repos"

def solve_task1_1():
    data = retrieve_org_repos_data(ORG)
    store_collection_into_db(CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME, data)
    
def solve_task1_2():
    collection = read_collection(CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME)
    stargazers_distribution = collection['stargazers_count']
    stats = aggregate_statistics(stargazers_distribution)
    
    return stats
    
    
    
    
    
    
    

def solve_task1_3():
    raise NotImplementedError

def solve_task1_4():
    raise NotImplementedError

        
def solve_task1():
    solve_task1_1()
    solve_task1_2()
    solve_task1_3()
    solve_task1_4()
    
    
def main():
    solve_task1_2()
    
    
if __name__=="__main__":
    main()
    
    