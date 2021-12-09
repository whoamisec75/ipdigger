import re
import socket
import sys
from colorama import Fore, Style

res  = ('[' + '\033[1;92m✓\033[0m' + ']')
que  = ('[' + '\033[1;91m-\033[0m' + ']')

def digger(target, output, include_host):
    try:
        if re.search('https://', target):
            target2 = target.replace('https://', '')
        elif re.search('http://', target):
            target2 = target.replace('http://', '')
        else:
            target2 = target

        IP = socket.gethostbyname(target2)
        print(res,Style.DIM + target + Style.RESET_ALL, '{}{}--->{}'.format(Fore.CYAN, Style.BRIGHT, Style.RESET_ALL), IP)
        if include_host:
            with open(output, 'a') as _output:
                print(f'{target}:{IP}', file=_output)
        else:
            with open(output, 'a') as _output:
                print(f'{IP}', file=_output)
    except Exception:
        print(que, f'{Fore.RED}{Style.BRIGHT}Unexpected error!{Style.RESET_ALL}')
    

