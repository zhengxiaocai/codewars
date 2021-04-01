# https://www.codewars.com/kata/5b728f801db5cec7320000c7/train/python


def solve(st, k):
    if len(st) < k:
        return ''
    st = list(st)
    for i in range(k):
        st.remove(min(set(st)))
    return ''.join(st)


def solve_best(st, k):
    for l in sorted(st)[:k]:
        st = st.replace(l, '', 1)
    return st


if __name__ == '__main__':
    print(solve('abracadabra', 1), 'bracadabra')
    print(solve('abracadabra', 2), 'brcadabra')
    print(solve('abracadabra', 6), 'rcdbr')
    print(solve('abracadabra', 8), 'rdr')
    print(solve('abracadabra', 50), '')
    test_st = 'ijlwvsoevutryetpkddbmjzfowotkxretrldcxzpcmwwhqqsxavzpmpdqormaeojdoxuhdaulzsqjmtvyeyqpppgjdnfkzcqpaywgkvpnfteuqsfwkkomzylecljizlkbcovcseddfuajpzswvhkfhcgvelyorlcunejjkqzxsmbpsdvtupmcplcllxjmlrchwmhzwugsbqnwfpmhkejdjljcnkybffdujryfkjtzupocjiuuzrtfgvgkpkxpkvtpwbcezzxxtzrwrtusicnfeieypfktrfrcztpzfljumotylxhqojslrkqndfdjehibtfyjeddgxbrqldrkyrfqphrjygwrjxftnodvwyikugefimpcohezsttcwdcjrjadfmygidptlpyhsraylvoqdkfwftejclgvnduzteagdfjxxsgsgqypniprnrhxhgujqlvipgjmkfvbxhydkrwwvinrfnajwhadsnjvufonrddnigqphvqspmytpneqyfxfwekgaqsqefxvgtoynvwtqugdnxighhtjmqeruynotwkbdxkvdvjhuloqdpkbxzlhqtvmfhsbferydbryjguvritswuggrutwujgdofekqkbjpuutcupimzaaqwfoevdcrogdgxnocjljafnumsfdfaqmicnlipvyhjpaubsinbqixpjdntephjxrgqedhdgergfwospzezqbnozvdrtwegwhjgwgsyxyhtvqftzyuquxikczpzstpwfgwwrvtexgmjymefntxsawnarhkiavotdrmmmrowflbypodmqjwugyhlelywgaspjefaxrjocirximnkfppvlwkhlxsfgiwuihlvzznzfimmnyaqxmfhoeyeurmkffscqjabxvgqpgolnbycyehngumdzdroaumfcqmeiimvzexuoyspigrkfywpypbwaiuvnipgakgtvuruaytheghtzfykblqrxonujhhwhjgdnjbbvtydyeoqcyybqkpaeujcawwmjfcyrkpvmyhyatydgdkwgydxuwtpaflytinxswywnqeezijfvrzexfjzsozyzyvezkddjkldxzszlfsxubecsgqmdffwuypqiirtjpvqgslsyryngvlqlozintlgljrituesbhlvjpfzmsnmwfycpfkcclrjfvasdvtvlyxsdqjzvniujqhlsnxdfgkvrafsrzyulzhqthmckcjvlsoqjmefijuvlgfmpmfgtrotkdfknytgorlzlubkihjbltfkivgleognkxjslnojovxksawmjukljwnmgrkhquumpzxwgpjmdzhxsezeoudyxafthhkyirvzqfcnlnytnhrxqmxdygkefsmobjwetcuydoeh'
    test_k = 1233
    print(solve(test_st, test_k))
