#lightswith_procedure.py
#สร้างฟังก์ชั่นเปิดไฟ
global switch_status
def turnon():
    global switch_status
    switch_status = True #เปลี่ยนสถานะเป็นเปิดไฟ

#สร้างฟังก์ชั่นปิดไฟ
def turnoff():
    global switch_status
    switch_status = False

switch_status = False #ปิด

print(f"Status = {switch_status}") #False
turnon()
print(f"Status = {switch_status}") #True
turnoff()
print(f"Status = {switch_status}") #False
turnoff()
print(f"Status = {switch_status}") #Flase