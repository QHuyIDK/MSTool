
Mini tool để nhập melody + bass và xuất file MP3.  

Bạn có thể nhập các nốt theo dạng `key:duration` (ví dụ: `c:500`) và thêm bass riêng.  

---

## Cài đặt

### 1. Clone repo về:  

```bash
git clone https://github.com/QHuyIDK/MSTool/
cd mstool
```
### 2. Cài dependencies:


```bash
pip install -r requirements.txt

requirements.txt có thể gồm:

numpy
pydub
```
### 3. (Optional) Nếu muốn cài global để chạy mstool từ mọi nơi:


```bash
chmod +x mstool.py
sudo ln -s $(pwd)/mstool.py /usr/local/bin/mstool
```
Sau đó chỉ cần gõ mstool là chạy được.


---

## Cách dùng

### Chạy tool:
```bash
./mstool.py
```
Hoặc nếu đã cài global:
```bash
mstool
```
### 1. Chọn file MP3 để sửa hoặc nhấn ENTER để tạo file mới.


## 2. Nhập tên file mới (không cần .mp3).


### 3. Nhập Melody theo dạng: key:duration (vd: c:500)

Nhấn # để kết thúc Melody.

Nhấn u để undo nốt cuối.



### 4. Sau khi xong Melody, tool sẽ hỏi nhập Bass theo cùng định dạng.


### 5. Tool sẽ tự play từng nốt và cuối cùng xuất file MP3.




---

## Ví dụ

Nhập Melody
`Nốt 1: c:500`
`Nốt 2: d:500`
`Nốt 3: e:500`
`Nốt 4: #`
`File MP3 đã lưu: output.mp3`


---

## Tool dùng pydub để tạo và phát âm thanh.

