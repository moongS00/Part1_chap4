def scoreCal(n1, n2, n3, n4, n5):
    total_acore = n1 + n2 + n3 + n4 + n5
    avg = total_acore / 5

    res1 = "Pass" if n1 >= 40 else "Fail"
    res2 = "Pass" if n2 >= 40 else "Fail"
    res3 = "Pass" if n3 >= 40 else "Fail"
    res4 = "Pass" if n4 >= 40 else "Fail"
    res5 = "Pass" if n5 >= 40 else "Fail"

    if n1 >= 40 and n2 >= 40 and n3 >= 40 and n4 >= 40 and n5 >= 40:
        if avg >= 60:
            final_res = "Pass!"
        else:
            final_res = "Fail!"
    else:
        final_res = "Fail!"

    print(f'{n1} : {res1}')
    print(f'{n2} : {res2}')
    print(f'{n3} : {res3}')
    print(f'{n4} : {res4}')
    print(f'{n5} : {res5}')
    print(f'총점 : {total_acore}')
    print(f'평균 : {avg}')
    print(f'final : {final_res}')