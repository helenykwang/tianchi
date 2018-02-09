#!/usr/bin/python
#-*- coding:utf-8 -*-


import itertools

def main():
    smoney = [0, 0, 110, 259, 260, 280, 300, 320, 320, 410, 450, 450]

    pockets = set()
    bigp = set()
    has_big = {0:0, 1:0, 2:0, 3:0, 4:0}
    cnt = 0

    for _pocket in itertools.combinations(smoney, 3):
        remain_money = smoney[:]
        for _ele in _pocket:
            remain_money.remove(_ele)
        
        # print(len(remain_money)) #remain 9
        for _pocket2 in itertools.combinations(remain_money, 3):            
            remain_money_2 = remain_money[:]
            for _ele in _pocket2:
                remain_money_2.remove(_ele)

            for _pocket3 in itertools.combinations(remain_money_2, 3):

                item = [_pocket, _pocket2, _pocket3]
                bigp_cnt = len(list(filter(lambda x:sum(x)>1100, item)))
                
                if sum(smoney)-sum(_pocket3)-sum(_pocket2)-sum(_pocket)>1100:
                    bigp_cnt += 1

                old_len = len(pockets)
                pockets.add(str(sorted(item))[1:-1] + '_%d'%(bigp_cnt)) 
                if len(pockets) == old_len:
                    pass
                else:
                    has_big[bigp_cnt] += 1

    print(has_big)
    print(len(pockets))
    # print(len(pockets))
    # print(collections.Counter(all_comb))
    # unhashable type: 'list'
    # {0: 241920, 1: 127680, 2: 0, 3: 0, 4: 0}
    # 369600

    with open("out_comb.txt", "w")as fp:
        for e in pockets:
            fp.write(e)
            fp.write("\n")


if __name__ == '__main__':
    main()
