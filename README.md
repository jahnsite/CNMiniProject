# CN Mini Project

### Tech Used

- Language Used : Python
- Tkinter for GUI (to display device type)
- Pyshark to scrape out the information like Mac Address and User agent

### Resources used

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent

- https://api.macvendors.com/

- https://pypi.org/project/user-agents/

### File Structure

#### Program1

`device.py`

- Able to fetch User Agent and show device type using pcap file using http protocol

Contains mobile http related data
`/files/mobile.pcap`

Contains PC http related data
`/files/pc.pcapng`

<hr/>

#### Program2

`vendor.py`

- Able to fetch source and destination MAC address from pcap file using arp protocol and displaying Vendor Name.

Contains packets which are from devices in the same network
`/files/vendor.pcapng`
