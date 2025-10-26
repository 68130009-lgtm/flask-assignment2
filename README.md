# Flask Assignment 2

## รายละเอียดงาน
พัฒนาเว็บด้วย Python Flask ที่มี:
1. เปิดได้จาก host ใดก็ได้ (`0.0.0.0`)
2. Path `/sum/xx/yy` → แสดงผลรวมของตัวเลขสองตัว พร้อมดัก error
3. Path `/concat/xx/yy` → แสดงการเชื่อมข้อความสองตัว

## ตัวอย่างการทดสอบ
- `/sum/12/3` → “The result of sum between 12 and 3 is 15”
- `/sum/12/a` → “You are using miss data type for operation”
- `/concat/12/3` → “The result of concatenate between 12 and 3 is 123”

## วิธีรัน
```bash
pip install flask
python app.py
