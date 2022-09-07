def defang_ip(ip):
    return ip.replace(".", "[.]")


print(defang_ip("192.168.0.1"))


def defang_ip2(ip):
    ip_list = ip.split(".")
    return "[.]".join(ip_list)


print(defang_ip("192.168.0.1"))
