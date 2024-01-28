import os

DHCPD_CONF = 'etc/dhcpcd.conf'
DNSMASQ_CONF = 'etc/dnsmasq.conf'
HOSTAPD_CONF = 'etc/hostapd.conf'


def get_wifi_info():
    data = {}
    with open(HOSTAPD_CONF, 'r') as f:
        for line in f:
            if line.startswith('ssid='):
                data['ssid'] = line.split('=')[1].strip()
            elif line.startswith('wpa_passphrase='):
                data['wpa_passphrase'] = line.split('=')[1].strip()
            elif line.startswith('country_code='):
                data['country_code'] = line.split('=')[1].strip()
    return data 

def set_wifi_info(key, value):
    with open(HOSTAPD_CONF, 'r') as f:
        lines = f.readlines()
    with open(HOSTAPD_CONF, 'w') as f:
        for line in lines:
            if line.startswith(key):
                line = key + '=' + value + '\n'
            f.write(line)

def get_dhcpcd_info():
    data = {}
    with open(DHCPD_CONF, 'r') as f:
        for line in f:
            if line.startswith('static ip_address='):
                data['ip_address'] = line.split('=')[1].strip()
            elif line.startswith('static domain_name_servers='):
                data['dns_servers'] = line.split('=')[1].strip()
    return data

def set_dhcpcd_info(key, value):
    with open(DHCPD_CONF, 'r') as f:
        lines = f.readlines()
    with open(DHCPD_CONF, 'w') as f:
        for line in lines:
            if line.startswith(key):
                line = key + '=' + value + '\n'
            f.write(line)

# def get_dnsmasq_info():
#     data = {}
#     with open(DNSMASQ_CONF, 'r') as f:
#         for line in f:
#             if line.startswith('interface='):
#                 data['interface'] = line.split('=')[1].strip()
#             elif line.startswith('dhcp-range='):
#                 data['dhcp_range'] = line.split('=')[1].strip()
#             elif line.startswith('dhcp-option='):
#                 data['dhcp_option'] = line.split('=')[1].strip()
#     return data

def set_dnsmasq_info(key, value):
    with open(DNSMASQ_CONF, 'r') as f:
        lines = f.readlines()
    with open(DNSMASQ_CONF, 'w') as f:
        for line in lines:
            if line.startswith(key):
                line = key + '=' + value + '\n'
            f.write(line)

def restart_network_services():
    os.system('systemctl restart dhcpcd && systemctl restart dnsmasq && systemctl restart hostapd')