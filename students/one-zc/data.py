## LIBRARY IMPORTS ##

import numpy as np


## FUNCTION DEF ##

# Function imports xy data from the given filename
def xyImport(path):
    '''
    Imports xy-data from columns in a text-based file (i.e. CSV) and returns a tuple of arrays containing the x-data (first column) and y-data (second column).

    Parameters:
        path: Path to data file.

    Output: Tuple of arrays (x, y)
    '''
    
    # Import the data
    # dtype is float64 for the whole array
    # omitting delimiter option lets genfromtxt find data on each line automatically
    data = np.genfromtxt(path, usecols=(0, 1))

    # Use subarray to grab x and y data into their own arrays
    x = data[:, 0]
    y = data[:, 1]

    # Return a tuple of arrays with separated data
    return x, y