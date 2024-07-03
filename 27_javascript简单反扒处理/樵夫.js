
var qiaofu = (function(){
    // 给数据进行加密 -> 反爬做的加密
    // AES多
    // 局部变量
    var key = "123456";
    var a = 10;

    function fn(){
        console.log("樵夫写的加密逻辑, 使用的密钥是", key);
    }
    function base64(){
        fn();
    }
    function rsa(){
        fn();
    }
    function aes(){
        fn();
    }
    return {  // 7
        "base64": base64,
        "rsa": rsa,
        "aes": aes,
        "md5": function(s){
            return "s的md5值"
        },
        "jiami": function(type){
            if(type == "md5"){
                return this.md5;
            } else {
                return function(s){
                    return "神奇的加密"+s;
                }
            }
        },
        hei: function(){
            return {
                "bai": {
                    "md5": function(){
                        return "1";
                    },
                    "rsa": {
                        "md5": function(){
                            return "88";
                        }
                    },
                    "des": function(){
                        return "3";
                    }
                },
                "lan": function(){
                    return function(){
                        return {
                            "md5":function(){return "4"}
                        },{
                            "md5":function(){return "5"}
                        }
                    }
                }
            }
        }
    };

})();

// r1 = qiaofu.jiami("md5")("123");
// console.log(r1);
// r2 = qiaofu.jiami("哈哈哈")("456");
// console.log(r2);
