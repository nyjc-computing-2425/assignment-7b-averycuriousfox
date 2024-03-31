# Built-in imports
import math
from os import read

# Your code below
GRADE = {}
for i in range(101):
    if i >= 70:
        GRADE[i] = "A"
    elif 60 <= i < 70:
        GRADE[i] = "B"
    elif 55 <= i < 60:
        GRADE[i] = "C"
    elif 50 <= i < 55:
        GRADE[i] = "D"
    elif 45 <= i < 50:
        GRADE[i] = "E"
    elif 40 <= i < 45:
        GRADE[i] = "S"
    else:
        GRADE[i] = "U"


def read_testscores(filename):
    """
    This function takes in a string "filename" and read the data in the file "filename". This function then return a list of dictionaries representing data from each row of file "filename".

    Parameters
    ----------
    filename:
        a string of the name of the file "filename"

    Returns
    -------
    list,dict:
        A list of dictionaries with each dictionary representing each row in the file "filename"

    Examples
    --------
    >>> studentdata = read_testscores('testscores.csv')
    >>> studentdata[0]['class']
    'Class1'
    >>> studentdata[0]['name']
    'Student1'
    >>> studentdata[0]['overall']
    51
    >>> studentdata[0]['grade']
    'D'
    """
    total_data = []
    with open(filename,"r") as f:
        headline = f.readline().split(",")
        for line in f.readlines():
            line = line.split(",")
            points = [line[2],line[3],line[4],line[5]]
            data_dict = {}
            data_dict["class"] = line[0]
            data_dict["name"] = line[1]
            data_dict["overall"] = math.ceil(((int(points[0])/30)*15) + ((int(points[1])/40)*30) + ((int(points[2])/80)*35) + ((int(points[3])/30)*20))
            data_dict["grade"] = GRADE[data_dict["overall"]]
            total_data.append(data_dict)
    return total_data


def analyze_grades(studentdata):
    """
    This function takes a list of dictionaries "studentdata" and returns a dictionary representing the number of each grade for each class.

    Parameter
    ---------
    list:
        a list of dictionaries "studentdata"

    Returns
    -------
    dict:
        a dictionary representing the number of each grades in each class

    Examples
    --------
    >>> analysis = analyze_grades(studentdata)
    >>> analysis['Class1']['A']
    4
    >>> analysis['Class18']['U']
    0
    """
    total_data = {}
    for class_data in studentdata:
        class_name = class_data["class"]
        student_grade = class_data["grade"]
        if class_name in total_data:
            total_data[class_name][student_grade] += 1
        else:
            total_data[class_name] = {"A": 0,
                                     "B": 0,
                                     "C": 0,
                                     "D": 0,
                                     "E": 0,
                                     "S": 0,
                                     "U": 0}
            total_data[class_name][student_grade] += 1
    return total_data


