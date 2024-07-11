e是一坨乱遭的东西
1 == (
    e = "{" == e[0] ? JSON.parse(e) : JSON.parse(webInstace.shell(e))
).Status || 200 == e.Code ? r(e.Data) : 200 == e.code ? r(e.data) : a(e.Msg)

if("{" == e[0]){
    e = JSON.parse(e)
} else{
    e =JSON.parse(webInstace.shell(e))
}

e.Status == 1

e => 解密  => json.parse()

