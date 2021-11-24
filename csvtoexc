import pandas as pd
import os

def get_filepaths(directory = "C:/Users/erenb/Desktop/Pro"):

    fname = ""

    for root, directories, files in os.walk(directory):
        for filename in files:

            r_buf = root

            fname = root.replace(root.rsplit('\\', 1)[0], '')
            fname = fname.replace("\\", '')

            r_buf = r_buf.replace("\\", "/")

            read_file = pd.read_csv(r_buf + '/' + files[0])
            read_file.to_excel(r_buf + '/' + fname + '.xlsx', index=None, header=True)

get_filepaths()
