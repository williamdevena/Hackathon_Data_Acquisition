import numpy as np
import pandas as pd
import logging
from src.storing import *

logging.basicConfig(level=logging.INFO)


def aggregate_statistics(distribution):
    if not isinstance(distribution, np.ndarray):
        distribution = np.array(distribution)

    return {
        'mean' : np.mean(distribution),
        'std' : np.std(distribution),
        'max' : np.max(distribution),
        'min' : np.min(distribution),
        'percentile' : {str(x) : np.percentile(distribution, x) for x in range(5, 100, 5)},
    }
    
    

def main():
    aggregate_statistics()
    
if __name__=="__main__":
    main()