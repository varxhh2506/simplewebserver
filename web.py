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