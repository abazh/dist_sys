# SOAP (Simple Object Access Protocol) 
Protokol berbasis XML yang digunakan untuk komunikasi antara client dan server di suatu jaringan. Pada Paengujian ini terdapat library yang masing-masing digunakan oleh client dan server, yaitu Zeep dan Spyne.
Zeep merupakan library yang digunakan client untuk menggunakan SOAP web services yang disediakan oleh server. Zeep ini akan membaca wsdl (Web Services Description Language) dari server dan otomatis membentuk SOAP request dalam bentuk XML, lalu mengirimkannya melalui protokol HTTP. Ini ditunjukkan pada potongan kode berikut ;
```
wsdl = 'http://soap-server:8000/?wsdl'
client = Client(wsdl=wsdl)
result = client.service.add(10, 5)
```
Pada sisi server, digunakan library/framework Spyne untuk membangun SOAP web services. Spyne akan membuat endpoint HTTP serta meng-handle request SOAP yang dikirimkan oleh client. Disini sudah ter-define fungsi method yang disediakan oleh server untuk dipanggil oleh client
```
class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b
```
<img src="https://i.imgur.com/rQBwRlN.jpeg">