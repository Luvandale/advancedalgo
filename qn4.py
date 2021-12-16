# def superDigit(stringN, PconcatofN):    
#     bigDigitStr = PconcatofN * stringN
#     digit = int(bigDigitStr)
#     return recurseCall(digit)

# def recurseCall(digit):
#     if len(str(digit)) == 1:
#         return digit
#     numCharList = list(str(digit))
#     sum = 0
#     for a in numCharList:
#         sum += int(a)   
#     return recurseCall(str(sum))


# print(superDigit("148", 3))
def s_main(n,k):
    def s_digit(p):
        # check if it is singlr digit
        if len(str(p) )== 1:
           
            return p
        else:
            q = list(str(p))
            r = 0
            # loop through q
            for i in q:
                # this will add the values to q inorder to generate a different smaller q
                r+= int(i)
                # return the new generated q value
            return s_digit(str(r))
    t = s_digit(int(n))
    return s_digit(t*k)
print(s_main("148",3))
        
    