
# a student object has a list of friend connections, a list of attributes,
# and a number of friends variable
class Student(object):
    def __init__(self, matrix_A, local_info):
        self.edge_array = matrix_A
        self.student_info = local_info
        # find out how many friends the student has
        count = 0
        for possible_edge in self.edge_array:
            if self.edge_array[possible_edge] == 1:
                count = count + 1
        self.number_friends = count

# reads in a text file with the A matrix
# which is a matrix of the connections between students
# and creates a list, for which every element is a list that represents a student
# and contains their connection data
# a 1 at a given index in that list indicates that a student is friends with the student at that index
# in the enclosing list
def read_in_A_matrix(file, number_students):
    text_file = open(file, "r")
    lines = text_file.read().split('\n')
    student_edges_list = []

    # initialize each student's list of friends to all zeroes
    for i in range (number_students):
        new_student_edges = [0] * number_students
        student_edges_list.append(new_student_edges)

    # then find the indexes at which each student has a connection and set the value at those indexes to 1
    for i in range (len(lines) - 1):
        first =(int(((lines[i]).split(' '))[0]) -1)
        second =( int(((lines[i]).split(' '))[1]) -1 )
        student_edges_list[first][second] = 1

    #test
    #print the first student's array of friend links
    print (student_edges_list[0])
    #first student is friends with the fifth student
    print(student_edges_list[0][4])
    #therefore fifth student is friends with the first student
    print(student_edges_list[4][0])

def read_in_local_info(filename, number_students):
    # read in the local info matrix as a list
    with open(filename) as file:
        lines = file.read().splitlines()
    print ("lines: ", lines)

def create_student(edges, attributes):
    pass

def main():
    # test on caltech data
    read_in_A_matrix("caltech.txt", 770)
    read_in_local_info("", 770)

if __name__ == "__main__":
    main()