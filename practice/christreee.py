day = int(input('kindly enter your prefered day of christmas: '))

days_dict = {1:'first',
            2:'second',
            3:'third',
            4:'fourth',
            5:'fifth',
            6:'sixth',
            7:'seventh',
            8:'eighth',
            9: "ninth",
            10:"tenth",
            11:"eleventh",
            12:"twelfth"}

days_list = ('And a Partridge in a Pear Tree!','Two Turtle Doves','Three French Hens','Four Calling Birds',
         'Five Golden Rings','Six Geese a Laying','Seven Swans a Swimming','Eight Maids a Milking',
         'Nine Ladies Dancing','Ten Lords a Leaping','Eleven Pipers Piping','12 Drummers Drumming')

print('On the',days_dict[day],'day of Christmas my true love gave to me:')

result = days_list[day-1::-1]

if day == 1:
  print('A partridge in a pair tree')
else:
  for item in result:
    print(item)