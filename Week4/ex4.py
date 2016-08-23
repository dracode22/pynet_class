


#!/usr/bin/env python



import pexpect
import time

def login(ssh_conn):
    
    password = '88newclass'
    
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')
    
    
def find_prompt(ssh_conn):
    
    ssh_conn.send('\n')
    time.sleep(1)
    ssh_conn.expect('#')
    prompt = ssh_conn.before + ssh_conn.after
    
    return prompt.strip()

    

def main():
    

    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'
    port = 22
    
    
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr,port))
    ssh_conn.timeout = 3
    
    
    login(ssh_conn)
    prompt = find_prompt(ssh_conn)
    
    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect(prompt)
    
    ssh_conn.sendline('conf t')
    ssh_conn.expect('#')
    
    ssh_conn.sendline('logging buffered 20100 ')
    ssh_conn.expect('#')
    
    ssh_conn.sendline('end')
    ssh_conn.expect(prompt)
    
    ssh_conn.sendline('show running | i buffer')
    ssh_conn.expect(prompt)
    
    
    print '\n>>>>'
    print ssh_conn.before
    print '>>>>\n'
    
if __name__ == '__main__':
    main()
    
    
