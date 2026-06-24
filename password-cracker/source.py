import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    result = OrderedDict()

    with open(input_file_name, 'r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            name, hash_value = row
            result[hash_value] = name

    cracked = OrderedDict()

    for password in range(1000, 10000):
        password_str = str(password)
        hashed = hashlib.sha256(password_str.encode()).hexdigest()
        if hashed in result:
            cracked[result[hashed]] = password_str

    with open(output_file_name, 'w') as outfile:
        for name, password in cracked.items():
            outfile.write(f"{name},{password}\n")


hash_password_hack('C:\\Users\\Asus\\Desktop\\Python\\Project\\rainbow_project_submission\\voroodi.csv', 'output.csv')


