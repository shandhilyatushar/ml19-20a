'''
    Package: cs771
    Module: plotData
    Author: Puru
    Institution: CSE, IIT Kanpur
    License: GNU GPL v3.0
    
    Plot 2D data in various ways to visualize classifiers and other things
'''

from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as lsc
import numpy as np

# A light red and light green binary colormap
colors = [ (1, 0.85, 0.85), (0.85, 1, 0.85) ]
nbins = 2
lrlg = lsc.from_list( 'lrlg', colors, nbins )

def getFigure( sizex = 7, sizey = 7 ):
    fig = plt.figure( figsize = (sizex, sizey) )
    return fig

def plotCurve( responseGenerator, fig, mode = "point", color = 'b', line = "solid", xlimL = 0, xlimR = 10, nBins = 500, label = "" ):
    X = np.linspace( xlimL, xlimR, nBins, endpoint = True )
    if mode == "point":
	    y = np.zeros( X.shape )
	    for i in range( X.size ):
		    y[i] = responseGenerator( X[i] )
    elif mode == "batch":
	    y = responseGenerator( X )
    plt.figure( fig.number )
    plt.plot( X, y, color = color, linestyle = line, label = label )
    if label:
        plt.legend()

def plot2D( X, fig, color = 'r', marker = '+', size = 100 ):
    plt.figure( fig.number )
    plt.scatter( X[:,0], X[:,1], s = size, c = color, marker = marker )

def plot2DPoint( X, fig, color = 'r', marker = '+', size = 100 ):
    plt.figure( fig.number )
    plt.scatter( X[0], X[1], s = size, c = color, marker = marker )

def shade2D( labelGenerator, fig, mode = "point", colorMap = lrlg, xlim = 10, ylim = 10, nBins = 500 ):
    xi, yi = np.mgrid[ -xlim:xlim:nBins*1j, -ylim:ylim:nBins*1j ]
    zi = np.zeros( xi.shape )
    if mode == "point":
        for i in range( zi.shape[0] ):
            for j in range( zi.shape[1] ):
                zi[i,j] = labelGenerator( xi[i,j], yi[i,j] )
    elif mode == "batch":
        zi = labelGenerator( np.hstack( (xi.reshape((xi.size, 1)), yi.reshape((yi.size, 1))) ) )
        zi = zi.reshape( xi.shape )
    zi[zi < 1/nBins] = 0
    zi[zi > 0] = 1
    plt.figure( fig.number )
    plt.pcolormesh( xi, yi, zi, cmap = colorMap )