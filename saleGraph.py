import matplotlib as plt

x = []
i=1
for i in range(12):
    monthSale = str(input("Enter the sales for each month from Jan-Dec: "))
    x.append(monthSale)
    i += 1

y = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

plt.plot(y, x, marker = 'o')

plt.title("Past Year Sales Review by Month")
plt.xlabel("Sales ($)")
plt.ylabel("Month")

plt.show()
