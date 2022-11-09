"""
Solves task 1 of the Hackathon
"""

from src.acquisition import *
from src.storing import *
from src.statistics import *
from src.reading import *
from src.costants import (
    ORG,
    CLUSTER_NAME,
    DATABASE_NAME,
    COLLECTION_NAME_REPOS,
    GITHUB_API_ENTRYPOINT,
)


def solve_task1_1():
    """
    Solves subtask 1.1 of the Hackathon
    """
    base_url = os.path.join(GITHUB_API_ENTRYPOINT, "orgs", "google", "repos")
    data = retrieve_data_from_url(base_url)
    store_collection_into_db(CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME_REPOS, data)


def solve_task1_2_3_4():
    """
    Solves subtask 1.2, 1.3 and 1.4 of the Hackathon
    """
    collection = read_collection(CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME_REPOS)
    df = pd.DataFrame(list(collection))
    stargazers_distribution = df["stargazers_count"]
    stats = aggregate_statistics(stargazers_distribution)

    return stats


def solve_task1():
    """
    Solves the entire task 1 of the Hackathon
    """
    solve_task1_1()
    stats = solve_task1_2_3_4()
    ## Storing in the database the results
    submission = {
        "task-1-submission": {
            "mean": float(stats["mean"]),
            "std": float(stats["std"]),
            "min": int(stats["min"]),
            "max": int(stats["max"]),
            "percentile_5": float(stats["percentile"]["5"]),
            "percentile_10": float(stats["percentile"]["10"]),
            "percentile_25": float(stats["percentile"]["25"]),
            "percentile_75": float(stats["percentile"]["75"]),
            "percentile_90": float(stats["percentile"]["90"]),
            "percentile_95": float(stats["percentile"]["95"]),
        }
    }
    client = connect_cluster_mongodb(CLUSTER_NAME, MONGODB_USERNAME, MONGODB_PASSWORD)
    database = connect_database(client, DATABASE_NAME)
    collection = connect_collection(database, "answer")
    collection.insert_one(submission)

    return stats


def main():
    stats = solve_task1()
    print(stats)


if __name__ == "__main__":
    main()
