"""
This module contains the functions to process statistics on some kind of distribution
"""

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)


def aggregate_statistics(distribution):
    """
    Returns some aggregate statistic (max, min, avg, std, percentiles) on the distribution given

    Args:
        - distribution (array): distribution on which we want to calculate the statistics

    Returns:
        - A dicitionary where the keys are the names of the statistic and the values are the value of that statistic
    """
    if not isinstance(distribution, np.ndarray):
        distribution = np.array(distribution)

    return {
        "mean": np.mean(distribution),
        "std": np.std(distribution),
        "max": np.max(distribution),
        "min": np.min(distribution),
        "percentile": {
            str(x): np.percentile(distribution, x) for x in range(5, 100, 5)
        },
    }


def main():
    aggregate_statistics()


if __name__ == "__main__":
    main()
