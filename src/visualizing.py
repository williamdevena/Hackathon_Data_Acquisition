'''
This module contains function for visualizing data
'''

import matplotlib.pyplot as plt

def visualize_time_series_aggregate(aggregate):
    '''
    Plots the time series of the commits in the MongoDB aggregate (list of dictionaries)
    
    Args:
        - aggregate (List): Contains the MongoDB aggregate result. It should have the keys 'date'
        and 'count'.
        
    Returns:
        - None
    '''
    x = [doc['date'] for doc in aggregate]
    y = [doc['count'] for doc in aggregate]
    plt.plot(x,y)
    plt.show()
    
    
def main():
    pass

if __name__=="__main__":
    main()