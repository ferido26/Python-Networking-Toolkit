# Python Socket Programming – Multi-Client Server

##  Overview
This project demonstrates a **multi-client TCP server-client architecture** built using Python. 

### Why This Project?
- As a Cybersecuity Trainee, I wanted to understand about how the real-world network communication works by implementing a **custom message protocol**, handling **multiple clients simultaneously**, and ensuring **reliable data transfer**.

---

##  Features
- Multi-client handling using **threading**
- Reliable communication using **TCP sockets**
- Custom **message framing protocol (header + data)**
- Graceful client disconnection
- Server response handling
- Active connection tracking

---

## 🏗️ Project Structure
- ├── server.py # Handles multiple client connections
- ├── client.py # Sends messages to server


---

## Concepts Learned

### 1. Socket Programming
- Used `socket.AF_INET` and `socket.SOCK_STREAM` for TCP communication.
- Learned how client-server architecture works.
```Creating a socket
class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
```

---

### 2. Server-Client Communication Flow
- Server listens for incoming connections.
- Client connects using IP and port.
- Data is exchanged between both.

---

### 3. Multi-threading
- Each client runs on a separate thread.
- Allows multiple clients to communicate simultaneously.

```python
threading.Thread(target=handle_client, args=(conn, addr))
```
---

### 4. Custom Message Protocol

Implemented a fixed-length header system because TCP does not preserve message boundaries, so this ensures that **complete message is delivered**, **No data corrupts**, and **get a structured communication**. 

- First send message length
- Then send actual message
```
 HEADER = 64
```

---

### 5. Encoding & Decoding
Used UTF-8 encoding for sending/receiving messages.
```
msg.encode("utf-8")
msg.decode("utf-8")
```

---

### 7. Graceful Disconnection
Implemented a custom disconnect message
```
DISCONNECT_MESSAGE = "DISCONNECT"
```
Allows clean closing of connections

---

### 8. Active Connection Tracking
Tracks number of connected clients
```
threading.active_count() - 1
```

### 9. Server Response Handling
Server sends acknowledgment after receiving a message
```
conn.send("Msg received".encode(FORMAT))
```


10. Active Connection Tracking
Tracks number of connected clients
```
threading.active_count() - 1
```

---

## How It Works
- Server
- Starts and listens for connections
- Accepts incoming clients
- Creates a new thread for each client
- Receives message length
- Receives actual message
- Sends response
- Closes connection on disconnect

## Client
- Connects to server
- Sends message length (fixed header)
- Sends actual message
- Waits for server response

--- 

## Limitations
- No error handling for unexpected disconnections
- No encryption (data sent in plain text)
- Hardcoded IP address in client
- No authentication mechanism

---

### Future Improvements

- Add exception handling
- Implement encryption (SSL/TLS)
- **Convert into a controlled remote command execution lab (for cybersecurity learning)**

---

### Reference
https://docs.python.org/3/library/socket.html#creating-sockets
