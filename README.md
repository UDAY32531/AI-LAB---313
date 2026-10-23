# AI-LAB---313

HELLO GUYS I AM UDAY BHASKAR 
PLEASE HAVE A LOOK ON THE 
REPO

CONTENTS :




1.
The BFS traversal

PART - 1

GOAL - Explore a graph level-by-level starting from a specific node , ensuring we don't visit the same node twice

Algo- BFS ( graph, start_node)

1. Create a empty list is called VISITED 
2. Create a list Queue and start_node as the first item
3. While the Queue is not empty , do

    a. current_node = Remove the first item from the front of the Queue
    b. IF current_node is NOT in VISITED

        i. PRINT "Expploring node: " + current_node
        ii. Add current_node to the VISITED list
        iii. **FOR EACH** `neighbor` in `current_node` in the `graph`:
            1. **IF** `neighbour` is **NOT** in `VISITED` and `neighbour` is **NOT** in
                `QUEUE`:

                    a. Add `neighbour` to the back of the `QUEUE`:

4. RETURN the VICITED list

PART - 2: 

The Main Program(interactive Graph Builder)

GOAL: Ask the user to define the connection (edges) of a graph, store them as an adjacency list (dictionary/map), and then run the traversal.

Algo: Main Program()

PRINT "---Build Your Graph---"

1. Create an empty dictionary/map called student_graph
2. PRINT "How many edges (connections) does your graph have?"
3. num_edges = Get interger input from the user
4. PRINT "Enter each edge separated by a space:"
5. Loop from 1 to num_edges:

    a.Get input from the user and split it into two variables: u and v.

    b. Check and Initialize Nodes:
        i. IF u does exist in student_graph:
            1. Add u to student_graph with an empty lsit.
        ii. IF v does not exist in student_graph:
            1. Add v to student_graph with an empty list
    c. Create a undirected Connection (Two-Way Street):
        i. Add v to u's of neighbours.
        ii. Add u to v's list of neighbours.

6. PRINT "Enter the starting node for BFS:"

7. start = Get input from the user.

8. PRINT "YOURTIONARY:" + student_graph

9. PRINT "Starting BFS Travasal.."

10. Call BFS_Traversal (student_graph, start)
