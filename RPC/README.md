# RPC (Remote Procedure Call)
Protokol yang dapat memungkinkan client untuk memanggil suatu fungsi dari server, seolah-olah fungsi itu ada di lokal (client). Client mengirimkan request ke server menggunakan format pesan yaitu JSON. Payload JSON yang digunakan sudah ter-define pada file rpcclient.py
```
payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1,
    }
    response = requests.post(url, data=json.dumps(payload)headers=headers).json()
    return response
```
Dimana method yang digunakan ada POST (tertera pada fungsi requests.post) dan params juga ter-define, yaitu add: [10, 2] dan multiply: [10, 5].
```
result_add = call_rpc("add", [10, 2])
result_multiply = call_rpc("multiply", [10, 5])
```
Client mengirimkan pesan request ke server, maka server akan menerima HTTP POST tersebut dan datanya akan diproses menggunakan JSONRPCResponseManager,disini akan dilihat apa isi dari HTTP POST yang dikirimkan dari client. Server akan menulis response yang akan dikirimkan ke client melalui potongan kode berikut ; 
```
response = JSONRPCResponseManager.handle(post_data, dispatcher)
```
Dispatcher akan mencari fungsi yang sesuai dengan fungsi yang sudah di-define di server dengan fungsi  yang direquest oleh client. Jika terdapat fungsi tersebut maka fungsi add() dan multiply() pada server akan di-execute
```
def add(a, b):
    return a / b

def multiply(a, b):
    return a * b
```
hasil execute fungsi tersebut akan diubah menjadi format JSON lalu dikirimkan ke client
```
self.wfile.write(response.json.encode())
```
<img src="https://i.imgur.com/mlT2HqV.jpeg">
