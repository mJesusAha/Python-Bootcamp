def iter_func(n, item_, word):
    i_n = 0
    for i in item_:
        str_i = str(i)
        if str_i.count(word):
            i_n = i_n + 1
            if i_n == n:
                return i
    return "none"


def sum_mass(item_, word):
    n = 0
    for i in item_:
        str_i = str(i)
        if str_i.count(word):
            n += 1
    return n


def fix_wiring1(cables, sockets, plugs):
    cables_sum = sum_mass(cables, "cable")
    sockets_sum = sum_mass(sockets, "socket")
    iter_n = min(cables_sum, sockets_sum)
    plug_ = "none"
    socket_ = ""
    cabl_ = ""
    for i in range(1, iter_n + 1):
        plug_ = iter_func(i, plugs, "plug")
        socket_ = iter_func(i, sockets, "socket")
        cabl_ = iter_func(i, cables, "cable")
        if plug_ == "none":
            yield "weld " + cabl_ + " to " + socket_ + " without plug"
        else:
            yield "plug " + cabl_ + " into " + socket_ + " using " + plug_
    return None
