var JSEncrypt = require("jsencrypt")

// const {JSEncrypt} = jsencrypt;  // 是否需要拆包. 忘记了. 下节课告诉你

var publickeystr = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDhNhuAr4UjFv+cj99PbAQWWx9H \
X+3jSRThJqJdXkWUMFMTRay8EYRtPFIiwiOUU4gCh4ePMxiuZJWUBHe1waOkXEFc \
Kg17luhVqECsO+EOLhxa3yHoXA5HcSKlG85hNV3G4uQCr+C8SOE0vCGTnMdnEGmU \
nG1AGGe44YKy6XR4VwIDAQAB";

var a = new JSEncrypt();
a.setPublicKey(publickeystr);

var func = function(txt) {
    var nestr = a.encrypt(txt);
    return nestr;
}
console.log(func("123"))



