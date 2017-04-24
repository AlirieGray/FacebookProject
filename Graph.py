from queue import Queue
import students
import networkx as nx
import random
import sys
from collections import Counter

def initialize_graph(local, A_matrix):
    # a list of Student objects, where each Student object has a list of attribute data called info
    student_info_list = students.initialize_student_list(local)

    # a list of all friendship connections in the school in the form [A, B], where A and B are friends
    friendships = students.create_friendships_list(A_matrix)

    G = nx.Graph()

    for friendship in friendships:
        G.add_node(int(friendship[0]), hasShared = False, hasSeen = False)
        G.add_node(int(friendship[1]), hasShared = False, hasSeen = False)
        G.add_edge(int(friendship[0]), int(friendship[1]))

    return G

# returns the number of people who see a post when it is shared initially to a node n
# with P being the likelihood that any given person will share the post (percentage)

def share_post(G, n, P, seen_so_far):
    # give a post to the node
    # if a node "sees" a post, that is, one of their friends has shared the post,
    # then increment the number of people who have seen it
    # and decide if they are also going to share it
    # if they are going to share it, add them to the queue

    q = Queue()
    q.put(n)

    while not q.empty():
        # dequeue the top node
        node = q.get()
        # the current node has now both seen and shared the post
        G.node[node]['hasShared'] = True
        G.node[node]['hasSeen'] = True

        # assume that all of the node's friends see the post
        # if a node hasn't yet seen the post, add them to the count of people that have seen it
        list_of_friends = G.neighbors(node)
        for student in list_of_friends:
            if not G.node[student]['hasSeen']:
                seen_so_far += 1
                G.node[student]['hasSeen'] = True

        # take roughly P percent of the node's friends
        select_friends = int(P * len(list_of_friends))

        # randomly pick up to select_friends to share with and add them to the queue
        for i in range (select_friends):
            r = random.randint(0, len(list_of_friends) - 1)
            # only share if the friend has not already shared the post before
            if not G.node[list_of_friends[r]]['hasShared']:
                G.node[list_of_friends[r]]['hasShared'] = False
                q.put(list_of_friends[r])
                seen_so_far += 1

        q.task_done()

    # return the number of people that have seen the post
    return seen_so_far

def clear_attributes(G):
    for node in G.nodes():
        G.node[node]['hasSeen'] = False
        G.node[node]['hasShared'] = False

# runs the share_post method on every node in the graph and returns the node that reaches the most people
def find_influencer(G):
    greatest = 0
    influencer = -1
    for node in G.nodes():
        influence = share_post(G, node, .10, 0)
        print (".")
        if influence > greatest:
            greatest = influence
            influencer = node
        clear_attributes(G)
    return influencer

# run the find_influencer method k times and find the node that is returned the most often
def probabilistic(G, k):
    node_list = []
    for i in range(k):
        n = find_influencer(G)
        node_list.append(n)
    count = Counter(node_list)
    return count.most_common()

def main():
    # test on Amherst data
    sys.setrecursionlimit(1500)
    g = initialize_graph("Amherst_local.csv", "Amherst_A.txt")
    print (probabilistic(g, 1))

if __name__ == "__main__":
    main()
