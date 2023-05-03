def is_valid(arg: str):
    """Проверка на правильность ip адреса"""
    arg = arg.replace(' ', '')
    int_ipaddress = []
    if '/' in arg and arg.count('/') == 1:
        ipaddress, prefix = arg.split('/')
        if prefix.isdigit() and 0 <= int(prefix) <= 32:
            if len(ipaddress.split('.')) == 4:
                for i in ipaddress.split('.'):
                    if i.isdigit() and 0 <= int(i) <= 255:
                        int_ipaddress.append(int(i))
                    else:
                        return False
                else:
                    if len(int_ipaddress) == 4:
                        int_ipaddress.append(int(prefix))
                        return int_ipaddress


def calculate_ip(ip):
    """Деление на подсети в бинарном виде"""
    mask_bin, wildcard_bin = '', ''
    ip_bin = list(map(lambda x: bin(x)[2:].zfill(8), ip[:4]))
    ip_bin = ''.join(ip_bin)
    network_bin = network_bc = network_min = network_max = ip_bin[:ip[-1]]
    for _ in range(32 - ip[-1]):
        network_bin += '0'
        network_bc += '1'
        network_min += '0'
        network_max += '1'
    else:
        network_min += '1'
        network_max += '0'

    for _ in range(ip[-1]):
        mask_bin += '1'
        wildcard_bin += '0'

    while len(mask_bin) < 32:
        mask_bin += '0'
        wildcard_bin += '1'

    network = [str(int(network_bin[:8], 2)), str(int(network_bin[8:16], 2)),
               str(int(network_bin[16:24], 2)), str(int(network_bin[24:32], 2))]

    first_host = [str(int(network_min[:8], 2)), str(int(network_min[8:16], 2)),
                  str(int(network_min[16:24], 2)), str(int(network_min[24:32], 2))]

    last_host = [str(int(network_max[:8], 2)), str(int(network_max[8:16], 2)),
                 str(int(network_max[16:24], 2)), str(int(network_max[24:32], 2))]

    broadcast = [str(int(network_bc[:8], 2)), str(int(network_bc[8:16], 2)),
                 str(int(network_bc[16:24], 2)), str(int(network_bc[24:32], 2))]

    mask = [str(int(mask_bin[:8], 2)), str(int(mask_bin[8:16], 2)),
            str(int(mask_bin[16:24], 2)), str(int(mask_bin[24:32], 2))]

    wirecard = [str(int(wildcard_bin[:8], 2)), str(int(wildcard_bin[8:16], 2)),
                str(int(wildcard_bin[16:24], 2)), str(int(wildcard_bin[24:32], 2))]

    host = 2 ** (32 - ip[-1]) - 2
    ip_dict = {
        'Network': '.'.join(network),
        'FirstHost': '.'.join(first_host),
        'LastHost': '.'.join(last_host),
        'BroadCast': '.'.join(broadcast),
        'Mask': '.'.join(mask),
        'WireCard': '.'.join(wirecard),
        'Hosts': host if host > 0 else 'N/A'
    }

    if ip[-1] == 31:
        ip_dict['FirstHost'] = '.'.join(network)
        ip_dict['LastHost'] = '.'.join(first_host)
        ip_dict['BroadCast'] = 'N/A'

    return ip_dict


def subnet_ip(data):
    if res := is_valid(data):
        return calculate_ip(res)
