import random

def ip_blocklist():
    
    blocklist = {
        "192.168.1.10",
        "192.168.1.15",
        "192.168.1.18"
    }
    return blocklist  

def check(ip, blocklist):
    if ip in blocklist:
        print(f"{ip}: block")
    else:
        print(f"{ip}: allow")

def ip_generate():
    a = random.randint(0, 20)
    ip = f"192.168.1.{a}"
    return ip  


if __name__ == "__main__":
    blocklist = ip_blocklist()
    for _ in range(10):
        ip = ip_generate()  
        check(ip, blocklist)  
    
    
