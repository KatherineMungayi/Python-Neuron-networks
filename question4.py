
import networkx as nx
import matplotlib as plt
from sys import argv
from heapq import heappush,heappop
g=nx.Graph

def UCS(graph, s, goal):
	# define dummy variables for use
	nodesQ = []
	visited_nodes = {}
	prev_nodes = {}

	# using heap for mainitng a queue
	heappush(nodesQ,(0,s,None,0))
	for nodes in graph:
		visited_nodes[nodes] = False
		prev_nodes[nodes] = None
	i = 1
	# mark all visited and previous nodes False and None
	while len(nodesQ) != 0:
		# pop the least cost node from heap and analyse it
		
		i = i+1
		total_cost, current_node, prev_node, link_cost = heappop(nodesQ)
		if visited_nodes[current_node] == False:
			visited_nodes[current_node] = True
			prev_nodes[current_node] = []
			prev_nodes[current_node].append(prev_node)
			prev_nodes[current_node].append(link_cost)
			# if goal return the total route
			if current_node == goal:
				final = []
				while current_node != s:
					temp = []
					temp.append(current_node)
					for i in prev_nodes[current_node]:
						temp.append(i)
					final.append(temp)
					current_node = prev_nodes[current_node][0]
				final.reverse()
				# retrn total cost and final path
				return total_cost,final
			# else explore neighbours
			for neighbors, ncost in graph[current_node].items():
				if visited_nodes[neighbors] == False:
					this_link_cost = ncost
					new_cost = total_cost + ncost
					heappush(nodesQ, (new_cost, neighbors, current_node, ncost))
	# return none if no path found

	return None
	pass
def main(file, arg1, arg2):
	# checking arguments for processing
	try:
		filename=file
		Source=arg1
		Destination=arg2
	except IndexError:
		
		return 0
	# open file and make data ready for analysis
	file = open(filename, 'r')
	filedata = file.readlines()
	# make a dictionary of graph
	filedata = [x.strip().split() for x in filedata]
	# if end of file then remove the last line
	if filedata[-1:][0][0] == 'END':
		filedata.pop()

	# empty graph
	G = {}
	for rec in filedata:
		src = rec[0]
		dest = rec[1]
		cst = rec[2]
		if src not in G:
			G[src] = {}
		if dest not in G:
			G[dest] = {}
		# create src and dest nodes with its length from input file
		G[src][dest] = int(cst)
		G[dest][src] = int(cst)

	# call the UCS function
	result = UCS(G,Source,Destination)

	print 
"\n\nFinal output: \n"
	# print the result in the required format
if result == None:
		print ; "\ndistance: infinity\nroute:\nnone\n"
else:
	print ; "\ndistance:",result[0],"km\nroute:"
	for line in result[1]:
         print; "%s to %s, %s km" % (line[1],line[0],line[2])
	print ;""
pass
# With valid path

main('input.txt','Sports Complex','Parking Lot')

