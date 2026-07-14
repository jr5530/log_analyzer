
from reader import read_csv_to_list
def filter_sensitive_ports(data1):
    sensitive_ports = {"22", "23", "3389"}
    res = [log for log in data1 if log[3] in sensitive_ports]
    return res
# print(filter_sensitive_ports(read_csv_to_list("network_traffic.log")))
