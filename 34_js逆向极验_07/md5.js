function MD5(e) {
    function c(e, t) {
        return e << t | e >>> 32 - t;
    }
    function u(e, t) {
        var n, r, o, i, a;
        return o = 2147483648 & e,
            i = 2147483648 & t,
            a = (1073741823 & e) + (1073741823 & t),
            (n = 1073741824 & e) & (r = 1073741824 & t) ? 2147483648 ^ a ^ o ^ i : n | r ? 1073741824 & a ? 3221225472 ^ a ^ o ^ i : 1073741824 ^ a ^ o ^ i : a ^ o ^ i;
    }
    function t(e, t, n, r, o, i, a) {
        return u(c(e = u(e, u(u(function s(e, t, n) {
            return e & t | ~e & n;
        }(t, n, r), o), a)), i), t);
    }
    function n(e, t, n, r, o, i, a) {
        return u(c(e = u(e, u(u(function s(e, t, n) {
            return e & n | t & ~n;
        }(t, n, r), o), a)), i), t);
    }
    function r(e, t, n, r, o, i, a) {
        return u(c(e = u(e, u(u(function s(e, t, n) {
            return e ^ t ^ n;
        }(t, n, r), o), a)), i), t);
    }
    function o(e, t, n, r, o, i, a) {
        return u(c(e = u(e, u(u(function s(e, t, n) {
            return t ^ (e | ~n);
        }(t, n, r), o), a)), i), t);
    }
    function i(e) {
        var t, n = '', r = '';
        for (t = 0; t <= 3; t++)
            n += (r = '0' + (e >>> 8 * t & 255)['toString'](16))['substr'](r['length'] - 2, 2);
        return n;
    }
    var a, s, l, _, f, p, h, d, g, v;
    for (a = function m(e) {
        var t, n = e['length'], r = n + 8, o = 16 * (1 + (r - r % 64) / 64), i = Array(o - 1), a = 0, s = 0;
        while (s < n)
            a = s % 4 * 8,
                i[t = (s - s % 4) / 4] = i[t] | e['charCodeAt'](s) << a,
                s++;
        return a = s % 4 * 8,
            i[t = (s - s % 4) / 4] = i[t] | 128 << a,
            i[o - 2] = n << 3,
            i[o - 1] = n >>> 29,
            i;
    }(e = function w(e) {
        e = e['replace'](/\r\n/g, '\n');
        for (var t = '', n = 0; n < e['length']; n++) {
            var r = e['charCodeAt'](n);
            r < 128 ? t += String['fromCharCode'](r) : (127 < r && r < 2048 ? t += String['fromCharCode'](r >> 6 | 192) : (t += String['fromCharCode'](r >> 12 | 224),
                t += String['fromCharCode'](r >> 6 & 63 | 128)),
                t += String['fromCharCode'](63 & r | 128));
        }
        return t;
    }(e)),
             h = 1732584193,
             d = 4023233417,
             g = 2562383102,
             v = 271733878,
             s = 0; s < a['length']; s += 16)
        d = o(d = o(d = o(d = o(d = r(d = r(d = r(d = r(d = n(d = n(d = n(d = n(d = t(d = t(d = t(d = t(_ = d, g = t(f = g, v = t(p = v, h = t(l = h, d, g, v, a[s + 0], 7, 3614090360), d, g, a[s + 1], 12, 3905402710), h, d, a[s + 2], 17, 606105819), v, h, a[s + 3], 22, 3250441966), g = t(g, v = t(v, h = t(h, d, g, v, a[s + 4], 7, 4118548399), d, g, a[s + 5], 12, 1200080426), h, d, a[s + 6], 17, 2821735955), v, h, a[s + 7], 22, 4249261313), g = t(g, v = t(v, h = t(h, d, g, v, a[s + 8], 7, 1770035416), d, g, a[s + 9], 12, 2336552879), h, d, a[s + 10], 17, 4294925233), v, h, a[s + 11], 22, 2304563134), g = t(g, v = t(v, h = t(h, d, g, v, a[s + 12], 7, 1804603682), d, g, a[s + 13], 12, 4254626195), h, d, a[s + 14], 17, 2792965006), v, h, a[s + 15], 22, 1236535329), g = n(g, v = n(v, h = n(h, d, g, v, a[s + 1], 5, 4129170786), d, g, a[s + 6], 9, 3225465664), h, d, a[s + 11], 14, 643717713), v, h, a[s + 0], 20, 3921069994), g = n(g, v = n(v, h = n(h, d, g, v, a[s + 5], 5, 3593408605), d, g, a[s + 10], 9, 38016083), h, d, a[s + 15], 14, 3634488961), v, h, a[s + 4], 20, 3889429448), g = n(g, v = n(v, h = n(h, d, g, v, a[s + 9], 5, 568446438), d, g, a[s + 14], 9, 3275163606), h, d, a[s + 3], 14, 4107603335), v, h, a[s + 8], 20, 1163531501), g = n(g, v = n(v, h = n(h, d, g, v, a[s + 13], 5, 2850285829), d, g, a[s + 2], 9, 4243563512), h, d, a[s + 7], 14, 1735328473), v, h, a[s + 12], 20, 2368359562), g = r(g, v = r(v, h = r(h, d, g, v, a[s + 5], 4, 4294588738), d, g, a[s + 8], 11, 2272392833), h, d, a[s + 11], 16, 1839030562), v, h, a[s + 14], 23, 4259657740), g = r(g, v = r(v, h = r(h, d, g, v, a[s + 1], 4, 2763975236), d, g, a[s + 4], 11, 1272893353), h, d, a[s + 7], 16, 4139469664), v, h, a[s + 10], 23, 3200236656), g = r(g, v = r(v, h = r(h, d, g, v, a[s + 13], 4, 681279174), d, g, a[s + 0], 11, 3936430074), h, d, a[s + 3], 16, 3572445317), v, h, a[s + 6], 23, 76029189), g = r(g, v = r(v, h = r(h, d, g, v, a[s + 9], 4, 3654602809), d, g, a[s + 12], 11, 3873151461), h, d, a[s + 15], 16, 530742520), v, h, a[s + 2], 23, 3299628645), g = o(g, v = o(v, h = o(h, d, g, v, a[s + 0], 6, 4096336452), d, g, a[s + 7], 10, 1126891415), h, d, a[s + 14], 15, 2878612391), v, h, a[s + 5], 21, 4237533241), g = o(g, v = o(v, h = o(h, d, g, v, a[s + 12], 6, 1700485571), d, g, a[s + 3], 10, 2399980690), h, d, a[s + 10], 15, 4293915773), v, h, a[s + 1], 21, 2240044497), g = o(g, v = o(v, h = o(h, d, g, v, a[s + 8], 6, 1873313359), d, g, a[s + 15], 10, 4264355552), h, d, a[s + 6], 15, 2734768916), v, h, a[s + 13], 21, 1309151649), g = o(g, v = o(v, h = o(h, d, g, v, a[s + 4], 6, 4149444226), d, g, a[s + 11], 10, 3174756917), h, d, a[s + 2], 15, 718787259), v, h, a[s + 9], 21, 3951481745),
            h = u(h, l),
            d = u(d, _),
            g = u(g, f),
            v = u(v, p);
    return (i(h) + i(d) + i(g) + i(v))['toLowerCase']();

}


console.log(MD5('123456'))