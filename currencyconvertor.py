file1 = open("currencyData.txt", "r")
content = file1.read()
file1.close()
list1 = content.split()

while True:
    print("\t<Indian Currency Convertor>")
    print("Choose Currency Name and Type It Below")
    i = 0
    while i < len(list1):
        print(list1[i], end=" | ")
        i += 3
    currency = input("\nINR to : ")
    rupees = float(input("Enter Quantity : "))
    for i in range(len(list1)):
        if currency == list1[i]:
            print(f"{rupees} {list1[i]} = {round(float(list1[i + 2]) * rupees, 6)} Rupees")
            print(f"{rupees} Rupees = ", round(rupees / float(list1[i + 2]), 6), f" {list1[i]}")

    x = input("Convert Again Press Y Else N ").lower()
    if x != "y":
        print("program exited")
        break
