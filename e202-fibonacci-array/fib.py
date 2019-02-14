def _?_: # defines function "fib" with inpara "N"
    assert(N > 2)
    p_1 = 1
    p_2 = 1
    cnt = 2
    print(p_1)
    print(p_2)
    _?_    # starts a while loop till "cnt" hits "N"
        _?_# calculate next p by adding p_1 and p_2
        print(p)
        p_2 = _?_# p_2 should be previous p_1
        p_1 = _?_# p_1 should be previous p
        _?_ # this line increase "cnt" by 1

fib(10)

