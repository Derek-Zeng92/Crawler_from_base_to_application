var CryptoJS = require("crypto-js");

function $_BHIA(e){
    var t = ''
      , n = 0;
    (e || [])['length'];
    while (!t && e[n])
        t = e[n] && e[n][4],
        n++;
    if (!t)
        return e;
    for (var r = '', o = ['mouse', 'touch', 'pointer', 'MSPointer'], i = 0, a = o['length']; i < a; i++)
        0 === t['indexOf'](o[i]) && (r = o[i]);
    for (var s = e['slice'](), c = s['length'] - 1; 0 <= c; c--) {
        var u = s[c]
          , l = u[0];
        if (-1 < new J(['move', 'down', 'up'])['$_EGg'](l))
            0 !== (u[4] || '')['indexOf'](r) && s['splice'](c, 1);
    }
    return s;
}

function $_BHGD(e){
    var t = 32767;
    return 'number' != typeof e ? e : (t < e ? e = t : e < -t && (e = -t),
    Math['round'](e));
}

function J(e) {
    this['$_JIB'] = e || [];
}

J.prototype = {
     "$_EGg": function(e) {
        var t = this['$_JIB'];
        if (t['indexOf'])
            return t['indexOf'](e);
        for (var n = 0, r = t['length']; n < r; n += 1)
            if (t[n] === e)
                return n;
        return -1;
    },
    "\u0024\u005f\u0045\u0041\u0068": function(e) {
        var t = this['$_JIB'];
        if (t['map'])
            return new J(t['map'](e));
        for (var n = [], r = 0, o = t['length']; r < o; r += 1)
            n[r] = e(t[r], r, this);
        return new J(n);
    },
}

function $_BHHI(e) {
    var t = 0
        , n = 0
        , r = []
        , i = 0;
    if (e['length'] <= 0)
        return [];
    for (var a = null, s = null, c = $_BHIA(e), u = c['length'], l = u < 300 ? 0 : u - 300; l < u; l += 1) {
        var _ = c[l]
            , f = _[0];
        -1 < new J(['down', 'move', 'up', 'scroll'])['$_EGg'](f) ? (a || (a = _),
            s = _,
            r['push']([f, [_[1] - t, _[2] - n], $_BHGD(i ? _[3] - i : i)]),
            t = _[1],
            n = _[2],
            i = _[3]) : -1 < new J(['blur', 'focus', 'unload'])['$_EGg'](f) && (r['push']([f, $_BHGD(i ? _[1] - i : i)]),
            i = _[1]);
    }
    return r;
}

function $_HCb(e) {
    var f = {
        "\u006d\u006f\u0076\u0065": 0,
        "\u0064\u006f\u0077\u006e": 1,
        "\u0075\u0070": 2,
        "\u0073\u0063\u0072\u006f\u006c\u006c": 3,
        "\u0066\u006f\u0063\u0075\u0073": 4,
        "\u0062\u006c\u0075\u0072": 5,
        "\u0075\u006e\u006c\u006f\u0061\u0064": 6,
        "\u0075\u006e\u006b\u006e\u006f\u0077\u006e": 7
    };
    function p(e, t) {
        for (var n = e['toString'](2), r = '', o = n['length'] + 1; o <= t; o += 1)
            r += '0';
        return n = r + n;
    }
    function h(e) {
        var t = []
          , n = e['length']
          , r = 0;
        while (r < n) {
            var o = e[r]
              , i = 0;
            while (1) {
                if (16 <= i)
                    break;
                var a = r + i + 1;
                if (n <= a)
                    break;
                if (e[a] !== o)
                    break;
                i += 1;
            }
            r = r + 1 + i;
            var s = f[o];
            0 != i ? (t['push'](8 | s),
            t['push'](i - 1)) : t['push'](s);
        }
        for (var c = p(32768 | n, 16), u = '', l = 0, _ = t['length']; l < _; l += 1)
            u += p(t[l], 4);
        return c + u;

    }
    function u(e, t) {
        for (var n = [], r = 0, o = e['length']; r < o; r += 1)
            n['push'](t(e[r]));
        return n;
    }
    function d(e, t) {
        e = function c(e) {

            var t = 32767
              , n = (e = u(e, function(e) {

                return t < e ? t : e < -t ? -t : e;
            }))['length']
              , r = 0
              , o = [];
            while (r < n) {
                var i = 1
                  , a = e[r]
                  , s = Math['abs'](a);
                while (1) {
                    if (n <= r + i)
                        break;
                    if (e[r + i] !== a)
                        break;
                    if (127 <= s || 127 <= i)
                        break;
                    i += 1;
                }
                1 < i ? o['push']((a < 0 ? 49152 : 32768) | i << 7 | s) : o['push'](a),
                r += i;
            }
            return o;
        }(e);
        var n, r = [], o = [];

        u(e, function(e) {

            var t = Math['ceil'](function n(e, t) {

                return 0 === e ? 0 : Math['log'](e) / Math['log'](t);
            }(Math['abs'](e) + 1, 16));
            0 === t && (t = 1),
            r['push'](p(t - 1, 2)),
            o['push'](p(Math['abs'](e), 4 * t));
        });
        var i = r['join']('')
          , a = o['join']('');

        return n = t ? u(function s(e, t) {

            var n = [];
            return u(e, function(e) {

                t(e) && n['push'](e);
            }),
            n;
        }(e, function(e) {

            return 0 != e && e >> 15 != 1;
        }), function(e) {

            return e < 0 ? '1' : '0';
        })['join']('') : '',
        p(32768 | e['length'], 16) + i + a + n;
    }
    return function(e) {
        for (var t = [], n = [], r = [], o = [], i = 0, a = e['length']; i < a; i += 1) {
            var s = e[i]
              , c = s['length'];
            t['push'](s[0]),
            n['push'](2 === c ? s[1] : s[2]),
            3 === c && (r['push'](s[1][0]),
            o['push'](s[1][1]));
        }
        var u = h(t) + d(n, !1) + d(r, !0) + d(o, !0)
          , l = u['length'];
        return l % 6 != 0 && (u += p(0, 6 - l % 6)),
        function _(e) {
            for (var t = '', n = e['length'] / 6, r = 0; r < n; r += 1)
                t += '()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz~'['charAt'](parseInt(e['slice'](6 * r, 6 * (r + 1)), 2));
            return t;
        }(u);
    }(e);
}

function first_blood () {
    var e = [
        [
            "move",
            413,
            59,
            1670594942024,
            "pointermove"
        ],
        [
            "move",
            412,
            59,
            1670594942030,
            "pointermove"
        ],
        [
            "move",
            411,
            59,
            1670594942034,
            "pointermove"
        ],
        [
            "move",
            409,
            59,
            1670594942040,
            "pointermove"
        ],
        [
            "move",
            409,
            59,
            1670594942041,
            "pointermove"
        ],
        [
            "move",
            407,
            59,
            1670594942051,
            "pointermove"
        ],
        [
            "move",
            407,
            59,
            1670594942055,
            "pointermove"
        ],
        [
            "move",
            405,
            59,
            1670594942061,
            "pointermove"
        ],
        [
            "move",
            405,
            60,
            1670594942063,
            "pointermove"
        ],
        [
            "move",
            403,
            60,
            1670594942069,
            "pointermove"
        ],
        [
            "move",
            403,
            60,
            1670594942071,
            "pointermove"
        ],
        [
            "move",
            402,
            61,
            1670594942073,
            "pointermove"
        ],
        [
            "move",
            401,
            61,
            1670594942075,
            "pointermove"
        ],
        [
            "move",
            401,
            61,
            1670594942077,
            "pointermove"
        ],
        [
            "move",
            400,
            61,
            1670594942079,
            "pointermove"
        ],
        [
            "move",
            398,
            62,
            1670594942081,
            "pointermove"
        ],
        [
            "move",
            398,
            63,
            1670594942083,
            "pointermove"
        ],
        [
            "move",
            396,
            63,
            1670594942085,
            "pointermove"
        ],
        [
            "move",
            395,
            63,
            1670594942087,
            "pointermove"
        ],
        [
            "move",
            394,
            64,
            1670594942089,
            "pointermove"
        ],
        [
            "move",
            392,
            65,
            1670594942091,
            "pointermove"
        ],
        [
            "move",
            391,
            65,
            1670594942095,
            "pointermove"
        ],
        [
            "move",
            389,
            66,
            1670594942098,
            "pointermove"
        ],
        [
            "move",
            388,
            67,
            1670594942099,
            "pointermove"
        ],
        [
            "move",
            388,
            66,
            1670594942100,
            "mousemove"
        ],
        [
            "move",
            387,
            67,
            1670594942101,
            "pointermove"
        ],
        [
            "move",
            385,
            67,
            1670594942103,
            "pointermove"
        ],
        [
            "move",
            384,
            68,
            1670594942105,
            "pointermove"
        ],
        [
            "move",
            382,
            69,
            1670594942107,
            "pointermove"
        ],
        [
            "move",
            380,
            69,
            1670594942109,
            "pointermove"
        ],
        [
            "move",
            379,
            70,
            1670594942111,
            "pointermove"
        ],
        [
            "move",
            378,
            71,
            1670594942113,
            "pointermove"
        ],
        [
            "move",
            377,
            70,
            1670594942114,
            "mousemove"
        ],
        [
            "move",
            376,
            72,
            1670594942115,
            "pointermove"
        ],
        [
            "move",
            374,
            72,
            1670594942117,
            "pointermove"
        ],
        [
            "move",
            373,
            73,
            1670594942119,
            "pointermove"
        ],
        [
            "move",
            372,
            73,
            1670594942121,
            "pointermove"
        ],
        [
            "move",
            370,
            74,
            1670594942123,
            "pointermove"
        ],
        [
            "move",
            368,
            75,
            1670594942125,
            "pointermove"
        ],
        [
            "move",
            366,
            76,
            1670594942127,
            "pointermove"
        ],
        [
            "move",
            365,
            77,
            1670594942129,
            "pointermove"
        ],
        [
            "move",
            364,
            78,
            1670594942133,
            "pointermove"
        ],
        [
            "move",
            362,
            79,
            1670594942134,
            "pointermove"
        ],
        [
            "move",
            361,
            81,
            1670594942135,
            "pointermove"
        ],
        [
            "move",
            360,
            82,
            1670594942137,
            "pointermove"
        ],
        [
            "move",
            358,
            83,
            1670594942139,
            "pointermove"
        ],
        [
            "move",
            356,
            84,
            1670594942141,
            "pointermove"
        ],
        [
            "move",
            355,
            85,
            1670594942143,
            "pointermove"
        ],
        [
            "move",
            354,
            87,
            1670594942145,
            "pointermove"
        ],
        [
            "move",
            352,
            89,
            1670594942147,
            "pointermove"
        ],
        [
            "move",
            351,
            90,
            1670594942149,
            "pointermove"
        ],
        [
            "move",
            349,
            91,
            1670594942151,
            "pointermove"
        ],
        [
            "move",
            348,
            93,
            1670594942153,
            "pointermove"
        ],
        [
            "move",
            347,
            94,
            1670594942155,
            "pointermove"
        ],
        [
            "move",
            345,
            96,
            1670594942157,
            "pointermove"
        ],
        [
            "move",
            344,
            97,
            1670594942159,
            "pointermove"
        ],
        [
            "move",
            342,
            99,
            1670594942161,
            "pointermove"
        ],
        [
            "move",
            341,
            101,
            1670594942163,
            "pointermove"
        ],
        [
            "move",
            340,
            103,
            1670594942165,
            "pointermove"
        ],
        [
            "move",
            339,
            105,
            1670594942167,
            "pointermove"
        ],
        [
            "move",
            337,
            107,
            1670594942169,
            "pointermove"
        ],
        [
            "move",
            336,
            109,
            1670594942171,
            "pointermove"
        ],
        [
            "move",
            334,
            112,
            1670594942173,
            "pointermove"
        ],
        [
            "move",
            333,
            114,
            1670594942175,
            "pointermove"
        ],
        [
            "move",
            332,
            116,
            1670594942177,
            "pointermove"
        ],
        [
            "move",
            330,
            119,
            1670594942179,
            "pointermove"
        ],
        [
            "move",
            330,
            121,
            1670594942181,
            "pointermove"
        ],
        [
            "move",
            328,
            123,
            1670594942183,
            "pointermove"
        ],
        [
            "move",
            327,
            125,
            1670594942185,
            "pointermove"
        ],
        [
            "move",
            326,
            127,
            1670594942187,
            "pointermove"
        ],
        [
            "move",
            324,
            131,
            1670594942189,
            "pointermove"
        ],
        [
            "move",
            323,
            133,
            1670594942191,
            "pointermove"
        ],
        [
            "move",
            322,
            136,
            1670594942193,
            "pointermove"
        ],
        [
            "move",
            320,
            138,
            1670594942195,
            "pointermove"
        ],
        [
            "move",
            320,
            141,
            1670594942198,
            "pointermove"
        ],
        [
            "move",
            318,
            145,
            1670594942200,
            "pointermove"
        ],
        [
            "move",
            316,
            148,
            1670594942201,
            "pointermove"
        ],
        [
            "move",
            316,
            150,
            1670594942203,
            "pointermove"
        ],
        [
            "move",
            314,
            153,
            1670594942205,
            "pointermove"
        ],
        [
            "move",
            312,
            157,
            1670594942207,
            "pointermove"
        ],
        [
            "move",
            311,
            160,
            1670594942209,
            "pointermove"
        ],
        [
            "move",
            309,
            163,
            1670594942211,
            "pointermove"
        ],
        [
            "move",
            308,
            166,
            1670594942214,
            "pointermove"
        ],
        [
            "move",
            307,
            169,
            1670594942218,
            "pointermove"
        ],
        [
            "move",
            305,
            173,
            1670594942219,
            "pointermove"
        ],
        [
            "move",
            303,
            179,
            1670594942221,
            "pointermove"
        ],
        [
            "move",
            302,
            179,
            1670594942222,
            "mousemove"
        ],
        [
            "move",
            301,
            182,
            1670594942224,
            "pointermove"
        ],
        [
            "move",
            300,
            186,
            1670594942225,
            "pointermove"
        ],
        [
            "move",
            299,
            189,
            1670594942227,
            "pointermove"
        ],
        [
            "move",
            297,
            192,
            1670594942229,
            "pointermove"
        ],
        [
            "move",
            296,
            196,
            1670594942232,
            "pointermove"
        ],
        [
            "move",
            293,
            200,
            1670594942233,
            "pointermove"
        ],
        [
            "move",
            293,
            203,
            1670594942235,
            "pointermove"
        ],
        [
            "move",
            291,
            206,
            1670594942237,
            "pointermove"
        ],
        [
            "move",
            289,
            210,
            1670594942239,
            "pointermove"
        ],
        [
            "move",
            288,
            213,
            1670594942241,
            "pointermove"
        ],
        [
            "move",
            287,
            216,
            1670594942243,
            "pointermove"
        ],
        [
            "move",
            285,
            219,
            1670594942245,
            "pointermove"
        ],
        [
            "move",
            284,
            221,
            1670594942247,
            "pointermove"
        ],
        [
            "move",
            283,
            225,
            1670594942249,
            "pointermove"
        ],
        [
            "move",
            281,
            228,
            1670594942251,
            "pointermove"
        ],
        [
            "move",
            280,
            230,
            1670594942253,
            "pointermove"
        ],
        [
            "move",
            279,
            233,
            1670594942255,
            "pointermove"
        ],
        [
            "move",
            278,
            235,
            1670594942257,
            "pointermove"
        ],
        [
            "move",
            277,
            238,
            1670594942259,
            "pointermove"
        ],
        [
            "move",
            276,
            240,
            1670594942261,
            "pointermove"
        ],
        [
            "move",
            275,
            242,
            1670594942263,
            "pointermove"
        ],
        [
            "move",
            274,
            245,
            1670594942265,
            "pointermove"
        ],
        [
            "move",
            272,
            247,
            1670594942267,
            "pointermove"
        ],
        [
            "move",
            272,
            249,
            1670594942269,
            "pointermove"
        ],
        [
            "move",
            270,
            252,
            1670594942271,
            "pointermove"
        ],
        [
            "move",
            269,
            254,
            1670594942273,
            "pointermove"
        ],
        [
            "move",
            269,
            257,
            1670594942275,
            "pointermove"
        ],
        [
            "move",
            267,
            259,
            1670594942277,
            "pointermove"
        ],
        [
            "move",
            267,
            261,
            1670594942279,
            "pointermove"
        ],
        [
            "move",
            266,
            262,
            1670594942281,
            "pointermove"
        ],
        [
            "move",
            265,
            265,
            1670594942283,
            "pointermove"
        ],
        [
            "move",
            264,
            266,
            1670594942285,
            "pointermove"
        ],
        [
            "move",
            263,
            268,
            1670594942287,
            "pointermove"
        ],
        [
            "move",
            262,
            269,
            1670594942289,
            "pointermove"
        ],
        [
            "move",
            262,
            271,
            1670594942291,
            "pointermove"
        ],
        [
            "move",
            261,
            273,
            1670594942293,
            "pointermove"
        ],
        [
            "move",
            260,
            274,
            1670594942295,
            "pointermove"
        ],
        [
            "move",
            260,
            276,
            1670594942297,
            "pointermove"
        ],
        [
            "move",
            258,
            278,
            1670594942299,
            "pointermove"
        ],
        [
            "move",
            257,
            279,
            1670594942301,
            "pointermove"
        ],
        [
            "move",
            256,
            281,
            1670594942303,
            "pointermove"
        ],
        [
            "move",
            256,
            282,
            1670594942305,
            "pointermove"
        ],
        [
            "move",
            255,
            283,
            1670594942307,
            "pointermove"
        ],
        [
            "move",
            255,
            285,
            1670594942309,
            "pointermove"
        ],
        [
            "move",
            254,
            285,
            1670594942311,
            "pointermove"
        ],
        [
            "move",
            253,
            287,
            1670594942314,
            "pointermove"
        ],
        [
            "move",
            253,
            287,
            1670594942316,
            "pointermove"
        ],
        [
            "move",
            252,
            288,
            1670594942320,
            "pointermove"
        ],
        [
            "move",
            251,
            289,
            1670594942321,
            "pointermove"
        ],
        [
            "move",
            251,
            290,
            1670594942323,
            "pointermove"
        ],
        [
            "move",
            250,
            291,
            1670594942325,
            "pointermove"
        ],
        [
            "move",
            249,
            291,
            1670594942327,
            "pointermove"
        ],
        [
            "move",
            249,
            292,
            1670594942329,
            "pointermove"
        ],
        [
            "move",
            248,
            293,
            1670594942331,
            "pointermove"
        ],
        [
            "move",
            248,
            293,
            1670594942335,
            "pointermove"
        ],
        [
            "move",
            247,
            293,
            1670594942339,
            "pointermove"
        ],
        [
            "move",
            246,
            293,
            1670594942343,
            "pointermove"
        ],
        [
            "move",
            245,
            295,
            1670594942351,
            "pointermove"
        ],
        [
            "move",
            244,
            295,
            1670594942359,
            "pointermove"
        ],
        [
            "move",
            243,
            295,
            1670594942365,
            "pointermove"
        ],
        [
            "move",
            243,
            295,
            1670594942369,
            "pointermove"
        ],
        [
            "move",
            242,
            295,
            1670594942373,
            "pointermove"
        ],
        [
            "move",
            241,
            296,
            1670594942381,
            "pointermove"
        ],
        [
            "move",
            240,
            297,
            1670594942383,
            "pointermove"
        ],
        [
            "move",
            240,
            297,
            1670594942387,
            "pointermove"
        ],
        [
            "move",
            239,
            297,
            1670594942391,
            "pointermove"
        ],
        [
            "move",
            238,
            297,
            1670594942393,
            "pointermove"
        ],
        [
            "move",
            237,
            297,
            1670594942397,
            "pointermove"
        ],
        [
            "move",
            236,
            297,
            1670594942398,
            "mousemove"
        ],
        [
            "move",
            236,
            298,
            1670594942402,
            "pointermove"
        ],
        [
            "move",
            235,
            299,
            1670594942405,
            "pointermove"
        ],
        [
            "move",
            234,
            299,
            1670594942407,
            "pointermove"
        ],
        [
            "move",
            233,
            299,
            1670594942411,
            "pointermove"
        ],
        [
            "move",
            232,
            300,
            1670594942416,
            "pointermove"
        ],
        [
            "move",
            231,
            301,
            1670594942419,
            "pointermove"
        ],
        [
            "move",
            230,
            300,
            1670594942420,
            "mousemove"
        ],
        [
            "move",
            230,
            301,
            1670594942421,
            "pointermove"
        ],
        [
            "move",
            229,
            301,
            1670594942423,
            "pointermove"
        ],
        [
            "move",
            229,
            301,
            1670594942425,
            "pointermove"
        ],
        [
            "move",
            228,
            301,
            1670594942429,
            "pointermove"
        ],
        [
            "move",
            227,
            302,
            1670594942433,
            "pointermove"
        ],
        [
            "move",
            226,
            302,
            1670594942435,
            "pointermove"
        ],
        [
            "move",
            225,
            303,
            1670594942441,
            "pointermove"
        ],
        [
            "move",
            224,
            303,
            1670594942450,
            "pointermove"
        ],
        [
            "down",
            224,
            303,
            1670594942962,
            "pointerdown"
        ],
        [
            "focus",
            1670594942962
        ],
        [
            "up",
            224,
            303,
            1670594943016,
            "pointerup"
        ]
    ]; // 用户在左侧滑动的轨迹
    return $_HCb($_BHHI(e));
}

function double_kill(){
     return $_HCb([]);
}

function  $_BIGR(e) {
    return void 0 === e;
}

function triple_kill(){
    var r =  {
    "STYLE": 1,
    "SCRIPT": 5,
    "A": 1,
    "DIV": 12,
    "LABEL": 3,
    "INPUT": 2,
    "textLength": 6148,
    "HTMLLength": 7436,
    "documentMode": "CSS1Compat",
    "browserLanguage": "zh-CN",
    "browserLanguages": "zh-CN,zh,en",
    "devicePixelRatio": 2.25,
    "colorDepth": 24,
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "cookieEnabled": 1,
    "netEnabled": 1,
    "innerWidth": 433,
    "innerHeight": 849,
    "outerWidth": 1707,
    "outerHeight": 920,
    "screenWidth": 1707,
    "screenHeight": 960,
    "screenAvailWidth": 1707,
    "screenAvailHeight": 920,
    "screenLeft": 0,
    "screenTop": 0,
    "screenAvailLeft": 0,
    "screenAvailTop": 0,
    "localStorageEnabled": 1,
    "sessionStorageEnabled": 1,
    "indexedDBEnabled": 1,
    "platform": "Win32",
    "doNotTrack": 1,
    "timezone": -8,
    "canvas2DFP": "bc665dae3a1ad081f784803fc723309c",
    "canvas3DFP": 0,
    "plugins": "internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer",
    "maxTouchPoints": 0,
    "flashEnabled": -1,
    "javaEnabled": 0,
    "hardwareConcurrency": 20,
    "jsFonts": "Arial,ArialBlack,ArialNarrow,Calibri,Cambria,CambriaMath,ComicSansMS,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MicrosoftSansSerif,MSGothic,MSPGothic,MSSansSerif,MSSerif,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,SegoeUILight,SegoeUISemibold,SegoeUISymbol,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings",
    "mediaDevices": -1,
    "timestamp": new Date()['getTime'](),
    "deviceorientation": -1,
    "touchEvent": -1,
    "performanceTiming": -1,
    "internalip": -1
}
      , o = [];
    var arr = [
    "textLength",
    "HTMLLength",
    "documentMode",
    "A",
    "ARTICLE",
    "ASIDE",
    "AUDIO",
    "BASE",
    "BUTTON",
    "CANVAS",
    "CODE",
    "IFRAME",
    "IMG",
    "INPUT",
    "LABEL",
    "LINK",
    "NAV",
    "OBJECT",
    "OL",
    "PICTURE",
    "PRE",
    "SECTION",
    "SELECT",
    "SOURCE",
    "SPAN",
    "STYLE",
    "TABLE",
    "TEXTAREA",
    "VIDEO",
    "screenLeft",
    "screenTop",
    "screenAvailLeft",
    "screenAvailTop",
    "innerWidth",
    "innerHeight",
    "outerWidth",
    "outerHeight",
    "browserLanguage",
    "browserLanguages",
    "systemLanguage",
    "devicePixelRatio",
    "colorDepth",
    "userAgent",
    "cookieEnabled",
    "netEnabled",
    "screenWidth",
    "screenHeight",
    "screenAvailWidth",
    "screenAvailHeight",
    "localStorageEnabled",
    "sessionStorageEnabled",
    "indexedDBEnabled",
    "CPUClass",
    "platform",
    "doNotTrack",
    "timezone",
    "canvas2DFP",
    "canvas3DFP",
    "plugins",
    "maxTouchPoints",
    "flashEnabled",
    "javaEnabled",
    "hardwareConcurrency",
    "jsFonts",
    "timestamp",
    "performanceTiming",
    "internalip",
    "mediaDevices",
    "DIV",
    "P",
    "UL",
    "LI",
    "SCRIPT",
    "deviceorientation",
    "touchEvent"
]
    return new J(arr)['$_EAh'](function(e) { // 同上节课
        var t = r[e];
        o['push']($_BIGR(t) ? -1 : t);
    }),
    o['join']('magic data');
}

function quadra_kil(e) {
    return "SPAN_0"
}

function $_GGy(e){
    for (var t = [], n = 0, r = e['length']; n < r; n += 1)
        t['push'](e['charCodeAt'](n));
    return t;
}

function $_HBO(e, t) {
    return e >> t & 1;
}

function $_GJF(e) {
    var t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()';
    return e < 0 || e >= t['length'] ? '.' : t['charAt'](e);
}

function $_HBu(e, o){
    var i = this;
    o || (o = i);
    for (var t = function(e, t) {
        for (var n = 0, r = 24 - 1; 0 <= r; r -= 1)
            1 === $_HBO(t, r) && (n = (n << 1) + $_HBO(e, r));
        return n;
    }, n = '', r = '', a = e['length'], s = 0; s < a; s += 3) {
        var c;
        if (s + 2 < a)
            c = (e[s] << 16) + (e[s + 1] << 8) + e[s + 2],
            n += $_GJF(t(c, 7274496)) + $_GJF(t(c, 9483264)) + $_GJF(t(c, 19220)) + $_GJF(t(c, 235));
        else {
            var u = a % 3;
            2 == u ? (c = (e[s] << 16) + (e[s + 1] << 8),
            n += $_GJF(t(c, 7274496)) + $_GJF(t(c, 9483264)) + $_GJF(t(c, 19220)),
            r = '.') : 1 == u && (c = e[s] << 16,
            n += $_GJF(t(c, 7274496)) + $_GJF(t(c, 9483264)),
            r = '.' + '.');
        }
    }
    return {
        "\u0072\u0065\u0073": n,
        "\u0065\u006e\u0064": r
    };
}

function O(e) {
    var t = $_HBu($_GGy(e));
    return t['res'] + t['end'];
}

// md5
function G(e) {
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

function cul_i(gt, challenge, s, finger_print){
    var now = new Date().getTime();
    var $_CEGT = {
        "v": "9.1.1",
        "de": false,
        "te": false,
        "me": true,
        "ven": "Google Inc. (Intel)",
        "ren": "ANGLE (Intel, Intel(R) UHD Graphics 770 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "fp": [
            "move",
            413,
            59,
            now,
            "pointermove"
        ],
        "lp": [
            "up",
            224,
            303,
            now + 992,
            "pointerup"
        ],
        "em": {
            "ph": 0,
            "cp": 0,
            "ek": "11",
            "wd": 1,
            "nt": 0,
            "si": 0,
            "sc": 0
        },
        "tm": {
            "a": now - 2367,
            "b": now - 2367 + 168,
            "c": now - 2367 + 168,
            "d": 0,
            "e": 0,
            "f": now - 2367 + 168 + 167,
            "g": now - 2367 + 168 + 167 + 4,
            "h": now - 2367 + 168 + 167 + 4+ 6,
            "i": now - 2367 + 168 + 167 + 4+ 6 ,
            "j": now - 2367 + 168 + 167 + 4+ 6 + 35,
            "k": now - 2367 + 168 + 167 + 4+ 6 + 15,
            "l": now - 2367 + 168 + 167 + 4+ 6 + 35,
            "m": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16,
            "n": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2,
            "o": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12,
            "p": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3,
            "q": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3,
            "r": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3 + 18,
            "s": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3 + 18 + 65,
            "t": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3 + 18 + 65,
            "u": now - 2367 + 168 + 167 + 4+ 6 + 35 + 16 +2 + 12 + 3 + 18 + 65
        },
        "dnf": "dnf",
        "by": 0
    }
    var i = this
      , e = first_blood()
      , t = double_kill()
      , n = triple_kill()
      , r = quadra_kil()
      , o = {
            "gt": gt,
            "challenge": challenge,
            "c": [
                12,
                58,
                98,
                36,
                43,
                95,
                62,
                15,
                12
            ],
            "s": s,
        }
      , a = 270742;  // 也可以设置成随机
    var result = "";
    for (var s = [['lang', o['lang'] || 'zh-cn'], ['type', 'fullpage'], ['tt', function(e, t, n) {
        if (!t || !n)
            return e;
        var r, o = 0, i = e, a = t[0], s = t[2], c = t[4];
        while (r = n['substr'](o, 2)) {
            o += 2;
            var u = parseInt(r, 16)
              , l = String['fromCharCode'](u)
              , _ = (a * u * u + s * u + c) % e['length'];
            i = i['substr'](0, _) + l + i['substr'](_);
        }
        return i;
    }(e, o['c'], o['s']) || -1], ['light', r || -1], ['s', G(O(t))], ['h', G(O(n))], ['hh', G(n)], ['hi', G(finger_print)], ['vip_order', undefined || -1], ['ct', undefined || -1], ['ep', $_CEGT || -1], ['passtime', a || -1], ['rp', G(o['gt'] + o['challenge'] + a)]], c = 0; c < s['length']; c++)
        result += '"' + s[c][0] + '":' + JSON['stringify'](s[c][1]) + ',';
    return result
}

function encrypte1(e, t, n) { // 猜测是aes加密, CryptoJS.
    var key = t;
    var iv  = "0000000000000000";
    key = CryptoJS.enc.Utf8.parse(key);
    iv = CryptoJS.enc.Utf8.parse(iv);

    // var data = '{"gt":"019924a82c70bb123aae90d483087f94","challenge":"f3f54acc6c2de81517344f8fc25c88bd","offline":false,"new_captcha":true,"product":"popup","width":"300px","https":true,"api_server":"apiv6.geetest.com","protocol":"https://","type":"fullpage","static_servers":["static.geetest.com/","dn-staticdown.qbox.me/"],"beeline":"/static/js/beeline.1.0.1.js","voice":"/static/js/voice.1.2.2.js","click":"/static/js/click.3.0.7.js","fullpage":"/static/js/fullpage.9.1.0.js","slide":"/static/js/slide.7.8.9.js","geetest":"/static/js/geetest.6.0.9.js","aspect_radio":{"slide":103,"click":128,"voice":128,"beeline":50},"cc":20,"ww":true,"i":"6148!!7436!!CSS1Compat!!1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!2!!3!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!1!!-1!!-1!!-1!!0!!0!!0!!0!!230!!849!!1707!!920!!zh-CN!!zh-CN,zh,en!!-1!!2.25!!24!!Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36!!1!!1!!1707!!960!!1707!!920!!1!!1!!1!!-1!!Win32!!1!!-8!!bc665dae3a1ad081f784803fc723309c!!0!!internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer!!0!!-1!!0!!20!!Arial,ArialBlack,ArialNarrow,Calibri,Cambria,CambriaMath,ComicSansMS,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MicrosoftSansSerif,MSGothic,MSPGothic,MSSansSerif,MSSerif,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,SegoeUILight,SegoeUISemibold,SegoeUISymbol,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings!!1670253944185!!-1!!-1!!-1!!12!!-1!!-1!!-1!!5!!-1!!-1"}'
    var r = CryptoJS.AES.encrypt(e, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC
    });

    var o = r['ciphertext']['words'];
    var i = r['ciphertext']['sigBytes'];
    var a = [];
    for (var s = 0; s < i; s++) {
        var c = o[s >>> 2] >>> 24 - s % 4 * 8 & 255;
        a['push'](c);
    }
    return a;
}

function $_HEm(e){
    var t = $_HBu(e);
   return t['res'] + t['end'];
}

function cul_second_w(aeskey, gt, challenge, s, finger_print) { // 通过传递参数把上一次的aeskey传递过来.
    // t['push'](e['toString']());  # 2000+
    var code_one = "function o(e,t){var $_CGDFA=ujJge.$_Co,$_CGDEf=['$_CGDIi'].concat($_CGDFA),$_CGDGz=$_CGDEf[1];$_CGDEf.shift();var $_CGDHe=$_CGDEf[0];function n(e){var $_EECFI=ujJge.$_Dr()[3][19];for(;$_EECFI!==ujJge.$_Dr()[12][16];){switch($_EECFI){case ujJge.$_Dr()[12][19]:var t=5381,n=e[$_CGDGz(62)],r=0;$_EECFI=ujJge.$_Dr()[12][18];break;case ujJge.$_Dr()[0][18]:while(n--)t=(t<<5)+t+e[$_CGDFA(25)](r++);$_EECFI=ujJge.$_Dr()[9][17];break;case ujJge.$_Dr()[0][17]:return t&=~(1<<31);break;}}}100<new Date()[$_CGDGz(286)]()-t[$_CGDGz(286)]()&&(e=$_CGDGz(1402)),r=$_CGDFA(717)+i[$_CGDGz(1415)]+$_CGDGz(1435)+n(o[$_CGDFA(69)]()+n(n[$_CGDFA(69)]())+n(e[$_CGDFA(69)]()))+$_CGDFA(1434);}"
    var code_two = 'function n(e){var $_EECFI=ujJge.$_Dr()[3][19];for(;$_EECFI!==ujJge.$_Dr()[12][16];){switch($_EECFI){case ujJge.$_Dr()[12][19]:var t=5381,n=e[$_CGDGz(62)],r=0;$_EECFI=ujJge.$_Dr()[12][18];break;case ujJge.$_Dr()[0][18]:while(n--)t=(t<<5)+t+e[$_CGDFA(25)](r++);$_EECFI=ujJge.$_Dr()[9][17];break;case ujJge.$_Dr()[0][17]:return t&=~(1<<31);break;}}}'
    var code_three = 'qwe'
    var r = '';
    !function o(e, t) {
        function n(e) {
            var t = 5381
              , n = e['length']
              , r = 0;
            while (n--)
                t = (t << 5) + t + e['charCodeAt'](r++);
            return t &= ~(1 << 31);
        }
        // 100 < new Date()['getTime']() - t['getTime']() && (e = 'qwe');
        r = '{' + cul_i(gt, challenge, s, finger_print) + '"captcha_token":"' + n(code_one + n(code_two) + n(code_three)) + '"}';
    }("bbOy", new Date());
    return $_HEm(encrypte1(r, aeskey));
}
