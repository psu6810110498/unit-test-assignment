# Unit Test Assignment

**รหัสนักศึกษา:** 6810110498  
**ชื่อ-นามสกุล:** มูฮัมหมัดฟาอีฟ ยามา

งานชิ้นนี้เป็นส่วนหนึ่งของวิชา Testing โดยมีการแยกโครงสร้างระหว่าง Production Code และ Test Code อย่างชัดเจน พร้อมทั้งมีการใช้ Test Double (Stub) เพื่อคะแนนพิเศษ

## โครงสร้างโปรเจกต์

```text
unit-test-assignment/
├── _6810110498/                    # Production code (แยกตามรหัสนักศึกษา)
│   ├── funny_string.py             # Logic Funny String
│   ├── alternating_characters.py    # Logic Alternating Characters
│   ├── caesar_cipher.py            # Logic Caesar Cipher
│   ├── two_characters.py           # Logic Two Characters
│   ├── grid_challenge.py           # Logic Grid Challenge
│   └── result_reporter.py          # Service สำหรับรายงานผล (ใช้ทดสอบ Stub)
├── tests/                          # Test code
│   ├── test_funny_string.py
│   ├── test_alternating_characters.py
│   ├── test_caesar_cipher.py
│   ├── test_two_characters.py
│   ├── test_grid_challenge.py
│   └── test_stubs.py               # การทดสอบโดยใช้ Stub (Bonus)
├── main.py                         # โปรแกรมสำหรับรันผ่าน CLI
└── pyproject.toml                  # ไฟล์ตั้งค่าโปรเจกต์
```

## วิธีการติดตั้งและใช้งาน

### 1. ติดตั้ง Dependencies
โปรเจกต์นี้ใช้ `pytest` สำหรับการทดสอบ:
```bash
pip install pytest pytest-cov
```

### 2. วิธีการรันโปรแกรม (CLI)
คุณสามารถรันโปรแกรมเพื่อทดสอบ Logic ต่างๆ ผ่านหน้าจอ Command Line:
```bash
python main.py
```

### 3. วิธีการรัน Unit Test
หากต้องการตรวจสอบความถูกต้องของ Code ทั้งหมด สามารถรันคำสั่ง:
```bash
python3 -m pytest -v
```

## รายละเอียดอัลกอริทึม
1. **Funny String**: เช็คว่าผลต่างของรหัสตัวอักษรระหว่าง String เดิมกับ String ย้อนกลับมันขนานกันมั้ย
2. **Alternating Characters**: นับจำนวนตัวอักษรที่ต้องลบเพื่อไม่ให้มีตัวซ้ำติดกัน
3. **Caesar Cipher**: การเข้ารหัสแบบเลื่อนตัวอักษร (Shift Cipher)
4. **Two Characters**: หาความยาวที่มากที่สุดของ String ที่เกิดจากตัวอักษร 2 ชนิดสลับกัน
5. **Grid Challenge**: จัดเรียงแถวใน Grid แล้วเช็คว่าลำดับตัวอักษรในคอลัมน์ยังเรียงกันมั้ย
6. **Result Reporter (Stub)**: แสดงการใช้ Test Double (Stub) เพื่อส่งผลลัพธ์ผ่าน Service (คะแนนพิเศษ)
