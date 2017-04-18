import students
import networkx as nx
import random
import sys

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

def share_post(G, n, P, seen_so_far):
    # give a post to the node
    # P is the likelihood that any given person will share the post (percentage)
    # if a node "sees" a post, that is, one of their friends has shared the post,
    # then increment the number of people who have seen it
    # and decide if they are also going to share it

    G.node[n]['hasShared'] = True
    G.node[n]['hasSeen'] = True

    # assume that all of the node's friends see the post
    # if a node has already seen the post, don't add it to the count of people that have seen it
    list_of_friends = G.neighbors(n)
    for student in list_of_friends:
        if not G.node[student]['hasSeen']:
            seen_so_far += 1
            G.node[student]['hasSeen'] = True

    # take roughly P percent of the node's friends
    select_friends = int (P * len(list_of_friends))

    # randomly pick up to select_friends to share with
    for i in range (select_friends):
        r = random.randint(0, len(list_of_friends) - 1)
        # only share if the friend has not already shared the post before
        if not G.node[list_of_friends[r]]['hasShared']:
            G.node[list_of_friends[r]]['hasShared'] = False
            seen_so_far = share_post(G, list_of_friends[r], P, seen_so_far)

    # return the number of people that have seen the post
    print (".")
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
        if influence > greatest:
            greatest = influence
            influencer = node
        clear_attributes(G)
    return influencer

def main():
    # test on Amherst data
    sys.setrecursionlimit(1500)
    g = initialize_graph("Amherst_local.csv", "Amherst_A.txt")
    print (find_influencer(g))

if __name__ == "__main__":
    main()
