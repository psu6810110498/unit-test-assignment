def funny_string(s):
    # ฟังก์ชันเช็คว่าความแตกต่างของรหัสตัวอักษรระหว่าง string เดิมกับ string ย้อนกลับมันขนานกันมั้ย
    r = s[::-1]
    for i in range(1, len(s)):
        diff1 = abs(ord(s[i]) - ord(s[i-1]))
        diff2 = abs(ord(r[i]) - ord(r[i-1]))
        if diff1 != diff2:
            return "Not Funny"
    return "Funny"
