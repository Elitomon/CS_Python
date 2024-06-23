# using two parellel arrays
# arrays are fixed length, ordered, and allow duplicates

months = ['Jan', 'Feb', 'March', 'Apr']
sales = ['80000', '100000', '120000', '150000']

month = input('For which month do you want sales? ')
for i in range (0, len(months), 1):
    print('i equals', i, 'months', months[i])
    print ('sales', sales[i])
    if months[i] == month:
        print('sales for', months[i], 'were', sales[i])

print ('done')