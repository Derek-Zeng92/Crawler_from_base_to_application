$(function(){$widthwindow = $(window).width();if($widthwindow < 750){	$(".list-charts li").width($widthwindow-60);$("#_17mb_ph .author,#_17mb_ph .lastchapter,#_17mb_ph .visit,#_17mb_ph .fullflag").hide(300);$("#_17mb_ph .articlename").width("70%");$("#_17mb_ph .lastupdate").width("30%");$("#bookcon .lastchapter,#booklast").hide(300);	$(".navbar-nav li").css({"display":"block","float":"left"});$(".myinfo,.bookcase").width("50%").height(60);	$("#navbar .bookcase").css("top","0px");$(".dropdown-menu a").css("color","#fff");$("#llastupdate tbody tr:gt(10)").hide(0);}})
var _mobile;
UA = navigator.userAgent.toLowerCase();
url = window.location;
url = url.toString();
if((UA.indexOf('iphone') != -1 || UA.indexOf('mobile') != -1 || UA.indexOf('android') != -1 || UA.indexOf('ipad') != -1 || UA.indexOf('windows ce') != -1 || UA.indexOf('ipod') != -1) && UA.indexOf('ipod') == -1) {
	_mobile = 1 ;$(function(){$("#gundong").hide()});
}
else{
	_mobile = null ;
}

//ͳ�ƴ���,PC+WAP
function _17mb_tj(){}
//������棨PC��
function _17mb_pctop(){
	if(!_mobile)
	document.write("<!--������дPC����������-->");
}
//�в���棨PC��
function _17mb_pcmiddle(){
	if(!_mobile)
	document.write("<!--������дPC�в�������-->");
}
//�ײ���棨PC��
function _17mb_pcbottom(){
	if(!_mobile)
	document.write("<!--������дPC�ײ�������-->");
}
//�������(PC)
function _17mb_pcduilian(){
	if(!_mobile)
	document.write("<!--������дPC�������-->");
}
//PC�½�ҳ���ι��1
function _17mb_chapter1(){
	if(!_mobile)
	document.write("<!--������дPC�½�ҳ���ι��1-->");
}
//PC�½�ҳ���ι��2
function _17mb_chapter2(){
	if(!_mobile)
	document.write("<!--������дPC�½�ҳ���ι��2-->");
}
//PC�½�ҳ���ι��3
function _17mb_chapter3(){
	if(!_mobile)
	document.write("<!--������дPC�½�ҳ���ι��3-->");
}
//������棨WAP��
function _17mb_waptop(){
	if(_mobile)
	document.write("<!--������дWAP����������-->");
}
//�в���棨WAP��
function _17mb_wapmiddle(){
	if(_mobile)
	document.write("<!--������дWAP�в�������-->");
}
//�ײ���棨WAP��
function _17mb_wapbottom(){
	if(_mobile)
	document.writeln("");
}
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?ba187bdcb4cc97d2cdba3789bd52488d";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();

var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?d78fc86b6a707e2ec20bacb216c0eb62";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();