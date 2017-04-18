'''Info on data
Each of the school .mat files has an A matrix (sparse) and a
"local_info" variable, one row per node: a student/faculty status
flag, gender, major, second major/minor (if applicable), dorm/house,
year, and high school. Missing data is coded 0.'''

from __future__ import division

#constants
FILE_NAME = 'Caltech_local'
total_students = 769

#read text file
def prepare_text(FILE_NAME):
    with open(FILE_NAME) as file:
        text = file.read()
    return text

#create lists of students
def create_students(text):
    list_students = [] #list of all students where each student is a list
    lines = text.splitlines() #should return a list of strings
    for each_line in lines: #for each string in the list of strings append that string
        list_students.append(each_line.split()) #list of student is a list of lists of strings
    return list_students

def count_status(list_students):
    all_status = []
    for student in list_students:
        if int(student[0]) in all_status:
            pass
        else:
            all_status.append(int(student[0]))
    all_status = sorted(all_status)
    s = len(all_status)
    count_status = []
    for i in range(0, s):
        count_status.append(0)
    for student in list_students:
        for x in range(0, s):
            if int(student[0]) == int(all_status[x]):
                count_status[x] = count_status[x] + 1
    count_status_100 = []
    for c in count_status:
        count_status_100.append((round((c*100)/total_students,2)))
    all_status_info = []
    all_status_info.append(all_status)
    all_status_info.append(count_status)
    all_status_info.append(count_status_100)
    return all_status_info

def count_gender(list_students):
    all_gender = []
    for student in list_students:
        if int(student[1]) in all_gender:
            pass
        else:
            all_gender.append(int(student[1]))
    all_gender = sorted(all_gender)
    s = len(all_gender)
    count_gender = []
    for i in range (0, s):
        count_gender.append(0)
    for student in list_students:
        for x in range(0, s):
            if int(student[0]) == int(all_gender[x]):
                count_gender[x] = count_gender[x] + 1
    count_gender_100 = []
    for c in count_gender:
        count_gender_100.append((round((c*100)/total_students,2)))
    all_gender_info = []
    all_gender_info.append(all_gender)
    all_gender_info.append(count_gender)
    all_gender_info.append(count_gender_100)
    return all_gender_info

def count_major(list_students):
    all_major = []
    for student in list_students:
        if int(student[2]) in all_major:
            pass
        else:
            all_major.append(int(student[2]))
    all_status = sorted(all_major)
    s = len(all_major)
    count_major = []
    for i in range(0, s):
        count_major.append(0)
    for student in list_students:
        for x in range(0, s):
            if int(student[2]) == int(all_status[x]):
                count_major[x] = count_major[x] + 1
    count_major_100 = []
    for c in count_major:
        count_major_100.append((round((c*100)/total_students,2)))
    all_major_info = []
    all_major_info.append(all_major)
    all_major_info.append(count_major)
    all_major_info.append(count_major_100)
    return all_major_info

def count_secondmm(list_students):
    all_secondmm = []
    for student in list_students:
        if int(student[3]) in all_secondmm:
            pass
        else:
            all_secondmm.append(int(student[3]))
    all_secondmm = sorted(all_secondmm)
    s = len(all_secondmm)
    count_secondmm = []
    for i in range(0, s):
        count_secondmm.append(0)
    for student in list_students:
        for x in range(0, s):
            if int(student[3]) == int(all_secondmm[x]):
                count_secondmm[x] = count_secondmm[x] + 1
    count_secondmm_100 = []
    for c in count_secondmm:
        count_secondmm_100.append((round((c*100)/total_students,2)))
    all_secondmm_info = []
    all_secondmm_info.append(all_secondmm)
    all_secondmm_info.append(count_secondmm)
    all_secondmm_info.append(count_secondmm_100)
    return all_secondmm_info

def count_housing(list_students):
    all_housing = []
    for student in list_students:
        if int(student[4]) in all_housing:
            pass
        else:
            all_housing.append(int(student[4]))
    all_housing = sorted(all_housing)
    w = len(all_housing)
    count_housing = []
    for i in range(0, w):
        count_housing.append(0)
    for student in list_students:
        for x in range(0, w):
            if int(student[4]) == int(all_housing[x]):
                count_housing[x] = count_housing[x] + 1
    count_housing_100 = []
    for c in count_housing:
        count_housing_100.append((round((c*100)/total_students,2)))
    all_housing_info = []
    all_housing_info.append(all_housing)
    all_housing_info.append(count_housing)
    all_housing_info.append(count_housing_100)
    return all_housing_info

def count_year(list_students):
    all_year = []
    for student in list_students:
        if int(student[5]) in all_year:
            pass
        else:
            all_year.append(int(student[5]))
    all_year = sorted(all_year)
    y = len(all_year)
    count_year = []
    for i in range(0, y):
        count_year.append(0)
    for student in list_students:
        for x in range(0, y):
            if int(student[5]) == int(all_year[x]):
                count_year[x] = count_year[x] + 1
    count_year_100 = []
    for c in count_year:
        count_year_100.append((round((c*100)/total_students,2)))
    all_year_info = []
    all_year_info.append(all_year)
    all_year_info.append(count_year)
    all_year_info.append(count_year_100)
    return all_year_info

def count_highschool(list_students):
    all_highschool = []
    for student in list_students:
        if int(student[6]) in all_highschool:
            pass
        else:
            all_highschool.append(int(student[6]))
    all_highschool = sorted(all_highschool)
    z = len(all_highschool)
    count_highschool = []
    for i in range(0, z):
        count_highschool.append(0)
    for student in list_students:
        for x in range(0, z):
            if int(student[6]) == int(all_highschool[x]):
                count_highschool[x] = count_highschool[x] + 1
    count_highschool_100 = []
    for c in count_highschool:
        count_highschool_100.append((round((c*100)/total_students,2)))
    all_highschool_info = []
    all_highschool_info.append(all_highschool)
    all_highschool_info.append(count_highschool)
    all_highschool_info.append(count_highschool_100)
    return all_highschool_info

#student_list = create_students(prepare_text(FILE_NAME))
#print(student_list)
#print(count_status(student_list))
#print(count_gender(student_list))
#print(count_major(student_list))
#print(count_secondmm(student_list))
#print(count_housing(student_list))
#print(count_year(student_list))
#print(count_highschool(student_list))

def main():

    list_students = create_students(prepare_text(FILE_NAME))

    count_status_list = count_status(list_students)
    status_name = count_status_list[0]
    status_score = count_status_list[2]

    count_gender_list = count_gender(list_students)
    gender_name = count_gender_list[0]
    gender_score = count_gender_list[2]

    count_major_list = count_major(list_students)
    major_name = count_major_list[0]
    major_score = count_major_list[2]

    count_secondmm_list = count_secondmm(list_students)
    secondmm_name = count_secondmm_list[0]
    secondmm_score = count_secondmm_list[2]

    count_housing_list = count_housing(list_students)
    housing_name = count_housing_list[0]
    housing_score = count_housing_list[2]

    count_year_list = count_year(list_students)
    year_name = count_year_list[0]
    year_score = count_year_list[2]

    count_highschool_list = count_highschool(list_students)
    highschool_name = count_highschool_list[0]
    highschool_score = count_highschool_list[2]

    list_all_names = []
    list_all_names.append(status_name)
    list_all_names.append(gender_name)
    list_all_names.append(major_name)
    list_all_names.append(secondmm_name)
    list_all_names.append(housing_name)
    list_all_names.append(year_name)
    list_all_names.append(highschool_name)

    list_all_scores = []
    list_all_scores.append(status_score)
    list_all_scores.append(gender_score)
    list_all_scores.append(major_score)
    list_all_scores.append(secondmm_score)
    list_all_scores.append(housing_score)
    list_all_scores.append(year_score)
    list_all_scores.append(highschool_score)

    print(list_all_names)
    print(list_all_scores)

    #dict_index = 0
    dict_status = {}
    length = len(list_all_scores[0]) - 1
    j = 0
    for i in list_all_names[0]:
        dict_status[i] = 0

    #dict_status = dict.fromkeys(list_all_names[0][i], list_all_scores[0][j])
    print(dict_status)

if __name__ == '__main__':
    main()
