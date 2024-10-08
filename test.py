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
  

def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def gcf(num_one, num_two):
    
    factors_one = find_factors(num_one)
    factors_two = find_factors(num_two)
    
    
    common_factors = list(set(factors_one) & set(factors_two))
    
    
    return max(common_factors)


num_one = int(input("Type in the first number: "))
num_two = int(input("Type in the second number: "))


result = gcf(num_one, num_two)
print(f"The Greatest Common Factor of {num_one} and {num_two} is: {result}")

  
