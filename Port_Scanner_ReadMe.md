# 🔍 Python Port Scanner

This is a multithreaded Python-based port scanner that scans all 65,535 TCP ports on a specified target host. It's built using the `socket` and `threading` modules and is intended for educational and ethical hacking purposes.

---

## 🚀 Features

- Scans all TCP ports on a target (1-65535)
- Uses multithreading for fast scanning
- Handles exceptions and user interruptions gracefully
- Displays real-time open ports in terminal
- Written in beginner-friendly Python with comments

---

## 📦 Requirements

- Python 3.x
- Works on Windows, macOS, or Linux (no external libraries required)

---

## 🛠 Usage

```bash
python scanner.py <target>
```
---

## 📘 How It Works

- Accepts a target hostname or IP as a command-line argument.
- Resolves the hostname to an IP.
- Starts a thread for each port (1 to 65535).
- Each thread attempts a TCP connection.
- If successful, it prints the open port number.

---

## 🧠 Learning Goals

This project helped me practice:

- Network programming with Python sockets
- Threading and concurrent execution
- Exception handling and graceful exits
- Building tools for ethical hacking and cybersecurity

---

## 📌 Next Steps / To-Do

- Add user-defined port ranges
- Export results to a file (TXT or JSON)
- Add service detection (e.g., HTTP, FTP)
- Use ThreadPoolExecutor for safer threading
- Add UDP scanning support

---

## 👩‍💻 Author

Lindsey Armstrong\
Aspiring ethical hacker and cybersecurity analyst

🔗 [LinkedIn](https://www.linkedin.com/in/whoislindseyarmstrong/)\
🌐 [My Portfolio Website](http://whoislindseyarmstrong.tech/)

---

## 📜 License
MIT License. Use responsibly.
