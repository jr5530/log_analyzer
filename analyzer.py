import reader

def check_outsiders_ip(data):
    res = [log[1] for log in data if log[1][:3] != "10." and log[1][:7] != "192.168"]
    return res

def filter_by_size(data):
    res = [log for log in data if int (log[5]) > 5000]
    return res

def tag_traffic(data):
    res = ["LARGE" if int(log[5]) > 5000 else "NORMAL" for log in data]
    return res
# print(tag_traffic(reader.read_csv_to_list("network_traffic.log")))

from collections import Counter

def count_source_ips_fast(data):
    return dict(Counter(log[1] for log in data))
print(count_source_ips_fast(reader.read_csv_to_list("network_traffic.log")))
