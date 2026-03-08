def alternating_characters(s):
    # นับจำนวนตัวที่ต้องลบทิ้งเพื่อไม่ให้มีตัวอักษรซ้ำติดกัน
    deletions = 0
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            deletions += 1
    return deletions
