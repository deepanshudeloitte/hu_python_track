class StringClass:
    def __init__(self, s):
        self.s = s

    def len_str(self):
      print(len(self.s))

    def str_to_list(self):
        print([char for char in self.s])


class PairPossible(StringClass):

    def __init__(self, s):
        StringClass.__init__(self, s)

    def pair(self):
        has = {}
        for i in self.s:
            if i in has:
                has[i] += 1
            else:
                has[i] = 1

        lis = []
        for i, val in has.items():
            if val % 2 == 0:
                lis.append(i)

        return lis


class SearchCommonElements(PairPossible):

    def __init__(self, s1, ans):
        self.s1 = s1
        self.ans = ans

    def search(self):
        res = []
        for i in self.ans:
            if i in self.s1:
                res.append(i)
        return res


c = StringClass("12314532")
c.len_str()
c.str_to_list()
p = PairPossible(StringClass)
print(p.pair())

# print(ans)
# s = SearchCommonElements("12345", ans)
# print(s.search())
