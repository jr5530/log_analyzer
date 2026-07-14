import reader

def check_outsiders_ip(data):
    res = [log[1] for log in data if log[1][:3] != "10." and log[1][:7] != "192.168"]
    return res

print(check_outsiders_ip(reader.read_csv_to_list("network_traffic.log")))

