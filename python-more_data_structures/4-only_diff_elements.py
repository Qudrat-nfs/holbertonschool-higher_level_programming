#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    qaqa = set_1.difference(set_2)
    qar = set_2.difference(set_1)
    only = qaqa.union(qar)
    return only
