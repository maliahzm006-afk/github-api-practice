import requests
from tqdm import tqdm

url = 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-723.exe'

r = requests.get(url,stream=True)


print(f'Status: {r.status_code}')

print(f'Content-Type: {r.headers['content-type']}')

print(f'Content-Length: {r.headers['content-length']}')


totalFileSize = int(r.headers['content-length'])

print(f'total File Size: {totalFileSize}')

totalBytesReceived = 0
fileStatusCode = r.status_code

if fileStatusCode == 200:
    print('DONWNLOADING...')

    with tqdm(total=totalFileSize,unit_scale=True) as progress_bar:
        with open('winrar.exe','wb') as file:
            for chunks in r.iter_content(chunk_size=4096):
                file.write(chunks)
                progress_bar.update(len(chunks))
    
else:
    print('❌ COULD NOT BE DOWNLOADED, RIGHT NOW')


print(f'total chunks: {totalBytesReceived/4096}')