import argparse
import time
import os
import sys

def monitor_log(filepath, keyword=None, save_path=None, show_timestamp=False):
    try:
        with open(filepath, 'r') as file:
            # Aller à la fin du fichier
            file.seek(0, os.SEEK_END)

            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.5)
                    continue

                if keyword and keyword.lower() not in line.lower():
                    continue

                output = line.strip()
                if show_timestamp:
                    output = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {output}"

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
    parser = argparse.ArgumentParser(description='Real-time log file monitor with optional filtering and saving.')
    parser.add_argument('file', help='Path to the log file to monitor')
    parser.add_argument('--filter', help='Keyword to filter lines')
    parser.add_argument('--save', help='Path to save matched lines')
    parser.add_argument('--timestamp', action='store_true', help='Include timestamps in output')

    args = parser.parse_args()

    monitor_log(args.file, args.filter, args.save, args.timestamp)

if __name__ == "__main__":
    main()

