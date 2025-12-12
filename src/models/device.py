from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Device:
    hostname: str
    mgmt_ip: str
    site: str
    role: str
    vendor: Optional[str] = None
    os_type: Optional[str] = None
    os_version: Optional[str] = None

    def __str__(self):
        base = f"Device: {self.hostname} ({self.mgmt_ip}) - {self.site} - {self.role}"
        if self.vendor:
            base += f" - {self.vendor}"
        if self.os_type:
            base += f" - {self.os_type}"
        if self.os_version:
            base += f" - {self.os_version}"
        return base
    
    def to_dict(self):
        return asdict(self)