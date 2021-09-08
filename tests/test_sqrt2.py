import os

import run_test

# Open Data File and read the binary data of e
data_path = os.path.join(os.getcwd(), 'data', 'data.sqrt2')

with open(data_path) as f:
    binary_data = f.read().replace("\n", "").replace(" ", "")

run_test.test_data(binary_data)
