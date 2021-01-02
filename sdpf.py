# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 

# Library for INT_MAX 
import sys 

class Graph(): 

	def __init__(self, vertices,n): 
		self.V = vertices 
		self.N=n
		self.graph = [[0 for column in range(vertices)] 
					for row in range(vertices)] 

	def printSolution(self, dist,m,y,t):
	    col=self.V+2
	    print("--------------------------------------------------------------------------------------------------------------")
	    print("Source\t->\tDestination \tDistance \t\t path")
	    print("--------------------------------------------------------------------------------------------------------------")
	    for node in range(self.V):
	        
	            w=[]
	            w1=[]
	            p=node
	            if p==t:
	                
	                print(m.ljust(5)+"->".ljust(10)+m.ljust(15),dist[node],"km".ljust(16),end=" ") 
	                print(m)
	                continue
	            while p!=t:
	                w.append(self.N[p])
	                p=y[p]
	            w.append(m)
	            w1=w[::-1]
	            print(m.ljust(5)+"->".ljust(10)+self.N[node].ljust(15),dist[node],"km".ljust(14),end=" ") 
	            for x in w1:
	                print(x,end=" ")
	            print()

	# A utility function to find the vertex with 
	# minimum distance value, from the set of vertices 
	# not yet included in shortest path tree 
	def minDistance(self, dist, sptSet): 

		# Initilaize minimum distance for next node 
		min = sys.maxsize 

		# Search not nearest vertex not in the 
		# shortest path tree 
		for v in range(self.V): 
			if dist[v] < min and sptSet[v] == False: 
				min = dist[v] 
				min_index = v 

		return min_index 

	# Funtion that implements Dijkstra's single source 
	# shortest path algorithm for a graph represented 
	# using adjacency matrix representation 
	def dijkstra(self, src,m): 

		dist = [sys.maxsize] * self.V 
		dist[src] = 0
		sptSet = [False] * self.V 
		y=[sys.maxsize] * self.V 
		y[src]=0

		for cout in range(self.V): 

			# Pick the minimum distance vertex from 
			# the set of vertices not yet processed. 
			# u is always equal to src in first iteration 
			u = self.minDistance(dist, sptSet) 

			# Put the minimum distance vertex in the 
			# shotest path tree 
			sptSet[u] = True

			# Update dist value of the adjacent vertices 
			# of the picked vertex only if the current 
			# distance is greater than new distance and 
			# the vertex in not in the shotest path tree 
			for v in range(self.V): 
				if self.graph[u][v] > 0 and sptSet[v] == False and  dist[v] > dist[u] + self.graph[u][v]: 
						dist[v] = dist[u] + self.graph[u][v] 
						y[v]=u
		

		self.printSolution(dist,m,y,src) 

# Driver program 
z=9
n=["Kolhapur","Sangli","Satara","Pune","Mumbai","Thane","Nashik","Aurangabad","Ahmednagar"]
g = Graph(z,n) 
g.graph = [[ 0, 46, 121, 240,386,0,448,430,0 ], 
			[ 46, 0, 0, 230,374,0,246,433,320 ], 
			[ 121, 0, 0, 110,253,259,328,0,199 ], 
			[ 240, 0, 110, 0,0,154,0,235,121 ],
			[ 386, 374, 253, 150,0,0,167,346,262],
		    [ 0, 383, 0, 154,0,0,147,326,0 ],
		     [ 448, 246, 0, 212,167,147,0,191,157],
		      [ 430, 0, 313, 0, 346,0,191,0,0],
		       [ 319, 320, 0, 121,262,0,157,0,0 ]
		        
		    
		]; 
print("Number of cities:",z)
print("--------------------------------------------------------------------------------------------------------------")
print("Given adjacency matrix")
print("               ",end="")
for i in n:
	print(i.ljust(15),end="")
print()
for i in range(z):
	print(n[i].ljust(15),end="")
	for j in range(z):
		print(str(g.graph[i][j]).ljust(13),end="  ")
	print('')
print("--------------------------------------------------------------------------------------------------------------")
print("Enter the source city")
s1=input()


s=s1.capitalize()
for t in range(z):
    if s==n[t]:
        break
      
g.dijkstra(t,s); 

# This code is contributed by Divyanshu Mehta 
