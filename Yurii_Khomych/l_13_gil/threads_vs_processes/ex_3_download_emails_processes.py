import concurrent
import imaplib
import time
from concurrent.futures import ProcessPoolExecutor

IMAP_SERVER = "imap.gmail.com"
USERNAME = "email@gmail.com"
PASSWORD = "password"


def download_emails(ids):
    client = imaplib.IMAP4_SSL(IMAP_SERVER)
    client.login(USERNAME, PASSWORD)
    client.select()
    for i in ids:
        print(f"Downloading mail id: {i.decode()}")
        _, data = client.fetch(i, "(RFC822)")
        with open(f"emails/{i.decode()}.eml", "wb") as f:
            f.write(data[0][1])
    client.close()
    print(f"Downloaded {len(ids)} mails!")


start = time.time()

client = imaplib.IMAP4_SSL(IMAP_SERVER)
client.login(USERNAME, PASSWORD)
client.select()
_, ids = client.search(None, "ALL")
ids = ids[0].split()
ids = ids[:200]
client.close()

number_of_chunks = 10
chunk_size = 10
executor = ProcessPoolExecutor(max_workers=number_of_chunks)
futures = []
for i in range(number_of_chunks):
    chunk = ids[i * chunk_size : (i + 1) * chunk_size]
    futures.append(executor.submit(download_emails, chunk))

for future in concurrent.futures.as_completed(futures):
    pass
print("Time:", time.time() - start)
