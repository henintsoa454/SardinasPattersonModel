class SardinasPatterson:
    def __init__(self):
        pass

    @staticmethod
    def generate_cn(c, n):
        if n == 0:
            return set(c)
        else:
            # create a set to hold our new elements
            cn = set()

            # generate c_(n-1)
            cn_minus_1 = SardinasPatterson.generate_cn(c, n - 1)

            for u in c:
                for v in cn_minus_1:
                    if (len(u) > len(v)) and u.find(v) == 0:
                        cn.add(u[len(v):])
            for u in cn_minus_1:
                for v in c:
                    if len(u) > len(v) and u.find(v) == 0:
                        cn.add(u[len(v):])
            return cn

    @staticmethod
    def generate_c_infinity(c):
        cs = []
        c_infinity = set()
        n = 1
        cn = SardinasPatterson.generate_cn(c, n)
        while len(cn) > 0:
            if cn in cs:
                break
            else:
                cs.append(cn)
                c_infinity = c_infinity.union(cn)
                n += 1
                cn = SardinasPatterson.generate_cn(c, n)
                # print( c_infinity)
        return c_infinity

    @staticmethod
    def sardinas_patterson_theorem(c):
        c_infinity = SardinasPatterson.generate_c_infinity(c)
        return len(c.intersection(c_infinity)) == 0

    @staticmethod
    def make_uniquely_decodable(c):
        if SardinasPatterson.sardinas_patterson_theorem(c):
            return c

        for codeword1 in c:
            c_minus_1 = c.copy()
            c_minus_1.remove(codeword1)
            if SardinasPatterson.sardinas_patterson_theorem(c_minus_1):
                return c_minus_1

        for codeword1 in c:
            for codeword2 in c:
                if codeword1 == codeword2:
                    continue
                c_minus_2 = c.copy()
                c_minus_2.remove(codeword1)
                c_minus_2.remove(codeword2)
                if SardinasPatterson.sardinas_patterson_theorem(c_minus_2):
                    return c_minus_2

        return None

    @staticmethod
    def is_decodable(c):
        res = SardinasPatterson.make_uniquely_decodable(c)
        if res is None:
            return False
        else:
            return True