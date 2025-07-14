import os
import numpy as np
from ipdb import set_trace

def get_data_lists(txt_path, num_column = 2):
    # set_trace()
    data_lists = [[] for _ in range(num_column)]
    if os.path.exists(txt_path):
        with open(txt_path, "r") as f:
            lines = f.readlines()
        for line in lines:
            tmp_list = line.strip().split("\t")
            assert len(tmp_list) == num_column, tmp_list + " has error."
            for i in range(num_column):
                data_lists[i].append(tmp_list[i])
    return data_lists


def calculate_growth_rate(data):
    # 判断数据长度，确保至少有两个数据点
    if len(data) < 2:
        raise ValueError("数据长度必须至少为2")
    
    # 计算增长率
    growth_rate = [0] + [(data[i] - data[i-1]) / data[i-1] * 100 for i in range(1, len(data))]
    
    return growth_rate