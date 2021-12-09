import threading
import argparse
from concurrent.futures import ThreadPoolExecutor
from ipdigger.core.digger import digger, que
from colorama import Style

green = '\033[92m'
end = '\033[0m'

example_text = """
Examples:
    1. ipdigger hosts.txt -c 20
    2. ipdigger hosts.txt -ih 
    3. ipdigger hosts.txt -o ouput.txt
"""

parser = argparse.ArgumentParser(epilog=example_text,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('hosts', help='Specify hosts file.')
parser.add_argument('-o', '--output', help='Specify the output file. Default is ip.txt.', default='ip.txt')
parser.add_argument('-c', '--concurrency', help='Specify concurrent threads. Default is 10.', default=10, type=int)
parser.add_argument('-ih', '--include-host', help='Include host with IP in output file.', action='store_true')
args = parser.parse_args()
targets = args.hosts
output = args.output
concurrency = args.concurrency
include_host = args.include_host

with open(targets) as _targets:
    read = _targets.read().splitlines()

def main():
    print(f'''{green}{Style.BRIGHT} _       _ _                   
|_|___ _| |_|___ ___ ___ ___   
| | . | . | | . | . | -_|  _|  
|_|  _|___|_|_  |_  |___|_|    
  |_|       |___|___|          
                     {end}   @whoamisec
                        ''')
    try:
        with ThreadPoolExecutor(max_workers=concurrency) as e:
            for target in read:
                e.submit(digger, target, output, include_host)
    except Exception:
        print(que, 'Unexpected error!')