import socket

def connect_to_phone(ip_address, port):
  """Connects to the phone at the specified IP address and port.

  Args:
    ip_address: The IP address of the phone.
    port: The port of the phone.

  Returns:
    The socket object that is connected to the phone.
  """

  socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket_object.connect((ip_address, port))
  return socket_object

def main():
  """Connects to the phone and prints the output."""

  ip_address = "192.168.1.100"
  port = 80
  socket_object = connect_to_phone(ip_address, port)
  data = socket_object.recv(1024)
  print(data)

if __name__ == "__main__":
  main()
