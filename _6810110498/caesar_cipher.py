def caesar_cipher(s, k):
    # เลื่อนตัวอักษรภาษาอังกฤษไปตามจำนวน k ที่กำหนด (รักษารูปแบบตัวเล็กตัวใหญ่)
    k %= 26
    res = []
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            res.append(chr((ord(char) - base + k) % 26 + base))
        else:
            res.append(char)
    return "".join(res)
