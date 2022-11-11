"""
Solves task 2 of the Hackathon
"""

from src.acquisition import *
from src.storing import *
from src.statistics import *
from src.visualizing import *
from src.costants import (
    CLUSTER_NAME,
    DATABASE_NAME,
    COLLECTION_NAME_JAX,
    GITHUB_API_ENTRYPOINT,
)


def solve_task2_1():
    """
    Solves subtask 2.1 of the Hackathon
    """
    base_url = os.path.join(GITHUB_API_ENTRYPOINT, "repos", "google", "jax", "commits")
    data = retrieve_data_from_url(base_url)
    store_collection_into_db(CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME_JAX, data)


def solve_task2_2():
    """
    Solves subtask 2.2 of the Hackathon
    """
    aggregate_pipeline = [
        {"$addFields": {"date": "$commit.author.date"}},
        {"$project": {"date": {"$arrayElemAt": [{"$split": ["$date", "T"]}, 0]}}},
        {"$project": {"date": {"$toDate": "$date"}}},
        {"$group": {"_id": "$date", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}},
        {"$project": {"date": "$_id", "count": "$count"}},
    ]
    result = aggregate_collection(
        CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME_JAX, aggregate_pipeline
    )

    return list(result)


def solve_task2_3(aggregate):
    """
    Solves subtask 2.3 of the Hackathon
    """
    visualize_time_series_aggregate(aggregate)


def solve_task2():
    """
    Solves the entire task 2 of the Hackathon
    """
    solve_task2_1()
    aggregate = solve_task2_2()
    ## Storing in the database the results
    submission_result = [x["count"] for x in aggregate]
    submission = {"task-2-submission": {"timeseries": submission_result}}
    client = connect_cluster_mongodb(CLUSTER_NAME, MONGODB_USERNAME, MONGODB_PASSWORD)
    database = connect_database(client, DATABASE_NAME)
    collection = connect_collection(database, "answer")
    collection.insert_one(submission)
    solve_task2_3(aggregate)


def main():
    solve_task2()


if __name__ == "__main__":
    main()
