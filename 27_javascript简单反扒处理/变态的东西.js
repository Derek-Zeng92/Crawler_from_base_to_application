function txsdefwsw() {
    var r = "V", n = "5", e = "8";

    function o(r) {
        if (!r) return "";
        for (var t = "", n = 44106, e = 0; e < r.length; e++) {
            var o = r.charCodeAt(e) ^ n;
            n = n * e % 256 + 2333, t += String.fromCharCode(o)
        }
        return t
    }

    try {
        var a = ["r", o("갯"), "g", o("갭"), function (t) {
            if (!t) return "";
            for (var o = "", a = r + n + e + "7", c = 45860, f = 0; f < t.length; f++) {
                var i = t.charCodeAt(f);
                c = (c + 1) % a.length, i ^= a.charCodeAt(c), o += String.fromCharCode(i)
            }
            return o
        }("@"), "b", "e", "d"].reverse().join("");
        !function c(r) {
            (1 !== ("" + r / r).length || 0 === r) && function () {
            }['constructor'](a)(), c(++r)
        }(0)
    } catch (a) {
        setTimeout(txsdefwsw, 100)
    }
}