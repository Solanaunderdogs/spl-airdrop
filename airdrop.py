import subprocess
with open('airdrop.txt', 'r+') as f: #r+ does the work of rw
    lines = f.readlines()
    for i, line in enumerate(lines):
        list_files = subprocess.Popen(["spl-token", "transfer", "--fund-recipient", "--allow-unfunded-recipient", "4w3Zi7aWaLMGafG6cApeMjJYuuA1VDTP4w4QbfTVgn1v", "130",lines[i].strip()], )
        list_files.wait()
    f.seek(0)
    for line in lines:

        f.write(line)
        print(line)
