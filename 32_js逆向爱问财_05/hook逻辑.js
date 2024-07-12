

//  hook cookie
var v = "";
Object.defineProperty(document, "cookie", {
    set: function(val){ // 在对 document.cookie = xxxx
        debugger; // 断点
        v = val;
        return v;
    },
    get(){ // 在使用document.cookie
        return v;
    }
})

// 934行. 加密的入口....

// 1. 是个属性. 2. document.cookie始终在变化。
//  直接丢到浏览器的console里面去.

// 每次运行都是不一样的hexin-v

// 为了看到更多的东西. 我选择在整个页面中加载js的第一句话进行hook
var set_headers = window.XMLHttpRequest.prototype.setRequestHeader;
window.XMLHttpRequest.prototype.setRequestHeader = function(name, value){
    if(name.indexOf('hexin-v')!=-1){
        debugger;
    }
    return set_headers(name, value);
}

// var eval_ = window.eval;
// window.eval = function(s){
//
//     debugger;
//     return eval_.apply(this, arguments); // call, apply 999
// }

// 有值是 True， 没值是False
var a = 10086;
console.log(a && (a = 3));// 如果a有值。 就返回a， 如果a没值，就运行a=3
console.log(a)
