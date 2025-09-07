import subprocess
import requests
import os 



windows_path =  'C:\Windows\System32\drivers\etc\hosts'
os_flags = os.O_RDONLY

opener = os.open(windows_path, os_flags)