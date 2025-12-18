from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Device:
    hostname: str
    mgmt_ip: str
    site: str
    role: str
    os_type: str
    vendor: Optional[str] = None
    os_version: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    collected_os_version: Optional[str] = None
    uptime: Optional[str] = None
    last_scanned: Optional[str] = None
    scan_status: Optional[str] = None

    def __str__(self):
        base = f"Device: {self.hostname} ({self.mgmt_ip}) - {self.site} - {self.role} - {self.os_type}"
        if self.vendor:
            base += f" - {self.vendor}"
        if self.os_version:
            base += f" - {self.os_version}"
        if self.scan_status == "success":
            scan_result = f"\nLast scan status : Success, scanned on : {self.last_scanned}\nData Collected:"
            if self.model:
                scan_result += f" - Model: {self.model}"
            if self.serial_number:
                scan_result += f" - Serial Number: {self.serial_number}"
            if self.collected_os_version:
                scan_result += f" - OS Version: {self.collected_os_version}"
            if self.uptime:
                scan_result += f" - Uptime: {self.uptime}"
            base += scan_result
        if self.scan_status == "partial":
            scan_result = f"\nLast scan status : Partial, last attempt : {self.last_scanned}"
            base += scan_result
        if self.scan_status == "failed":
            scan_result = f"\nLast scan status : Failed, last attempt : {self.last_scanned}"
            base += scan_result
        if self.scan_status is None:
            base += f"\nNever scanned device"
        return base
    
    def to_dict(self):
        return asdict(self)