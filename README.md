# Dijkstra-Algorithm
This is python implementation of Dijkstra shortest path finding algorithm in weighted graph. 
### Input:
Adjency matrix of the graph, Starting vertex, ending vertex
### output: 
Will show the vertices path between starting and ending vertices. 

# Test - 1 - Graph_1
![graph_1](https://user-images.githubusercontent.com/64163517/162205644-d29f246d-f0ef-4e7d-850d-03a24360b577.jpeg)


Input: dijkstra(graph,0,2)
Output: [0, 3, 4, 2]

Input: dijkstra(graph,3,2)
Output: [3, 4, 2]

Input: dijkstra(graph,0,4)
Output: [0, 3, 4]

Input: dijkstra(graph,0,1)
Output: [0, 3, 1]


# Test - 2 - Graph_2![graph_2](https://user-images.githubusercontent.com/64163517/162205618-d322786c-77d5-4bc1-8711-82192d65bc48.jpeg)

Input: dijkstra(graph_2,1,5)
Output: [1, 7, 5]

Input: dijkstra(graph_2,1,9)
Output: [1, 7, 9]

Input: dijkstra(graph_2,6,9)
Output: [6, 1, 7, 9]

Input: dijkstra(graph_2,0,9)
Output: [0, 1, 7, 9]