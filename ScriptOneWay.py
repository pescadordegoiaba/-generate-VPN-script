import random

def gerar_ip_vpn():
    ip = ""
    for _ in range(4):
        octeto = random.randint(0, 255)
        ip += str(octeto) + "."
    return ip[:-1]

def testar_ip(ip):
    if ip.startswith("10.") or ip.startswith("172.") or ip.startswith("192.168."):
        return "VPN"
    else:
        return "IP Público"

# Exemplo de uso
ip_aleatorio = gerar_ip_vpn()
resultado = testar_ip(ip_aleatorio)
print(f"IP: {ip_aleatorio}")
print(f"Tipo: {resultado}")
