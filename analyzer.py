import reader

def check_outsiders_ip(data):
    res = [log[1] for log in data if log[1][:3] != "10." and log[1][:7] != "192.168"]
    return res

def filter_by_size(data):
    res = [ log for log in data if int (log[5]) > 5000]
    return res
print(filter_by_size(reader.read_csv_to_list("network_traffic.log")))

