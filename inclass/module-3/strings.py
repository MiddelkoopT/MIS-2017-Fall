#!/usr/bin/env python3
## Simple python string class to demonstrate testing

## Basic functions
def concatinate(s1,s2):
    return str(s1)+str(s2)

def last(s1):
    return s1[-1]

def first(s1):
    return s1[0]


## internal test
def test():
    ## simple tests
    print("+++","concatinate AAA BBB",concatinate("AAA","BBB"))
    assert concatinate("AAA","BBB")=="AAABBB"

    ## this one would break if the "str" was removed (try it)
    print("+++","concatinate 111 222",concatinate(111,222))
    assert concatinate(111,222)=="111222"


## JSON extended tests
def testJSON(filename):
    import json

    f=open(filename)
    tests=json.load(f)
    f.close()

    for test in tests:
        print("+++",test["name"],test)
        operator=test["operator"]
        expected=test["expected"]
        reslut=None
        if operator=="c":
            result=concatinate(test["s1"],test["s2"])
        elif operator=="l":
            result=last(test["s1"])
        elif operator=="f":
            result=first(test["s1"])
        print("---",expected,result)
        assert expected==result


## entry point if module called directly
if __name__=='__main__':
    print("strings.py test")
    test()
    testJSON("strings.json")
    print("strings.py done")

