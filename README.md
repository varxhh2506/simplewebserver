# EX01 Developing a Simple Webserver
## Date:26/09/2026

## AIM:
To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
web.py
from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
    <head>
        <title>simplewebserver</title>
    </head>
    <body align="center">
        <h1>Table Configuration</h1>
        <h2>varshika</h2>
        <h2>26019047</h2>
        <table align="center" border="2">
            <tr>
                <th>Device Name</th>
                <td>TL15-53M-G2</td>
            </tr>
            <tr>
                <th>Processor</th>
                <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
            </tr>
            <tr>
                <th>Installed RAM</th>
                <td>16.0 GB (15.7 GB usable)</td>
            </tr>
            <tr>
                <th>Graphics cards</th>
                <td>Intel(R) Graphics (128 MB)</td>
            </tr>
            <tr>
                <th>Storage</th>
                <td>116 GB of 477 GB used</td>
            </tr>
            <tr>
                <th>Device ID</th>
                <td>978E3432-BEBB-44C2-8145-050980B48717</td>
            </tr>
            <tr>
                <th>Product ID</th>
                <td>00342-42954-11668-AAOEM</td>
            </tr>
            <tr>
                <th>System type</th>
                <td>64-bit operating system, x64-based processor</td>
            </tr>
            <tr>
                <th>Pen and touch</th>
                <td>No pen or touch input is available for this display</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()

```

## OUTPUT:
webpage
![alt text](<Screenshot (28).png>)
serverpage
![alt text](<Screenshot (30).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
