var CryptoJS = require("crypto-js")

var key = "bd565e12f66150c7";
var iv  = "0000000000000000";
key = CryptoJS.enc.Utf8.parse(key);
iv = CryptoJS.enc.Utf8.parse(iv);

var data = '{"gt":"019924a82c70bb123aae90d483087f94","challenge":"f3f54acc6c2de81517344f8fc25c88bd","offline":false,"new_captcha":true,"product":"popup","width":"300px","https":true,"api_server":"apiv6.geetest.com","protocol":"https://","type":"fullpage","static_servers":["static.geetest.com/","dn-staticdown.qbox.me/"],"beeline":"/static/js/beeline.1.0.1.js","voice":"/static/js/voice.1.2.2.js","click":"/static/js/click.3.0.7.js","fullpage":"/static/js/fullpage.9.1.0.js","slide":"/static/js/slide.7.8.9.js","geetest":"/static/js/geetest.6.0.9.js","aspect_radio":{"slide":103,"click":128,"voice":128,"beeline":50},"cc":20,"ww":true,"i":"6148!!7436!!CSS1Compat!!1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!2!!3!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!1!!-1!!-1!!-1!!0!!0!!0!!0!!230!!849!!1707!!920!!zh-CN!!zh-CN,zh,en!!-1!!2.25!!24!!Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36!!1!!1!!1707!!960!!1707!!920!!1!!1!!1!!-1!!Win32!!1!!-8!!bc665dae3a1ad081f784803fc723309c!!0!!internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer!!0!!-1!!0!!20!!Arial,ArialBlack,ArialNarrow,Calibri,Cambria,CambriaMath,ComicSansMS,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MicrosoftSansSerif,MSGothic,MSPGothic,MSSansSerif,MSSerif,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,SegoeUILight,SegoeUISemibold,SegoeUISymbol,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings!!1670253944185!!-1!!-1!!-1!!12!!-1!!-1!!-1!!5!!-1!!-1"}'
var r = CryptoJS.AES.encrypt(data, key, {
    iv: iv,
    mode: CryptoJS.mode.CBC
});
console.log(r.ciphertext)  // 密文


