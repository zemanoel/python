"""
Biblioteca os = Módulo que fornece uma maneira simples de usar funcionalidades que são dependentes de sistema
operacional
"""
import os  # importa o modulo ou biblioteca os = integra os programas de recursos do sistema operacional
import time

# print('#'*60)
# ip_ou_host = input('Digite o IP ou HOST a ser verificado: ')
# print('-'*60)
# os.system(f'ping -n 6 {ip_ou_host}')  # chamando system da biblioteca os - comando ping -n (-n numero de pacotes 6)
# print('-'*60)
with open('hosts.txt') as file:
    dump = file.read()
    dump_convertido = dump.splitlines()
    for ip in dump_convertido:
        os.system('ping ' + ip)
        time.sleep(5)
        os.system('pause')
