var window = global; // node的全局 ->  浏览器里面的window;

function o(n) {
    // t = "",
    // ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function(n) {
    //     t += window['unescape']("%u00" + n)
    // });
    // // 上面这一坨运行完. t里面是fromCharCode
    // var t, e = t;
    return String['fromCharCode'](n)
}


function cv(t) {
    t = window['encodeURIComponent'](t)["replace"](/%([0-9A-F]{2})/g, function(n, t) {
        return o("0x" + t) // 把百分号. 换成了0x
    });
    try {
        // base64, 浏览器自带的btoa功能
        return window.btoa(t)
    } catch (n) {
        // base64, nodejs的base64

        return window['Buffer']["from"](t)["toString"]("base64");
    }
}

function oZ(n, t) {
    // t = t || u();
    for (var e = (n = n["split"](""))['length'], r = t['length'], a = 'charCodeAt', i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n["join"]("");

}



// 规定:
// { url: "完整的url", }
//
function get_mm(url, params){
    // 加一点我自己的代码. 处理成它需要的那个样子
    // 分离出. baseurl, url
    // 借助URL的功能.
    var t = {};
    var u = new URL(url);
    t['baseURL'] = u['origin']; // t里面就有的baseURL了
    t['url'] = url
    t['params'] = params

    s = -1228;
    var e, r = +new Date - (s || 0) - 1661224081041, a = [];

    // void 0 === t[Zt] && (t[Zt] = {})
    if (void 0 === t['params']){
        t['params'] = {}
    }

    return  Object['keys'](t["params"])["forEach"](function(n) {
        if (n == "analysis")
            return false;
        t['params']['hasOwnProperty'](n) && a['push'](t['params'][n])
    }),// 把params里面的所有的值. 组装到a列表


    a = a['sort']()["join"](""), // 排序. 拼接 结果就是一个字符串. 装着所有的数据

    a = cv(a), // 计算了一个base64, "MjIwMjItMTItMDIzNmFsbGNuaXBob25l@#/xxxx/xxxx@#时间@#3"

    a = (a += "@#" + t["url"]["replace"](t["baseURL"], "")) + ("@#" + r) + ("@#" + 3),

    e = cv(oZ(a, "xyz517cda96abcd")),
    -1 == t["url"]["indexOf"]("analysis") && (t["url"] += (-1 != t["url"]["indexOf"]("?") ? "&" : "?") + "analysis" + "=" + window["encodeURIComponent"](e)),
    t.url;
}

// console.log(get_mm({"url": "https://api.qimai.cn/rank/indexPlus/brand_id/2", params:{
//     "brand": "all",
//     "country": "cn",
//     "device": "iphone",
//     "genre": "36",
//     "date": "2022-12-02",
//     "page": 2
// }}))


function p(n, t) {
        for (var e = (n = n["split"](""))['length'], r = t['length'], a = 'charCodeAt', i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i) % r][a](0));
    return n["join"]("");

    }

function get_qm_check() {
    var n = {
        "gpu": "ANGLE (Intel, Intel(R) UHD Graphics 770 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "check": "0,0,0,0,0"
    }

    return cv(p(JSON.stringify(n), 'xyz57209048abcd'))
}

console.log(get_qm_check())