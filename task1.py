'''
Solves task 1 of the Hackathon
'''

from src.acquisition import *
from src.storing import *
from src.statistics import *
from src.costants import ORG, CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME_REPOS, GITHUB_API_ENTRYPOINT


def solve_task1_1():
    '''
    Solves subtask 1.1 of the Hackathon
    '''
    base_url = os.path.join(GITHUB_API_ENTRYPOINT, "orgs", "google", "repos")
    data = retrieve_data_from_url(base_url)
    store_collection_into_db(CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME_REPOS, data)
    
def solve_task1_2_3_4():
    '''
    Solves subtask 1.2, 1.3 and 1.4 of the Hackathon
    '''
    collection = read_collection(CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME_REPOS)
    df = pd.DataFrame(list(collection))
    stargazers_distribution = df['stargazers_count']
    stats = aggregate_statistics(stargazers_distribution)
    
    return stats
        
def solve_task1():
    '''
    Solves the entire task 1 of the Hackathon
    '''
    solve_task1_1()
    stats = solve_task1_2_3_4()
    
    return stats
    
def main():
    stats = solve_task1()
    
    return stats
    
if __name__=="__main__":
    main()
    
    