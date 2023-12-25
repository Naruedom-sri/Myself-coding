pi = 3.1415926
print(" *** Finding circumference ***  ")
radius = input("Enter radius : ")
radius = float(radius)
circumference = 2*pi*radius
print(f"Circumference = {circumference}")
print(f"Circumference = {circumference:0.2f}") #แสดงผลจำนวนทศนิยม 2 ตำแหน่ง
print(f"whole number => {int(circumference)}")  #แสดงผลเฉพาะส่วนที่เป็นจำนวนเต็ม4