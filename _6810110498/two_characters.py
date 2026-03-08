def two_characters(s):
    # พยายามสร้าง string ที่ยาวที่สุดจากตัวอักษรแค่ 2 ชนิดที่สลับกันไปมา
    unique_chars = list(set(s))
    max_len = 0
    
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            # กรองเอาแค่ 2 ตัวที่เลือก
            filtered = [c for c in s if c == char1 or c == char2]
            
            # เช็คว่ามันสลับกันจริงมั้ย
            valid = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k+1]:
                    valid = False
                    break
            
            if valid:
                max_len = max(max_len, len(filtered))
                
    return max_len
