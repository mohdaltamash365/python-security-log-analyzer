
def analyze_log(filename):

    failed_logins = 0

    failed_ips = {}
    
    try:
        with open(filename, "r") as file:
     
            for line in file:
                line = line.strip()

    
                if "Failed login" in line:
                    failed_logins += 1

                    ip = line.split("from ")[1]

                    failed_ips[ip] = failed_ips.get(ip, 0) + 1

                    print(f"ALERT: Failed login detected")
                    print(f"Source IP: {ip}")

    except FileNotFoundError:
        print("ERROR: Log file not found")

    return failed_logins, failed_ips

def main(threshold):

    failed_logins, failed_ips = analyze_log("security_log.txt")

    print(f"\nTotal Failed logins: {failed_logins}")
    print("\nFailed Login Attempts by IP:")

    for ip, count in failed_ips.items():
        print(f"{ip} → {count} attempts")

    print("\nSecurity Analysis: ")

    for ip, count in failed_ips.items():
        if count >= threshold:
            print(f"WARNING: {ip} has {count} failed login attempts")
        elif count == 2:
            print(f"SUSPICIOUS: {ip} has {count} failed login attempts")
        else:
            print(f"INFO: {ip} has {count} failed login attempts")
if __name__ == "__main__":
    main(3)
