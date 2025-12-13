from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

class NetDevice:
    def __init__(self, host, username, password, device_type):
        self.host = host
        self.username = username
        self.password = password
        self.device_type = device_type
        self.session = None
        self.status = None
        self.error = None
    
    def connect(self):
        if self.session is None:
            try:
                self.session = ConnectHandler(
                    device_type=self.device_type,
                    host=self.host,
                    username=self.username,
                    password=self.password
                )
                self.status = "success"
                print("Connection successful.")
                return True
            except NetmikoTimeoutException as e:
                self.status = "failed"
                self.error = str(e)
                print(f"Connection to device {self.host} timed out: {e}")
                return False
            except NetmikoAuthenticationException as e:
                self.status = "failed"
                self.error = str(e)
                print(f"Authentication issue to device {self.host} failed: {e}")
                return False
            except Exception as e:
                self.status = "failed"
                self.error = str(e)
                print(f"Connection to device {self.host} failed: {e}")
                return False
        else:
            print("Already connected.")
            return True
    
    def send_command(self, command):
        if self.session:
            output = self.session.send_command(command)
            return output
        else:
            return("Not connected to the device")
    
    def disconnect(self):
        """Closes the connection."""
        if self.session:
            self.session.disconnect()
            self.session = None
            print(f"Disconnected from {self.host}")
        else:
            print("Not connected, nothing to disconnect.")
