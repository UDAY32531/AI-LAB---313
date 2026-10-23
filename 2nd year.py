#AI LAB (2nd YEAR 3rd SEM)
# 5 MIN MAX
"""def minimax(depth, node_index ,is_max,score,height):
    if depth == height:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
             minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

scores = [3,5,2,9,69,5,23,63]
height =3

best_value = minimax(0, 0, True, scores, height)

print("The optimal value is:", best_value)"""



# ALPHA BETA
"""
import math

# Alpha-Beta Pruning Function
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):
    # Base Case: Leaf node reached
    if depth == height:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta,
                height
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Beta Cut-off
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta,
                height
            )
            best = min(best, value)
            beta = min(beta, best)

            # Alpha Cut-off
            if beta <= alpha:
                break

        return best


# Main Program
values = list(map(int, input("Enter 8 leaf node values: ").split()))
height = 3
result = alpha_beta(
    0,
    0,
    True,
    values,
    -math.inf,
    math.inf,
    height
)
print("\nOptimal Value:", result)"""
# 4 A* STAR
"""import heapq
def a_star(graph,heuristic,start,goal):
    open_list =[(heuristic[start],start)]

    g_score = {node:float('inf')for node in graph}
    g_score[start]=0

    parent = {start:None}

    while open_list :
        _, current= heapq.heappop(open_list)

        if current== goal:
            path=[]
            while current is not None:
                path.append(current)
                current=parent[current]
            return path[::-1],g_score[goal]
        for neighbour,cost in graph[current]:
            tentative_g =g_score[current]+cost

            if tentative_g < g_score[neighbour]:
                g_score[neighbour] = tentative_g
                parent[neighbour]= current

                f_score= tentative_g + heuristic[neighbour]
                heapq.heappush(open_list,(f_score,neighbour))

    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic values: estimated distance to goal D
heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

start = 'A'
goal = 'D'

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")"""

# 3 HILL CLIMB
"""def objective_function(x):
    return -4 * (x - 5)**2 + 100

def hill_climbing(start, step_size, max_iteration):
    current = start
    current_value = objective_function(current)
    
    for i in range(max_iteration):
        left = current - step_size
        right = current + step_size
        
        left_value = objective_function(left)
        right_value = objective_function(right)
        
        if left_value > current_value:
            current = left
            current_value = left_value
        
        elif right_value > current_value:
            current = right
            current_value = right_value
        
        else:
            break
            
    return current, current_value
start = float(input("Enter the starting value: "))
step_size = float(input("Enter the step size: "))
max_iteration = int(input("Enter maximum iterations: "))
best_position, best_value = hill_climbing(start, step_size, max_iteration)

print(f"\nBest position = {best_position}")
print(f"Maximum value = {best_value}")"""


# 2 DFS
"""def dfs(graph, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        current_node = stack.pop(0)
        
        if current_node not in visited :
            print(f"Exploring Node: {current_node}")
            visited.append(current_node)
            
            for neighbour in graph.get(current_node, []):
                if neighbour not in visited and neighbour not in stack:
                    stack.append(neighbour)
                    
    return visited

print("---Build Your Graph")
student_graph = {}

num_edges = int(input("How many edges does your graph have?"))

print("Enter each edge separated by a space(e,g., A B):")

for i in range(num_edges):
    u, v  = input(f"Edge {i + 1}:").split()
    
    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []
    
    student_graph[u].append(v)
    student_graph[v].append(u)
    
start = input("Enter the starting node for BFS:")

print(f"\nYour Graph Dictionary: {student_graph}")
print("Starting DFS Traversal...")

dfs(student_graph, start)"""


# 1 BFS
"""def bfs(graph, start_node):
    visited = []
    queue = [start_node]
    
    while queue:
        current_node = queue.pop(0)
        
        if current_node not in visited :
            print(f"Exploring Node: {current_node}")
            visited.append(current_node)
            
            for neighbour in graph.get(current_node, []):
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)
                    
    return visited

print("---Build Your Graph")
student_graph = {}

num_edges = int(input("How many edges does your graph have?"))

print("Enter each edge separated by a space(e,g., A B):")

for i in range(num_edges):
    u, v  = input(f"Edge {i + 1}:").split()
    
    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []
    
    student_graph[u].append(v)
    student_graph[v].append(u)
    
start = input("Enter the starting node for BFS:")

print(f"\nYour Graph Dictionary: {student_graph}")
print("Starting BFS Traversal...")

bfs(student_graph, start)"""




# PRACTICE 
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_result(self):
        print(self.name, "scored", self.marks)

s1 = Student("Uday", 85)
s1.show_result()"""

"""
l=[0,2,1]
for i in range(max(l)+2):
    if i in l :
        pass
    else:
        print("missing number is",i)
"""


"""arr=[1,8,6,2,5,4,8,3,7]
area=0
i=0
j=len(arr)-1
while(i!=j):
    h=min(arr[i],arr[j])
    l=j-i
    a=h*l
    area=max(a,area)
    if arr[i] < arr[j]:
        i=i+1
    else:
        j=j-1
    print("!\n")
print(area)"""

#bucket with most water 
"""arr=[1,8,6,2,5,4,8,3,7]
area=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        h=min(arr[i],arr[j])
        l=j-i
        a=h*l
        area=max(a,area)
    print("*")
print(area)"""




"""x=[-6,-5,4,5,2]
max=x[0]
smax=x[1::][0]
tmax=x[2::][0]
for i in x:
    if i<0:
        i=-i
    if i >max:
        tmax=smax
        smax=max
        max=i
    if i<max and i>=smax:
        tmax=smax
        smax=i
    if i<smax and i>=tmax:
        tmax=i

print(max)
print(smax)
print(tmax)
print(max*smax*tmax)"""








"""x=[10,2,1,8,9]
max=x[0]
smax=x[1::][0]
tmax=x[2::][0]
for i in x:
    if i >max:
        tmax=smax
        smax=max
        max=i
    if i<max and i>smax:
        tmax=smax
        smax=i
    if i<smax and i>tmax:
        tmax=i
print(max)
print(smax)
print(tmax)"""


"""print(max)
print(smax)
"""

#TO FIND THE MIDDLE MOST ELEMENT IN A LIST 
"""x=[1,2,3]
y=[4,5,6,7]
z=x+y
if len(z)%2!=0:
    p=int(len(z)/2)
    print(z[p])
else:
    p=int(len(z)/2)
    q=int((len(z)/2) -1)
    print((z[p]+z[q])/2)
print(z)"""

"""numbers = [1, 2, 3, 4, 5, 6]
print([i*i for i in numbers if i%2==0])"""


"""l=[1,2,3,4,5,6,7,8]
for i in l:
    print(i,end=" ")"""

"""print("hello i am uday bhaskar")
#SELECTION )(*&^%$#@!!@#$%^&*()
list=[64,22,11,2,1,4]
n=6
for i in range(n-1):
    minindex=i
    for j in range(i+1,n):
        if(list[j]<list[minindex]):
            minindex=j
        temp=list[i]
        list[i]=list[minindex]
        list[minindex]=temp
print(list)"""



"""for i in range(6):
    for j in range(6):
        if(i==0 or i==5 or j==0 or j==5):
            print("!",end=" ")
        else:
            print("#",end=" ")
    print(" ")"""


from functools import reduce
"""d=[1,2,3,4,5,6,8,9,10]
f=filter(lambda x:x%2==0,d)
m=map(lambda x:x*2,d)
r=reduce(lambda x,y:x+y,d)
print(list(f),list(m),r)"""

#find the frequency of each char out put as char:count
"""x=input("enter a string")
l=[]
for i in range(len(x)):
    if(x[i]not in l):
        l.append(x[i])
        print(x[i],x.count(x[i]))"""

#find first non repeating character
"""s=input("enter a string")
for i in range(len(s)):
    if(s.count(s[i])==1):
        print(s[i])
        break"""

#Anagram strings
"""s="listen"
k="silent"
c=0
if len(s)==len(k):
    for i in s:
        if i in k:
            c=c+1
        else:
            print("not anagrams")
            break
    if(c==len(s)):
        print("anagram")
else:
    print("not anagrams len wise")"""

# Remove duplicate characters in a string
"""s="udayu 12 12"
l=[]
for i in range(len(s)):
    if(s[i] not in l):
        l.append(s[i])
print("".join(l))
"""
#palindrome number 
"""x=int(input("enter a number"))
rev=0
x1=x
while(x>0):
    r=x%10
    rev=rev*10+r
    print(rev)
    x=x//10
if(rev==x1):
    print("palindrome")
else:
    print("not a palindrome")
"""
#perfect number
"""x=int(input("enter a number"))
s=0
for i in range(1,int(x/2)+1):
    if (x%i==0 and i%2==0):
        s=s+i
if (s==x):
    print("perfect number")
else:
    print("not a perfect  number")"""
    
#Wap sort the char of string and first alphabet symbols
#followed by numberic values za23no -----> anoz23 
"""s="z a 2  3 n o"
a=[]
n=[]
for i in range(len(s)):
    if s[i].isalpha():
        a.append(s[i])
    else:
        n.append(s[i])
print("".join(sorted(a)+sorted(n)))"""

#Wap to print the second largest and second smallest element in a list of
#10 integers without using sort function
"""l=[]
for _ in range(10):
    l.append(int(input("enter")))
print(l)    
for i in range(10):
    for j in range(10):
        if l[i]<l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
print("second largest","=",l[8],"second smallest","=",l[1])"""

#Wap to create two lists each containing 5 elements.
#print both the lists one element from each list combined at a time
"""a=[1,2,3,4,5]
b=["a","b","c","d","e"]
x=[]
for i in range(5):
    x.append(a[i])
    x.append(b[i])
print(x)"""

