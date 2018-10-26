import os,errno
import pandas as pd
import numpy as np

from haversine import haversine
from collections import Counter


def create_dir(dir_name):

    """
    Creates a directory with the given name.
    If it already exists,does nothing.
    In case of any other error,raises exception.
    """

    try:
        os.makedirs(dir_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def pretty_print(q,elapsed_time,neighbours,flag=None):

    """
    Prints output in style
    """
    title1 = "Query "   + str(q+1) 
    title2 = "Time =  "   + str(round(elapsed_time,2)) + "sec"
    if len(title1)>len(title2):

        dash = "="*len(title1)
    else:
        dash = "="*len(title2)

    print dash
    print title1
    print title2
    print dash

    for idx,n in enumerate(neighbours):
        print "Neighbour[%d]"%(idx+1)
        if(flag==None):
            print "JP_ID :" , n[1]  
            print "DTW   :" , round(n[0],1) , "km", "\n"
        else:
            print "JP_ID           :" , n[1] 
            print "Matching Points :" , n[0] , "\n"

def create_csv(tripIdList,jpIdList):
    
    """
    Creates the testSet_JourneyPatternIDs.csv file
    """
	
    header = ['Test_Trip_ID','Predicted_JourneyPatternID']
    tuples = zip(tripIdList,jpIdList)
    pd.DataFrame(tuples).to_csv('../testSet_JourneyPatternIDs.csv',sep='\t',index=False,header=header) 

def remove_time(row):

    """
    Removes timestamps and reverses lat-lon for each point 
    """
    
    row['Trajectory'] = [list(reversed(point[-2:])) for point in row['Trajectory']]


def majority_voting(L):

    # Count occurencies(i.e: frequency) of each element in list
    counts   = Counter(L)
    
    # Get frequencies
    freqs    = counts.values()
    
    # Get element with max frequency and its frequency
    result , max_freq = counts.most_common(1)[0]

    # Repeat with one less element ,in case there are two or more elements with max frequency
    if freqs.count(max_freq) > 1:
        return majority_voting(L[:-1])
    # Return element ,in case it is the only one having that frequency
    else:
        return result

def mydtw(x,y,dist=haversine):
    
    """
    Computes Dynamic Time Warping (DTW) of two sequences.
    It does not make any approximations.
    It is based on Wikipedia's pseudocode.
    """
    
    N = len(x)
    M = len(y)
    
    # Create an array, N+1 x M+1 , filled with zeros
    DTW  = np.zeros((N+1,M+1))
    
    # Initialize first column & first row with 'inf'
    DTW[0, 1:] = float('inf')
    DTW[1:, 0] = float('inf')
    
    for i in range(1,N+1):
        for j in range(1,M+1):
            cost   = dist(x[i-1],y[j-1])
            DTW[i,j] = cost + min(DTW[i-1, j-1], DTW[i, j-1], DTW[i-1, j])
    return DTW[N,M],None    

# LCS DP algorithm
def lcs(X , Y):
    
    """
    LCS DP algorithm
    Note: We have a match only when haversine distance between two points is less 200m 
    """

    m = len(X)
    n = len(Y)

    C = [[None]*(n+1) for i in xrange(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            # Fill in 1st column and 1st row with zeros
            if i == 0 or j == 0 :
                C[i][j] = 0
            elif haversine(X[i-1],Y[j-1])<=0.2:
                C[i][j] = C[i-1][j-1]+1
            else:
                C[i][j] = max(C[i-1][j] , C[i][j-1])

    # Start from the right-most-bottom-most corner
    lcs = []
    i = m
    j = n
    while i > 0 and j > 0:
        # If current point in X and current point in Y are within 200m distance
        if haversine(X[i-1],Y[j-1])<=0.2:
            lcs.append(X[i-1])
            i-=1
            j-=1

        elif C[i-1][j] > C[i][j-1]:
            i-=1
        else:
            j-=1

    return C[m][n],lcs