import argparse
import time
import os
import sys
from datetime import datetime

try:
    from termcolor import colored
except ImportError:
    print("[!] 'termcolor' module is not installed. Run 'pip install termcolor' to enable color highlighting.")
    def colored(text, color): return text  # fallback

def monitor_log(filepath, keyword=None, save_path=None, show_timestamp=False):
    try:
        with open(filepath, 'r') as file:
            file.seek(0, os.SEEK_END)  # Go to end of file

            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.5)
                    continue

                if keyword and keyword.lower() not in line.lower():
                    continue

                output = line.strip()
                if show_timestamp:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    output = f"[{timestamp}] {output}"

                # Highlight keyword in color
                if keyword:
                    output = output.replace(keyword, colored(keyword, 'red', attrs=['bold']))

                print(output)

                if save_path:
                    with open(save_path, 'a') as out_file:
                        out_file.write(output + '\n')

    except FileNotFoundError:
        print(f"[!] File not found: {filepath}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[+] Monitoring stopped.")
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description='Real-time log file monitor with keyword filtering and output options.')
    parser.add_argument('file', help='Path to the log file to monitor')
    parser.add_argument('--filter', help='Keyword to filter and highlight')
    parser.add_argument('--save', help='File path to save matched lines')
    parser.add_argument('--timestamp', action='store_true', help='Include timestamp in output')

    args = parser.parse_args()

    monitor_log(args.file, args.filter, args.save, args.timestamp)

if __name__ == "__main__":
    main()
