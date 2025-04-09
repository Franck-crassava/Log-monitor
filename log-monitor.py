import argparse
import time
import os
import sys
import requests
from datetime import datetime

try:
    from termcolor import colored
except ImportError:
    print("[!] 'termcolor' not installed. Run 'pip install termcolor'")
    def colored(text, color): return text  # fallback

def send_webhook(webhook_url, content):
    data = {"content": content}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code not in [200, 204]:
            print(f"[!] Failed to send to webhook (HTTP {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"[!] Webhook error: {e}")

def monitor_log(filepath, keyword=None, save_path=None, show_timestamp=False, webhook_url=None):
    try:
        with open(filepath, 'r') as file:
            file.seek(0, os.SEEK_END)

            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.5)
                    continue

                if keyword and keyword.lower() not in line.lower():
                    continue

                output = line.strip()
                clean_output = output

                if show_timestamp:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    output = f"[{timestamp}] {output}"
                    clean_output = f"[{timestamp}] {clean_output}"

                if keyword:
                    output = output.replace(keyword, colored(keyword, 'red', attrs=['bold']))

                print(output)

                if save_path:
                    with open(save_path, 'a') as out_file:
                        out_file.write(clean_output + '\n')

                if webhook_url:
                    send_webhook(webhook_url, clean_output)

    except FileNotFoundError:
        print(f"[!] File not found: {filepath}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[+] Monitoring stopped.")
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description='Real-time log file monitor with filters, saving, and alerting.')
    parser.add_argument('file', help='Path to the log file')
    parser.add_argument('--filter', help='Keyword to filter and highlight')
    parser.add_argument('--save', help='Path to save filtered lines')
    parser.add_argument('--timestamp', action='store_true', help='Include timestamp in output')
    parser.add_argument('--webhook', help='Webhook URL (Discord or Slack) to send alerts')

    args = parser.parse_args()

    monitor_log(
        filepath=args.file,
        keyword=args.filter,
        save_path=args.save,
        show_timestamp=args.timestamp,
        webhook_url=args.webhook
    )

if __name__ == "__main__":
    main()
