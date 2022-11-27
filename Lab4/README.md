# Shift-Reduce-Parsers
Phân tích cú pháp ngôn ngữ Python

### Thư viện sử dụng:
* numpy
* schemdraw
* matplotlib
* PyQt5
### Cách cài đặt:
<pre> pip install -r requirements.txt </pre>
    
    
### Cách sử dụng:
<pre> python main.py </pre>

### Thông tin về cách mô tả mạch điện
- Ký hiệu:
    + '+' : mắc nối tiếp
    + '*' : mắc song song
    + '()': đống gói mạch

- Để khai báo giá trị của R1 và R2:
    + R1=5,R2=6
    
- Để khai báo mạch điện của R1 nối tiếp R2 và mắc song song với R3:
    + (R1+R1)*R3