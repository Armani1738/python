for row in range(1,  13):
     for column in range(2,  21):
         print(f"{column:>2} * {row:>2} = {row * column:>3}", end='\t\t')
print()