## LIBRARY IMPORTS ##

import numpy as np


## FUNCTION DEF ##

def selectRoi(data, index, radius):
    '''
    Selects a region of interest from given data centered on an index with some radius of points on either side.
    
    Parameters:
        data: Array-like. 1D array of data to select from.
        index: Int index within data, center of ROI.
        radius: Number of points to select on either side of center.

    Output: Array
    '''

    # Indexed bounds of the ROI
    bounds = [index - radius, index + radius]

    # Get data over those indices
    return data[bounds[0]:bounds[1]]

# Function returns a quadratic fit of given data
def quadraticFit(x, y):
    '''
    Fits data to a quadratic function, and returns x- and y-data suitable for plotting.
    
    Parameters:
        x: Array-like independent data
        y: Array-like dependent data

    Output: Tuple of data arrays (x, y)
    '''

    # Returned x data should be a linspace over given x
    xfit = np.linspace(min(x), max(x))
    
    # Returned y data is actual quadratic fit
    coeffs = np.polyfit(x, y, 2)
    yfit = (coeffs[0] * xfit**2) + (coeffs[1] * xfit) + coeffs[2]

    # Return arrays suitable for plotting
    return xfit, yfit