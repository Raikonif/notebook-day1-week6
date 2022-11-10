from os import listdir
from os.path import isfile, join
import csv


def discover_data_files(path='../data', pattern='csv'):
    return [join(path, f) for f in listdir(path) if isfile(join(path, f)) and f.endswith('csv')]


def read_file(files):
    readers = []
    for  f in files:
        csv_file = open(f, encoding='UTF-16')
        readers.append((f, csv.reader(csv_file, delimiter='\t')))
    return readers
