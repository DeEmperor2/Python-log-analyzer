failed_count = 0
failed_users = {}

with open("sample_logs.txt", "r") as file:
    logs = file.readlines()

print("\nAnalyzing logs...\n")

for log in logs:
    print(log.strip())

    if "FAILED" in log:
        failed_count += 1

        parts = log.split()
        username = parts[2]

        if username in failed_users:
            failed_users[username] += 1
        else:
            failed_users[username] = 1

print(f"\nTotal Failed Login Attempts: {failed_count}")

print("\nUsers with failed attempts:")

for user, count in failed_users.items():
    print(f"{user}: {count} failed attempts")

if failed_count >= 3:
    print("\n⚠️ ALERT: Multiple failed login attempts detected!")