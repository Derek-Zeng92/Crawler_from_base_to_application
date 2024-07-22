var {RSAKey} = require("node-jsencrypt")
var CryptoJS = require("crypto-js");

var quanjv = {
    $_EJt:{
        "offline": false,
        "new_captcha": true,
        "product": "popup",
        "width": "300px",
        "https": true,
        "api_server": "apiv6.geetest.com",
        "protocol": "https://",
        "type": "fullpage",
        "static_servers": [
            "static.geetest.com/",
            "dn-staticdown.qbox.me/"
        ],
        "beeline": "/static/js/beeline.1.0.1.js",
        "voice": "/static/js/voice.1.2.2.js",
        "click": "/static/js/click.3.0.7.js",
        "fullpage": "/static/js/fullpage.9.1.0.js",
        "slide": "/static/js/slide.7.8.9.js",
        "geetest": "/static/js/geetest.6.0.9.js",
        "aspect_radio": {
            "slide": 103,
            "click": 128,
            "voice": 128,
            "beeline": 50
        }
    },
    $_EIf:{}
}

function cul_first_w(gt, challenge){
    var t = quanjv;
    t['$_EJt']['gt'] = gt;
    t['$_EJt']['challenge'] = challenge;
    var e = $_BIB_(); // 拿到了一个很像浏览器指纹的一个大字符串(预期)

    t['$_EJt']['cc'] = 20,
    t['$_EJt']['ww'] = true,
    t['$_EJt']['i'] = e; // JSON.stringify({}) => ""
    var r = $_CCHs()  // 这一步完事儿了 -> 生成一个aeskey. 然后用rsa进行加密
      , o = encrypte1(JSON['stringify'](t['$_EJt']), $_CCIT())   // encrypt(带有指纹相关信息的字符串, aeskey)
      , i = $_HEm(o)
      , s = {
        "\u0067\u0074": t['$_EJt']['gt'],
        "\u0063\u0068\u0061\u006c\u006c\u0065\u006e\u0067\u0065": t['$_EJt']['challenge'],
        "\u006c\u0061\u006e\u0067": "zh-cn",
        "\u0070\u0074": 0,
        "\u0063\u006c\u0069\u0065\u006e\u0074\u005f\u0074\u0079\u0070\u0065": 'web',
        "\u0077": i + r
    };
    return {
        "msg": s,
        "aeskey": $_CCIT(),
        "finger_print": e
    };
}

function $_HEm(e){
    var t = $_HCX(e);
   return t['res'] + t['end'];
}

function $_HCX(e, o){
    var i = this;
    o || (o = i);
    for (var t = function(e, t) {
        for (var n = 0, r = 24 - 1; 0 <= r; r -= 1)
            1 === $_HBO(t, r) && (n = (n << 1) + $_HBO(e, r));
        return n;
    }, n = '', r = '', s = e['length'], a = 0; a < s; a += 3) {
        var c;
        if (a + 2 < s)
            c = (e[a] << 16) + (e[a + 1] << 8) + e[a + 2],
            n += $_GJF(t(c, 7274496)) + $_GJF(t(c, 9483264)) + $_GJF(t(c, 19220)) + $_GJF(t(c, 235));
        else {
            var _ = s % 3;
            2 == _ ? (c = (e[a] << 16) + (e[a + 1] << 8),
            n += $_GJF(t(c, 7274496)) + $_GJF(t(c, 9483264)) + $_GJF(t(c, 19220)),
            r = '.') : 1 == _ && (c = e[a] << 16,
            n += $_GJF(t(c, 7274496)) + $_GJF(t(c, 9483264)),
            r = '.' + '.');
        }
    }
    return {
        "\u0072\u0065\u0073": n,
        "\u0065\u006e\u0064": r
    };

}

function $_HBO(e, t) {
    return e >> t & 1;
}

function $_GJF(e) {
    var t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()';
    return e < 0 || e >= t['length'] ? '.' : t['charAt'](e);
}

function encrypte1(e, t, n) { // 猜测是aes加密, CryptoJS.
    // t = _['parse'](t); // CryptoJS.enc.utf8.parse(t)
    // iv = _['parse']('0000000000000000'); // CryptoJS.enc.utf8.parse('0000000000000000')
    //
    // // n && n['iv'] || ((n = n || {})['iv'] = _['parse']('0000000000000000'));
    // var r = m['encrypt'](u, 数据, key, iv); // m  CryptoJS.AES.encrypt
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

function $_CCHs(e){
    // 你可以选择用python去做. 别抠代码...
    // 你知道它用的rsa. 并且. 你知道它用的是JSEncrypt  但是. JSEncrypt没有给两个数字的功能
    var rsa = new RSAKey(); // 如果你受不了这个方案. 你可以选择使用python来完成该算法
    rsa.setPublic('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
    var t = rsa['encrypt']($_CCIT(e)); // 对aeskey进行加密
    while (!t || 256 !== t['length'])
        t = rsa['encrypt']($_CCIT(!0));
    return t;
}

function X(){
    this['n'] = null,
    this['e'] = 0,
    this['d'] = null,
    this['p'] = null,
    this['q'] = null,
    this['dmp1'] = null,
    this['dmq1'] = null,
    this['coeff'] = null;
    this['setPublic']('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
}




function $_CCIT(e){
    return quanjv['$_EIf']['aeskey'] && !e || (quanjv['$_EIf']['aeskey'] = te()),
    quanjv['$_EIf']['aeskey']; // 返回aeskey
}

function te(){
    return e() + e() + e() + e();
}

function e(){
    return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
}

function $_BIB_() {
    // var n = this;
    var r = {
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
    "innerWidth": 180,
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
    "timestamp": 1670247241171,
    "deviceorientation": -1,
    "touchEvent": -1,
    "performanceTiming": -1,
    "internalip": -1
};
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
];
    r['timestamp'] = new Date()['getTime'](),
    r['deviceorientation'] = -1,
    r['touchEvent'] = -1,
    r['performanceTiming'] = -1,
    r['internalip'] = -1;
    var o = [];
    return new ce(arr)['$_EAC'](function(e) {
        var t = r[e];
        o['push']((void 0 === t) ? -1 : t);
    }),
    o['join']('!!');
}

function ce(e) {
    this['$_BAEB'] = e || [];
}

ce['prototype'] = {
    "\u0024\u005f\u0045\u0041\u0043": function(e) {
        var t = this['$_BAEB'];
        if (t['map'])
            return new ce(t['map'](e));
        for (var n = [], r = 0, o = t['length']; r < o; r += 1)
            n[r] = e(t[r], r, this);
        return new ce(n);
    }
};

// console.log(cul_first_w("019924a82c70bb123aae90d483087f94", "1a8b07125f63e70c4ca40a508ccea183"))