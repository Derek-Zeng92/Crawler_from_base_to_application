
// 安装命令 npm install node-jsencrypt
const JSEncrypt = require("node-jsencrypt");

var encrypt = new JSEncrypt();
var time = new Date().getTime();

key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCN0LdLeyGeIZdUGdxFeHmAjrinbVdXgFmrj+WwxTSrY3gigY1XivP5cBw8UCMzB6/R0UCXKCx3/Wru75AMEr6Bxfk9R15OLmbo0b/W8c0rmVN0cgSsT+JzRmeBzlAPoHJwrdooLqNXx1tuApQSwvxsGJC4zS68PeGSuxKUkJY0iwIDAQAB'
encrypt.setPublicKey(key);
var pwd = "123456"
r = encrypt.encrypt(pwd);
console.log(r);