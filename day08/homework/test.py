

 #თუ ერთრთი პირობა არასწორია and ოპერატორის გამოყენებისას დაგვიბრუნდება false,თუ ორივე სწორია მივიღებთ True, თუ ორივე არასწორია მივიღებთ false.

#print(True and True)  #True
#print(True and False)  #False
#print(False and True)  #False
#print(False and False) #False




# or ოპერატორის გამოყენებისას ერთერთი პირობა უნდა იყოს სწორი,თუ ერთერთი პირობა სწორია და მეორე არაწსორი, მივიღებთ True-ს, თუ ორივე სწორია მივიღებთ True,თუ ორივე არასწორია მივიღებთ False.
#print(True or True) #True
#print(True or False) #True
#print(False or True) #True
#print(False or False) #False



#print("-------------- AND ----------")
#num = 5

#print(num >= 1 and num <= 10) #5 მეტია 1 ზე ამიტომ true, 5 ნაკლებია 10ზე ამიტომ True, საბოლოოდ True
#print(num >= 1 and num <= 4) #მეორე პირობა არასწორია ამიტომ and ოპერატორის გამო მივიღებთ  false.
#print(num > 5 and num <=10) #რადგან პირველი პირობა არასწორია მივიღებთ false.
#print(num > 5 and num > 10) #რადგან ორივე პირობა არასწორია მივიღებთ false.


#print("-------------- OR ----------")


#print(num >= 1 or num <= 10) # 5 მეტია 1 ზე ამიტომ true, 5 ნაკლებია 10ზე ამიტომ True, საბოლოოდ True
#print(num >= 1 or num <= 4) # მეორე პირობა არასწორია ამიტომ or ოპერატორის გამო ერთერთი პირობა თუ არის სწორი  მივიღებთ  True.
#print(num > 5 or num <=10) #True
#print(num > 5 or num > 10) #რადგან ორივე პირობა არასწორია მივიღებთ false.



#მაგალითი and ოპერატორი-->
#num = 10
#print(num < 20 and num > 20) #False
#print(num >= 5 and num <=10) #true
#print(num >= 15 and num >=11) #false
#print(num == 10 and num == 15) #false


#მაგალითი or ოპერატორი-->
#num = 10
#print(num < 20 or num > 20) #true
#print(num >= 5 or num <=10) #true
#print(num >= 15 or num >=11) #false
#print(num == 10 or num == 15) #True