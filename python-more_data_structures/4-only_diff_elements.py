#!/usr/bin/python3
def common_elements(set_1, set_2):
    qaqa = set_1.difference(set_2)
    qar = set_2.difference(set_1)
    common = qaqa.union(qar)
    return common
