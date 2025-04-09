# 📘 log-monitor.py

**Real-time log monitoring with filtering, saving, alerting, and visual enhancements.**  
A handy Python tool to tail log files like `tail -f` and add filters, timestamps, webhook alerts, and more.

---

## ⚙️ Features

- 🔁 Real-time log file monitoring (`tail -f` style)
- 🔍 Keyword filtering (`--filter`)
- 💾 Save filtered lines to a file (`--save`)
- ⏱️ Optional timestamps for each matching line (`--timestamp`)
- 🌈 Colored console output for matched keywords
- 📡 Alerting via Discord/Slack webhook (`--webhook`)

---

## 🚀 Usage

```bash
python log-monitor.py /path/to/log/file [options]
```

## 🔧 Options
Argument	Description
--filter	Keyword to filter and highlight lines
--save	File path to save filtered output
--timestamp	Show timestamps on each printed line
--webhook	Discord or Slack webhook URL for alerting

📌 Examples
```bash
# Simple real-time tail
python log-monitor.py /var/log/syslog

# Filter lines with "CRITICAL" and add timestamps
python log-monitor.py /var/log/syslog --filter CRITICAL --timestamp

# Filter, timestamp, save to file, and alert via webhook
python log-monitor.py /var/log/auth.log --filter "fail" --save fails.log --timestamp --webhook https://discord.com/api/webhooks/...

# Minimalist keyword match + Discord alert
python log-monitor.py logs/app.log --filter error --webhook https://hooks.slack.com/...
```

🛠 Requirements
Python 3.x

requests for webhook sending
Install via:

```bash
pip install requests
Optional: termcolor for colored terminal output
```
Install via:

```bash
pip install termcolor
```

## 🔐 Security Note
When using webhook alerts, keep the URL secure and never expose it publicly, especially in public repositories.

## ✍️ Author
Franck CRASSAVA – Cybersecurity & Network Architecture Student
