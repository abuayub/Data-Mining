# -*- coding: utf-8 -*-
from math import pow, sqrt
import csv
import matplotlib.pyplot as plt
import numpy as np

class Point(object):
    def __init__(self,feature_vector):
        self.feature_vector = feature_vector
        self.cluster = None
        self.visited = False

    def __str__(self):
        return str(self.feature_vector)

def _as_points(points):
    return [Point(point) for point in points]

def as_lists(clusters):
    clusters_as_points = {}
    for cluster, members in clusters.items():
        clusters_as_points[cluster] = [member.feature_vector for member in members]
    return clusters_as_points

def print_points(points):
    s = ''
    for p in points:
        s += str(p) + '\n'
    return s[:-2]

def euclidean(x,y):
    assert len(x) == len(y)
    sum = 0.0
    for i in range(len(x)):
        sum += pow(x[i] - y[i],2)
    return sqrt(sum)

def immediate_neighbours(point, all_points, epsilon, distance, debug):
   
    neighbours = []
    for p in all_points:
        if p == point:
            continue
        d = distance(point.feature_vector,p.feature_vector)
        if d < epsilon:
            neighbours.append(p)
    return neighbours

def add_connected(points, all_points, epsilon, min_pts, current_cluster, distance, debug):
    ''' find every point in the set of all_points which are
    density-connected, starting with the initial points list. '''
    cluster_points = []
    for point in points:
        if not point.visited:
            point.visited = True
            new_points = immediate_neighbours(point, all_points, epsilon, distance, debug)
            if len(new_points) >= min_pts:                                
                for p in new_points:
                    if p not in points:
                        points.append(p)

        if not point.cluster:
            cluster_points.append(point)
            point.cluster = current_cluster
    if debug: 
        print ('Added points %s' % print_points(cluster_points))
    return cluster_points

def dbscan(points, epsilon, min_pts, distance=euclidean, debug=False):
    

    
    epsilon = float(epsilon)
    if not isinstance(points, Point):
        points = _as_points(points)

    if debug:
        print ('\nEpsilon: %.2f' % epsilon)
        print ('Min_Pts: %d' % min_pts)
    
    clusters = {}    
    clusters[-1] = []  
    current_cluster = -1
    for point in points:
        if not point.visited:
            point.visited = True
            neighbours = immediate_neighbours(point, points, epsilon, distance, debug)
            if len(neighbours) >= min_pts:
                current_cluster += 1
                if debug: 
                    print ('\nCreating new cluster %d' % (current_cluster))
                    print ('%s' % str(point))
                point.cluster = current_cluster                
                cluster = [point,]
                cluster.extend(add_connected(neighbours, points, epsilon, min_pts, 
                                             current_cluster, distance, debug))
                clusters[current_cluster] = cluster
            else:
                clusters[-1].append(point)
                if debug: 
                    print ('\nPoint %s has no density-connected neighbours.' % str(point.feature_vector))

    return as_lists(clusters)

if __name__ == '__main__':
    epsilon = 250
    min_pts = 0.5

    reader=csv.reader(open("atttwod.csv","rt"),delimiter=',')
    x=list(reader)
    points = []
    reader2 = csv.reader(open("atttwod.csv","rt"), delimiter=',', lineterminator='\n')
    for row in reader2:
        points.append(row)
    #print(points.shape)    
    points = np.array(points).astype('float')
   
    print(points)
    #points = []
    #for i in xrange(150):
        #points.append([random.uniform(0.0, 20.0), random.uniform(0.0, 20.0)])

    clusters = dbscan(points, epsilon, min_pts, debug=True)
    print ('\n========== Results of Clustering =============')
    for cluster, members in clusters.items():
        print ('\n--------Cluster %d---------' % cluster)
        for point in members:
            print (point)
 

