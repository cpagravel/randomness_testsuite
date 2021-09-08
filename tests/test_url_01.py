import os
from nist80022.Tools import Tools

import run_test

# Open Data File and read the binary data of e
data_path = os.path.join(os.getcwd(), 'data', 'test_data_01.txt')

with open(data_path) as f:
    test_data = f.read().replace("\n", "").replace(" ", "")

run_test.test_data(Tools.string_to_binary(test_data))
