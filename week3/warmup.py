def mydict(d,k,val):
    d.update({k:val})
    #d[k] = val
    print(d)

test_dict = {'dog':'bark',"cat":'meow'}

test_dict2={'tomato':True,"cheese":False}

mydict(test_dict2,'pickles','True')
mydict(test_dict,'fish','glug')