import csv
FILE = "Caltech_A.txt"

# a student object has a list of attributes
class Student(object):
    def __init__(self, local_info):
        self.info = local_info
        self.hasSharedPost = False

def create_student(attributes):
    return Student(attributes)

# returns a list of all edges in the school in the form [A,B] where A and B are friends
def create_friendships_list(file):
    text_file = open(file, "r")
    friendships = text_file.read().split('\n')
    edges = []

    for friendship in friendships:
        pair = []
        pair.append((friendship.split(' '))[0])
        pair.append((friendship.split(' '))[1])
        edges.append(pair)

    return edges

def prepare_csv_local(filename_data):
    local_list = []
    with open(filename_data) as f:
        reader = csv.reader(f)
        for row in reader:
            local_list.append(row)
    return local_list


def initialize_student_list(local):
    local_info = (prepare_csv_local(local))
    students = []

    for info in local_info:
        students.append(create_student(info))

    return students

def main():
    pass

if __name__ == "__main__":
    main()