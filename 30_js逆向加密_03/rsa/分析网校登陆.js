let paramss = {
   url: '/common/getTime',  // 第一次要请求的url
}
zdAjax(paramss, function(ress){
      var param = {
        url: '/login/passwordLogin',
        data: {
          userName: username,
          password: encryptFn(pwd + '' + ress.data),
          imageCaptchaCode: imgCode,
        },
      };
      zdAjax(param, function(res){ // ajax success???
          //如果res.code是1. 那么保持cookie状态(登陆成功了????)
          //该函数你请求成功之后(处理结果的)
      })
})

// 对jquery的ajax做了再一次的封装
function zdAjax(options, fn){
  // 第一个参数就是为了凑成一个ajax需要的东西
  $.ajax({
    url: options['url'],
    data: options['data']?options['data']: {},
    success:function(r){
      fn(r)  // 调用fn
    }
  })
}


