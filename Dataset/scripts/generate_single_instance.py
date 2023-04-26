# Path: generate_dataset.py
import random
from parse_instance import parse_instance
import statistics 

BASE_GROUP_PATH = "../base_group/"
FILENAMES_PATH = "./filenames.txt"

"""
sorry but in functions here n is n, wmax is c, V is C and W is V
"""


def very_large_n(arguments):
    n_min, n_max, base_group_path, filenames_path = arguments
    """
    This function generates an instance of the dataset with a very large n. The
    parameters c, C & V are taken randomly from a file in base_group
    """
    # base_group is a folder with files of instances, the filenames are stored
    # in filenames.txt
    with open(filenames_path, "r") as f:
        filenames = f.readlines()
    # we have to choose a random file from the base_group_path
    filename = filenames[random.randint(0, len(filenames)-1)][:-1]
    # now we have to open the file and read the values of c, C & V
    optimum, n, c, C, V = parse_instance(base_group_path+filename)
    # C_min = min(C)
    # C_max = max(C)
    # V_min = min(V)
    # V_max = max(V)
    C_avg = statistics.mean(C)
    V_avg = statistics.mean(V)

    if V_avg < 50:
        V_avg = 50
    if C_avg < 50:
        C_avg = 50
    # now we have to generate a random n between n_min and n_max
    n = random.randint(n_min, n_max)
    for i in range(len(C), n):
        C.append(random.randint(C_avg-50, C_avg+50))
        V.append(random.randint(V_avg-50, V_avg+50))
    return [n, c, C, V]


def very_large_wmax(arguments):
    c_min, c_max, base_group_path, filenames_path = arguments
    """
    This function generates an instance of the dataset with a very large c. The
    parameters n, C & V are taken randomly from a file in base_group
    """
    # base_group is a folder with files of instances, the filenames are stored
    # in filenames.txt
    with open(filenames_path, "r") as f:
        filenames = f.readlines()
    # we have to choose a random file from the base_group_path
    filename = filenames[random.randint(0, len(filenames)-1)][:-1]
    # now we have to open the file and read the values of c, C & V
    optimum, n, c, C, V = parse_instance(base_group_path+filename)
    c = random.randint(c_min, c_max)
    # C_min = min(C)
    # C_max = max(C)
    # V_min = min(V)
    # V_max = max(V)
    C_avg = statistics.mean(C)
    V_avg = statistics.mean(V)

    if V_avg < 50:
        V_avg = 50
    if C_avg < 50:
        C_avg = 50
    # now we have to generate a random n between n_min and n_max
    for i in range(len(C), n):
        C.append(random.randint(C_avg-50, C_avg+50))
        V.append(random.randint(V_avg-50, V_avg+50))
        # if i%100==0:
    # print(n, c, len(C), len(V))
    # assert(len(C)==n)
    return [n, c, C, V]


def very_large_n_and_wmax(arguments):
    n_min, n_max, c_min, c_max, base_group_path, filenames_path = arguments
    """
    This function generates an instance of the dataset with a very large n and
    c. The parameters C & V are taken randomly from a file in base_group
    """
    # base_group is a folder with files of instances, the filenames are stored
    # in filenames.txt
    with open(filenames_path, "r") as f:
        filenames = f.readlines()
    # we have to choose a random file from the base_group_path
    filename = filenames[random.randint(0, len(filenames)-1)][:-1]
    # now we have to open the file and read the values of c, C & V
    optimum, n, c, C, V = parse_instance(base_group_path+filename)
    n = random.randint(n_min, n_max)
    c = random.randint(c_min, c_max)
    # C_min = min(C)
    # C_max = max(C)
    # V_min = min(V)
    # V_max = max(V)
    C_avg = statistics.mean(C)
    V_avg = statistics.mean(V)

    if V_avg < 50:
        V_avg = 50
    if C_avg < 50:
        C_avg = 50
    # now we have to generate a random n between n_min and n_max
    for i in range(len(C), n):
        C.append(random.randint(C_avg-50, C_avg+50))
        V.append(random.randint(V_avg-50, V_avg+50))
    return [n, c, C, V]


def very_large_valued_V(arguments):
    ci_min, ci_max, base_group_path, filenames_path = arguments
    """
    This function generates an instance of the dataset with a very large valued
    C. The parameters n, c & V are taken randomly from a file in base_group
    """
    # base_group is a folder with files of instances, the filenames are stored
    # in filenames.txt
    with open(filenames_path, "r") as f:
        filenames = f.readlines()
    # we have to choose a random file from the base_group_path
    filename = filenames[random.randint(0, len(filenames)-1)][:-1]
    # now we have to open the file and read the values of c, C & V
    optimum, n, c, C, V = parse_instance(base_group_path+filename)
    # V_min = min(V)
    # V_max = max(V)
    V_avg = statistics.mean(V)
    # now we have to generate a random n between n_min and n_max
    for i in range(len(C), n):
        C.append(random.randint(ci_min, ci_max))
        V.append(random.randint(V_avg-50, V_avg+50))
    return [n, c, C, V]


def very_large_valued_W(arguments):
    vi_min, vi_max, base_group_path, filenames_path = arguments
    """
    This function generates an instance of the dataset with a very large valued
    V. The parameters n, c & C are taken randomly from a file in base_group
    """
    # base_group is a folder with files of instances, the filenames are stored
    # in filenames.txt
    with open(filenames_path, "r") as f:
        filenames = f.readlines()
    # we have to choose a random file from the base_group_path
    filename = filenames[random.randint(0, len(filenames)-1)][:-1]
    # now we have to open the file and read the values of c, C & V
    optimum, n, c, C, V = parse_instance(base_group_path+filename)
    # C_min = min(C)
    # C_max = max(C)
    C_avg = statistics.mean(C)
    c = random.randint(vi_min, vi_max)*100
    # now we have to generate a random n between n_min and n_max
    for i in range(len(C), n):
        C.append(random.randint(C_avg-50, C_avg+50))
        V.append(random.randint(vi_min, vi_max))
    return [n, c, C, V]


def very_large_valued_V_and_W(arguments):
    ci_min, ci_max, vi_min, vi_max, base_group_path, filenames_path = arguments
    """
    This function generates an instance of the dataset with a very large valued
    C & V. The parameters n & c are taken randomly from a file in base_group
    """
    # base_group is a folder with files of instances, the filenames are stored
    # in filenames.txt
    with open(filenames_path, "r") as f:
        filenames = f.readlines()
    # we have to choose a random file from the base_group_path
    filename = filenames[random.randint(0, len(filenames)-1)][:-1]
    # now we have to open the file and read the values of c, C & V
    optimum, n, c, C, V = parse_instance(base_group_path+filename)
    c = random.randint(vi_min, vi_max)*100
    # now we have to generate a random n between n_min and n_max
    for i in range(len(C), n):
        C.append(random.randint(ci_min, ci_max))
        V.append(random.randint(vi_min, vi_max))
    return [n, c, C, V]
