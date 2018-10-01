## LIBRARY IMPORTS ##

import numpy as np
import scipy.optimize as optimize


## FUNCTION DEF ##

def curveFit(fitfxn, x, y, guess):
    '''
    Fits given xy-data to a given function of n-arguments. Returns a tuple of arrays containing x- and y- data suitable for plotting.

    Parameters:
        fitfxn: A proper Python function with at least 1 argument, which returns a number value. Data will be fitted to this function by calling fitfxn(x, *args).
        x: Array-like independent data.
        y: Array-like dependent data.
        guess: Tuple-like of n-1 elements corresponding to guessed values for <*args> of fitfxn.

    Output: Tuple of arrays, (x, y, popt).
        popt is parameters used to fit data to fitfxn
    '''

    # Use scipy curve_fit to find argument values
    popt, pcov = optimize.curve_fit(fitfxn, x, y, p0=guess)

    # Return linear space across x bounds
    xfit = np.linspace(min(x), max(x))

    # Evaluate fitfxn over x space using fitted params
    yfit = fitfxn(xfit, *popt)

    return xfit, yfit, popt