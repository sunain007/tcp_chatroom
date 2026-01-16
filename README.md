# TCP Chatroom (Python Socket Programming)

A multi-client TCP chatroom application written in **Python**, supporting **real-time messaging**, **admin controls**, and **basic moderation features** such as **kick** and **ban**. The project uses **socket programming** and **multithreading** to handle multiple clients concurrently.

---

## 📌 Features

* Multi-client chat using TCP sockets
* Nickname-based user identification
* Admin authentication (password protected)
* Admin-only commands:

  * `/kick <username>`
  * `/ban <username>`
* Persistent bans using `bans.txt`
* Graceful client disconnect handling
* Thread-safe client communication
* Prevents kicked/banned users from sending messages

---

## 🛠 Technologies Used

* Python 3
* `socket` module
* `threading` module
* TCP/IP networking

---

## 📂 Project Structure

```
.
├── server.py        # Chat server
├── client.py        # Chat client
├── bans.txt         # Stores banned usernames
└── README.md        # Project documentation
```

---

## ⚙️ How It Works

### Server

* Listens for incoming TCP connections
* Requests nickname from each client
* Verifies admin credentials if nickname is `admin`
* Maintains:

  * Connected clients list
  * Nicknames list
* Broadcasts messages to all connected clients
* Handles admin moderation commands

### Client

* Connects to the server
* Sends nickname (and password if admin)
* Runs two threads:

  * **Receive thread** → listens for server messages
  * **Write thread** → sends user input
* Stops all activity when kicked, banned, or disconnected

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone <repository-url>
cd tcp_chatroom
```

### 2️⃣ Start the server

```bash
python3 server.py
```

Server output:

```
Server is running...
```

### 3️⃣ Start a client

```bash
python3 client.py
```

---

## 👤 Admin Usage

### Login as Admin

```
Nickname: admin
Password: adminpass
```

### Admin Commands

| Command          | Description                             |
| ---------------- | --------------------------------------- |
| `/kick username` | Disconnects a user                      |
| `/ban username`  | Disconnects and permanently bans a user |

> ⚠️ Only the admin can execute these commands

---

## 🔐 Security Notes

* Admin privileges are **validated server-side**
* Clients cannot spoof admin commands
* Banned users are blocked before joining
* Thread termination prevents message sending after disconnect

---

## 🧪 Known Limitations

* Messages are plaintext (no encryption)
* No TLS/SSL support
* No message history persistence
* Single admin account (hardcoded password)

---

## 🔧 Future Improvements

* TLS encryption using `ssl`
* Multiple admin roles
* Message logging
* Rate limiting / flood protection
* Async server using `asyncio`
* GUI client

---

## 📚 Learning Outcomes

This project demonstrates:

* TCP socket programming
* Multithreading and synchronization
* Client-server architecture
* Secure command handling
* Proper socket lifecycle management

---

## 📜 License

This project is for **educational purposes**. Feel free to modify and extend it.

---

## ✨ Author

**Sunain Aijaz**
Cybersecurity & Penetration Testing Enthusiast
