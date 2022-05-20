def sum_and_greet(*number,**students):
    sum=1
    for b in number:
        sum*=b
        print(sum)
    print(f"Hello{students}")