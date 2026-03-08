from _6810110498.funny_string import funny_string
from _6810110498.alternating_characters import alternating_characters
from _6810110498.caesar_cipher import caesar_cipher

def main():
    print("--- การบ้านวิชา Testing (รหัสนิสิต: 6810110498) ---")
    print("1. เล่น Funny String")
    print("2. เล่น Alternating Characters")
    print("3. เล่น Caesar Cipher")
    print("4. เลิกเล่น")
    
    while True:
        choice = input("\nเลือกโหมด: ")
        if choice == "1":
            s = input("ใส่ข้อความ: ")
            print(f"ผลลัพธ์: {funny_string(s)}")
        elif choice == "2":
            s = input("ใส่ข้อความ: ")
            print(f"ตัวที่ต้องลบ: {alternating_characters(s)}")
        elif choice == "3":
            s = input("ใส่ข้อความ: ")
            try:
                k = int(input("เลื่อนไปกี่ตัว: "))
                print(f"ผลลัพธ์: {caesar_cipher(s, k)}")
            except ValueError:
                print("ใส่เลขไม่ถูกครับ")
        elif choice == "4":
            print("บ๊ายบาย!")
            break
        else:
            print("เลือกเลข 1-4 นะครับ")

if __name__ == "__main__":
    main()
