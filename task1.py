from acquisition import *
from storing import *

def solve_task1_1():
    org = "google"
    cluster_name = "daps2022"
    database_name = "hackathon_DAPS"
    collection_name = "google_repos"
    data = retrieve_org_repos_data(org)
    store_collection_into_db(cluster_name, database_name, collection_name, data)
    
def solve_task1_2():
    raise NotImplementedError

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
    solve_task1_1()
    
    
if __name__=="__main__":
    main()
    
    