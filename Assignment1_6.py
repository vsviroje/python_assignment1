def chknum(n):
    if n>0:
        print("Positive Number");
    elif n<0:
        print("negative Number");
    else:
        print("zero");


if __name__=='__main__':
    n=int(input());
    chknum(n);