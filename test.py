# number = [1,2,3,4,5,6]
# print(number[3])
# #number
# color = input("what color is the sky?")
# if color == "blue":
#     print("correct")
# else:
#     print("incorrect")
# #color

#odd or even
# def evenodd():
#     evenodd=int(input("give me a number: "))
#     if evenodd % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# evenodd()

#bill value

#def thing ():
    #bill = int(input("whats the bill?"))

    #quality = input("what is the quality?:['bad', 'okay', 'good', 'great']")
   # if quality == "bad":
    #    print(bill) 
    #elif quality == "okay":
     #   print(bill * 1.15) 
    #elif quality == "good":
  #      print (bill * 1.20)
   # elif quality == "great":
 #       print(bill * 1.25)

#thing()

#all factors

#def find_factors():
      #num = int(input("type in a number"))
      #factors = []
      #for i in range(1, num + 1):
              #if num % i == 0:
                  #factors.append(i)
      #print(factors)
#find_factors()

#gcf

""" def gcf(num_one, num_two):
    
   num_1 = int(input("type in a number"))
      factors = []
      for i in range(1, num + 1):
          if num % i == 0:
              factors.append(i)
      print(factors)
find_factors()
num_2 = int(input("type in another number"))
      factors = []
      for i in range(1, num + 1):
          if num % i == 0:
              factors.append(i)
      print(factors)
find_factors()
def gcf(num_1, num_2):
  num_1 = int(input("type in a number"))
  num_2 = int(input("type in another number")
  num_1 % 0 and num_2 ==0 """
  

#def find_factors(num):
  #  factors = []
 #   for i in range(1, num + 1):
 #       if num % i == 0:
 #           factors.append(i)
#    return factors


num_one = int(input("give me a number"))
num_two = int(input("give me another number"))
gcf = 1

for i in range(1, min(num_one, num_two)):
       ## now check if i is factor of BOTH numbers
    if num_one % i == 0 and num_two % i == 0:
        gcf = i
print(f"The Greatest Common Factor is {gcf}")
