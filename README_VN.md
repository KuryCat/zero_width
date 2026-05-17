# zero_width 1.0

Một công cụ Python giúp bạn ẩn và hiện các thông điệp bí mật bên trong văn bản bằng kỹ thuật ký tự có độ rộng bằng 0 (Zero-Width Characters). Văn bản chứa phần ẩn nhìn bề ngoài hoàn toàn bình thường, nhưng hệ thống và công cụ vẫn có thể đọc được nội dung gốc.

## Tính năng chính

1. Hiện từ bị ẩn trong một chuỗi văn bản.
2. Ghép từ cần giấu vào một văn bản thường ở dạng vô hình.

## Cài đặt

Công cụ chạy trực tiếp bằng Python 3 mà không cần cài đặt thêm thư viện bên thứ ba:

```bash
python main.py
```

## Cách dùng

### 1. Ghép từ bị ẩn vào văn bản (Merge)

Dùng lệnh `merge` để nhúng một từ vào vị trí mong muốn trong văn bản gốc. Từ được nhúng sẽ biến thành ký tự zero-width vô hình.

Cú pháp đầy đủ:
```bash
python main.py merge "bạn [___] tôi" "và"
```

Cú pháp viết tắt (Shorthand):
```bash
python main.py "bạn [___] tôi" "và"
```

Kết quả hiển thị trên màn hình:
```text
bạn tôi
```
*Lưu ý: Từ "và" đã được nhúng vào vị trí dấu ngoặc vuông ở dạng vô hình, không chiếm diện tích hiển thị.*

Nếu văn bản gốc không chứa ký hiệu vị trí `[___]`, công cụ sẽ tự động nhúng từ ẩn vào cuối văn bản:
```bash
python main.py merge "bạn" "tôi"
```
Kết quả hiển thị trên màn hình vẫn chỉ là:
```text
bạn
```

### 2. Hiện từ bị ẩn trong văn bản (Reveal)

Dùng lệnh `reveal` và truyền vào chuỗi văn bản chứa ký tự ẩn (kết quả thu được từ lệnh merge trước đó) để trích xuất lại thông điệp bí mật.

Cú pháp đầy đủ:
```bash
python main.py reveal "bạn tôi"
```

Cú pháp viết tắt (Shorthand):
```bash
python main.py "bạn tôi"
```

Kết quả hiển thị trên màn hình:
```text
và
```

Công cụ hỗ trợ nhận diện các định dạng đánh dấu vị trí ẩn khi ghép từ bao gồm:
* `[___]` hoặc `[ẩn]`
* `<hidden>ẩn</hidden>`
* `{ẩn}`

### 3. Sử dụng tệp điều khiển zw.cmd trên Windows

Nếu bạn sử dụng Windows Command Prompt (CMD), bạn có thể dùng tệp `zw.cmd` đi kèm để gõ lệnh ngắn hơn. Chạy lệnh trực tiếp từ thư mục của dự án:

```cmd
zw "bạn [___] tôi" "và"
zw "bạn tôi"
zw merge "bạn [___] tôi" "thân"
zw reveal "bạn tôi"
```

Để sử dụng công cụ ở mọi thư mục trên máy tính, hãy sao chép tệp `zw.cmd` cùng với tệp `main.py` vào một thư mục cố định và thêm đường dẫn của thư mục đó vào biến môi trường PATH của Windows.

## Lưu ý an toàn và kiểm tra mã nguồn

### Cảnh báo virus giả (False Positive)
Kỹ thuật chèn ký tự Unicode ẩn (Zero-Width) đôi khi có thể bị một số trình quét bảo mật như Windows Defender nghi ngờ nhầm là mã độc ẩn. Bạn có thể hoàn toàn yên tâm sử dụng dựa trên các yếu tố sau:

* Toàn bộ mã nguồn được viết bằng Python dưới dạng văn bản thuần (`.py`), cho phép bạn mở ra kiểm tra trực tiếp từng dòng logic.
* Dự án không chứa bất kỳ tệp nhị phân biên dịch sẵn nào (`.exe`, `.dll`) hoặc mã nguồn bị làm mờ (obfuscation).
* Bạn có thể tự khởi chạy và kiểm soát hoàn toàn hoạt động của công cụ thông qua trình biên dịch Python chính thức.

### Hướng dẫn chạy từ mã nguồn
1. Tải toàn bộ thư mục dự án về máy tính.
2. Đảm bảo máy tính đã cài đặt Python phiên bản 3.6 trở lên.
3. Mở cửa sổ dòng lệnh tại thư mục dự án và thực hiện các lệnh theo cú pháp phía trên.

## Giấy phép

Dự án này được cấp phép tuân thủ theo các điều khoản của MIT License - xem chi tiết tại tệp `LICENSE_VN`.
