import os
import shutil

def delete_file():
    list = os.listdir("knn_examples/test")
    number_files = len(list)

    if number_files >= 100:
        shutil.rmtree("knn_examples/test")
        print("clean!!")