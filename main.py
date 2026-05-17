import argparse
import base64
import re

ZW_START = "\u2060"
ZW_END = "\u2061"
BIT_ZERO = "\u200c"
BIT_ONE = "\u200d"

HIDDEN_PATTERNS = [r"\[(.*?)\]", r"<hidden>(.*?)</hidden>", r"\{(.*?)\}"]


def encode_hidden(text):
    raw = text.encode("utf-8")
    b64 = base64.b64encode(raw).decode("ascii")
    bits = []
    for ch in b64:
        bits.append("".join(BIT_ONE if bit == "1" else BIT_ZERO for bit in format(ord(ch), "08b")))
    return ZW_START + "".join(bits) + ZW_END


def decode_hidden(encoded):
    bits = []
    for ch in encoded:
        if ch == BIT_ZERO:
            bits.append("0")
        elif ch == BIT_ONE:
            bits.append("1")
    if not bits:
        return None
    bytes_data = []
    for i in range(0, len(bits), 8):
        chunk = bits[i : i + 8]
        if len(chunk) < 8:
            break
        bytes_data.append(int("".join(chunk), 2))
    try:
        raw = bytes(bytes_data)
        return base64.b64decode(raw).decode("utf-8")
    except Exception:
        return None


def extract_hidden_words(text):
    hidden = []
    for pattern in HIDDEN_PATTERNS:
        hidden += re.findall(pattern, text)

    for encoded in re.findall(f"{ZW_START}([\u200c\u200d]+){ZW_END}", text):
        decoded = decode_hidden(encoded)
        if decoded:
            hidden.append(decoded)

    return hidden


def reveal_hidden(text):
    hidden = extract_hidden_words(text)
    if not hidden:
        return "Không tìm thấy từ bị ẩn. Hãy dùng lệnh merge để nhúng từ ẩn vào văn bản."
    return "\n".join(hidden)


def merge_hidden(normal, hidden):
    if not hidden:
        return "Không có từ bị ẩn để ghép. Vui lòng cung cấp từ ẩn."

    hidden_seq = encode_hidden(hidden)
    merged = normal
    if re.search(r"\[.*?\]", merged) or re.search(r"<hidden>.*?</hidden>", merged) or re.search(r"\{.*?\}", merged):
        merged = re.sub(r"\[.*?\]", hidden_seq, merged, count=1)
        merged = re.sub(r"<hidden>.*?</hidden>", hidden_seq, merged, count=1)
        merged = re.sub(r"\{.*?\}", hidden_seq, merged, count=1)
        merged = re.sub(r"(\s)" + re.escape(hidden_seq) + r"(\s)", r"\1" + hidden_seq, merged)
    else:
        merged = f"{merged}{hidden_seq}"

    return merged


def main():
    parser = argparse.ArgumentParser(
        description="zero-write: nhúng từ ẩn vào văn bản mà vẫn hiển thị bình thường"
    )
    parser.add_argument("command", nargs="?", help="reveal|merge hoặc văn bản để xử lý")
    parser.add_argument("pos2", nargs="?", help="Chuỗi bình thường hoặc văn bản chứa ẩn")
    parser.add_argument("pos3", nargs="?", help="Từ bị ẩn khi dùng merge")

    args = parser.parse_args()

    if args.command in ("reveal", "show"):
        if not args.pos2:
            parser.error("Thiếu chuỗi để hiện từ bị ẩn. Ví dụ: python main.py reveal \"Tôi [yêu] em\"")
        print(reveal_hidden(args.pos2))
        return

    if args.command in ("merge", "join"):
        if not args.pos2 or not args.pos3:
            parser.error("Thiếu tham số cho ghép. Ví dụ: python main.py merge \"Tôi [___] em\" \"yêu\"")
        print(merge_hidden(args.pos2, args.pos3))
        return

    if args.command is None:
        parser.print_help()
        return

    if args.pos2 is None:
        print(reveal_hidden(args.command))
        return

    print(merge_hidden(args.command, args.pos2))


if __name__ == "__main__":
    main()
