#1. 初识jQuery
加载jQuery库
<script type="text/javascript" src=".../../jquery.js"></script>
$等价于jQuery
	
	等待dom元素加载完毕执行JavaScript
	$(document).ready(function(){
	//执行JavaScript
	})

与window.onload=function(){};比较

window.onload=function(){};
必须等待网页中所有内容加载完毕后才能执行
$(document).ready();
所有DOM结构绘制完毕后就可以执行

window.onload=function(){};
不能同时编写多个
$(document).ready();
能同时绑定多个

$(document).ready();
可以简化写为
$(function(){});

DOM对象，文档对象模型,文档可以被描述为文档树，每一个元素都是dom元素
DOM对象可以使用JavaScript中的方法

jQuery对象
通过jQuery包装DOM对象后产生的对象
jQuery对象可以使用jQuery里的方法

jQuery对象和DOM对象之间的相互转换
jQuery对象是个数组对象，可以通过下标访问dom对象
$('#someId')[0]
等价于
$('#someId').get(0)
将DOM对象转换为jQuery对象只需要用$()将DOM对象包装起来就行了
$(document.getElementsByTagName('head')[0]);

jQuery选择器
CSS选择器

	jQuery选择器获取的永远是对象,即使网页上没有这个元素,所以不能通过
	if($('#ff')){}
	来判断这个元素是否存在
	应该用
	if($('#ff').length>0){}

$('a + b');//紧跟在a元素后边的b元素
等价于
$('a').next();

$('a ~ b');//a之后所有的b
等价于
$('a').nextAll('b');

而$('a').siblings('b')所有a的兄弟b元素

关键就看过滤选择器了

	1. 基本过滤选择器
	:first;第一个元素
	:last;最后一个元素
	:not(selector);不为...的元素
	:even;索引值为偶数的元素(索引从0开始)
	:odd;索引值为奇数的元素(索引从0开始)
	:eq(index);等于索引值的元素(索引从0开始)
	:gt(index);大于索引值的元素(索引从0开始)
	:lt(index);小于索引值的元素(索引从0开始)
	:animated;正在执行动画的元素

	2. 内容过滤选择器
	:contains(text);含有文本text的元素
	:empty();不包含子元素或文本的空元素
	:has(selector);含有选择器的元素
	:parent;含有子元素或文本元素的元素

	3. 可见性过滤
	:hidden;选取所有不可见元素,包括type='hidden',display:none,visibility:hidden.
	:visible;选取所有可见元素

	4. 属性过滤选择器
	[src];//拥有此属性的元素
	[name="solo"];//那么属性为solo的元素
	[name!="solo"];//name属性不为solo的元素
	[src^="http://"];//src以http://开头的元素
	[src$='.jpg'];//src属性以.jpg结尾的元素
	[src*='.jpg'];//src属性含有.jpg的元素

	5. 子元素过滤器
	:nth-child(index/even/odd/eq);选取某个父元素下的第index个子元素
	:first-child;第一个子元素
	:last-child;最后一个子元素
	:only-child;父元素只有一个子元素

	6. 表单对象属性过滤器
	:enabled;
	:disabled:
	:checked;
	:selected;

表单选择器

	:input;所有input,textarea,select,button元素
	:text;当行文本框
	:password;密码框
	:radio;单选框
	:checkbox;复选框
	:submit;提交按钮
	:image;图像按钮
	:reset;重置按钮
	:button;所有按钮
	:file;上传域
	:hidden;不可见元素
***

jQuery方法
show();显示隐藏的元素
hide();隐藏元素
css(name,value);设置元素样式
text(string);设置匹配元素的文本内容
filter(expr);筛选制定表达式与匹配的元素集合
addClass(class);添加制定的类名
removeClass(class);去掉类名
is(":visible");判断元素是否可见

jQuery中的toggle

	$sthEle.click(function(){
		if($someEle.is(":visible")){
			//元素隐藏 执行1...
		}else{
			//元素显示 执行2...
		}
	});
	等价于
	$sthEle.toggle(function(){
			//元素显示  执行3..
		},function(){
			//元素显示  执行4..
	})

#2 DOM操作

1. 查找节点
元素文本节点
$('p').text();//p元素节点的文本
属性节点
$('p').attr('class');//p元素的class属性

2. 创建节点
$('ul').append($('<li class="active"\>雪梨</li\>'));//创建li节点,将其添加到ul节点中

3. 插入节点
append()元素内部追加
appendTo()互换追加顺序
prepend()元素内部前置
prependTo()互换
after()元素之后插入
insertAfter()互换
before()元素之前插入
insertBefore()互换

4. 删除节点
$('div').remove();//删除节点，但是之后还能引用
$('div').empty();//清空元素中的所有后代节点

5. 复制节点
$('div').clone();浅复制
$('div').clone(true);深复制,复制绑定事件

6. 替换节点
$('div').replaceWith('<li\>someNode</li\>')
$('<li\>someNode</li\>').replaceAll('div')

7. 包裹节点
$('div').wrap('p');//用p把div包裹起来
$('div').wrapAll('p');//用p把所有div包裹起来
$('div').wrapInner('p');//用p把div内部包裹起来

8. 属性操作
attr()获取元素属性
removeAttr()删除元素属性
jQuery中很多方法都是同一个函数获取又设置的，不加参数就是获取，加了参数就是设置
同样是这样的还有
html()
text()
height()
width()
val()
css()

9. 样式操作
$('div').attr('class');//获取div元素的class属性
$('div').attr('class','more');//设置div元素的class属性为more

追加样式
$('div').addClass('high');//追加了一个叫high的类

移除样式
$('div').removeClass('high');//移除了一个叫high的类

切换样式
$('div').toggleClass('high');//如果有high类就删除,如果没有就添加

判断是否含有某个样式
$('div').hasClass('high');//判断div是否含有high类

10. 设置、获取html、文本和值

html()方法
$('div').html();
$('div').html('xxx');

text()方法
$('div').text();
$('div').text('xxx');

val()方法
类似于JavaScript中的value属性,返回文本框,下拉列表,单选框,复选框的值(多选为包含值的数组)
val()还有一个用处,它能使select(下拉框)，checkbox(多选框)和radio(单选框)响应的选项被选中

11. 遍历节点

children()方法,获得元素所有子元素的集合
next(),获取匹配元素后边同辈元素
prev(),获取匹配元素前边紧邻元素
siblings(),获取所有同辈元素

12. CSS-DOM操作
$('p').css({'fontSize':'1.2em','backgroundColor':'whitesmoke'});
$('p').height();//获取元素的高度
与之相对的还有width()方法

$('p').offset();//获取元素的相对偏移，返回对象有top和left属性
$('p').position();//获取元素相对一最近一个position属性设置为relative或absolute的祖父节点的相对便宜
$('p').scrollTop();//滚动条距离顶部
$('p').scrollLeft();//滚动条距离左边

#jQuery中的事件与动画

1. 加载DOM与window.onload之间的差异

	- 加载内容与速度
	$(document).ready()只要DOM就绪就可以了
	而window.onload必须等到每个元素都加载完毕，包括图片视频等
	所以$(document).ready()会比window.onload快很多
	$(window).load(function(){})
	等价于
	window.onload = function(){}

	-多次使用
	window.onload只能保存对一个函数的引用
	$(document).ready()能在现有的行为上追加新的行为
	
	-简写
	$(document).ready(function(){})可以简写为$(function(){})

2. 事件绑定
bind()方法
bing(type[,data],fn);
type事件类型参数,包括
blur,focus,load,resize,scroll,unload,click,dbclick,mousedown,mouseup,mousemove,mouseover,mouseout,mouseenter,mouseleave,change,select,submit,keydown,keypress,keyup,error,也可以是自定义参数名
第二个参数传递给事件对象额外的数据对象

$('div').bind('click',function(){console.log(this)});

简写绑定事件
click,mouseover,mouseout这类事件,在程序中会经常使用到,jQuery提供了一套简写的方法.

$('div').click(function(){})
$('div').mouseover(function(){})
$('div').mouseout(function(){})

合成事件
hover()和toggle()

$('div').hover(enter,leave);
function enter(){};
function leave(){};

$('div').toggle(fn1,fn2,fn3...);
function fn1(){};
function fn2(){};
function fn3(){};

	事件对象
	$('div').bind('click',function(event){
		//do sth here.
		event.stopPropagation();//停止事件冒泡
		event.preventDefault();//阻止默认行为
		return false;//同时阻止冒泡和默认行为
	});

事件对象的属性
$('div').bind('click',function(event){//do sth});
event.type 事件类型
event.stopPropagation() 阻止冒泡
event.preventDefault() 阻止默认事件
event.target 获取到触发事件的元素
event.relatedTarget
event.pageX;//光标相对于页面的x坐标
event.pageY;//光标相对于页面的y坐标
event.which;//

移除事件

$('#btn').unbind();//移除id为btn的元素上边的所有事件
unbind()没有参数则删除所有绑定事件

$('#btn').unbind('click',myfunc);//解除绑定的myfunc的click事件

只需单击一次，立即解除绑定
one()方法

$('#btn').one('click',function(){});

模拟操作
常用模拟
$('#btn').trigger('click'[,data]);//触发click事件,以数组形式传入参数
简写为
$('#btn').click();

trigger()事件触发事件并执行默认操作.
triggerHadler()触发事件，然而取消默认事件.

##jQuery动画

show()和hide()方法
$('div').hide()
等价于
$('div').css("display":"none")

hide()方法隐藏元素之前会先记住原先display属性值,调用show()就恢复原先值

fadeIn()和fadeOut()方法
淡入和淡出

slideUp()和slideDown()方法

自定义动画方法
animate(params,speed,callback);
params为属性对象参数
speed为速度
callback为回调函数

stop();//停止当前动画
stop(true);//停止当前动画，并将动画队列清空
stop(true,true);//清空动画队列，调到当前动画的结束时刻

判断原始是否处于动画状态
is(":animated");

#jQuery表单、表格操作

表单标签组成：
1. 表单标签,服务器url与方法
2. 表单域，文本框，密码框，单选框之类
3. 表单按钮，提交，重置按钮
	
	表格获得焦点和失去焦点后背景颜色的变化
	$('input:first').focus(function(){
		$(this).css({"backgroundColor":"whitesmoke"});
	}).blur(function(){
		$(this).css({"background-color":"white"})
	});

	点击改变文本域大小
	$(":button:last").prev().click(function(){
		//$('textarea[name]').height($('textarea[name]').height()+50);
		if(!$('textarea[name]').is(':animated')){
			$('textarea[name]').animate({"height":"+=50"},400);
		}
	});
	$(":button:last").click(function(){
		//$('textarea[name]').height($('textarea[name]').height()-50);
		if(!$('textarea[name]').is(':animated')){
		 $('textarea[name]').animate({"height":"-=50"},400);
		}
	});


	表单选择
	<form id="sport" action="">
	你爱好的运动是?
		<input type="checkbox" id="checkallone">全选/全不选<br />
		<input type="checkbox" name="items" value="足球">足球
		<input type="checkbox" name="items" value="篮球">篮球
		<input type="checkbox" name="items" value="羽毛球">羽毛球
		<input type="checkbox" name="items" value="乒乓球">乒乓球<br />
		<input type="button" id="checkall" value="全选">
		<input type="button" id="checkno" value="全不选">
		<input type="button" id="checkrec" value="反选">
		<input type="button" id="send" value="提交">
	</form>
	
	所以到最后原生JavaScript还是很吊
	cka = $('input#checkall');
	ckao = $('input#checkallone');
	ckn = $('input#checkno');
	ckr = $('input#checkrec');
	sd = $('input#send');
	all = $('[name="items"]:checkbox');
	cka.click(function(){
		// all.attr('checked',true);
		// console.log($(all[0]).is(":checked"));
		all.each(function(){
			this.checked=true;
		})
	});
	ckn.click(function(){
		// all.attr('checked',false);
		// console.log($(all[0]).is(":checked"));
		all.each(function(){
			this.checked=false;
		})
	})
	// ckr.click(function(){
	// 	for(var a=0;a<all.length;a++){
	// 		if($(all[a]).is(':checked')){
	// 			$(all[a]).attr('checked',false);
	// 		}else{
	// 			$(all[a]).attr('checked',true);
	// 		}
	// 	}
	// });
	ckr.click(function(){
		all.each(function(){
			// $(this).attr('checked',!$(this).attr('checked'));
			this.checked=!this.checked;
		})
	})
	ckao.click(function(){
		all.each(function(){
			this.checked = ckao[0].checked;
		})
	})
	all.click(function(){
		var flag = true;
		all.each(function(){
			if(!this.checked){
				flag = false;
			}
		});
		ckao[0].checked=flag;
	})

end()方法返回到当前对象

	$('sele').siblings().addClass('scla').end().find(":radio").attr('checked',true);

	has()
	hasClass()
	选择器

##6.jQuery与Ajax	

部分刷新
美中不足,IE 5 之后才有XMLHttpRequest对象的,
1.ajax必须做好浏览器兼容问题
2.后退，前进按钮
3.ajax对搜索引擎支持不足，所以推广处于劣势
4.开发和调试工具的缺乏

ajax方法
	
	function ajax(){
		var res = null;
		if(window.ActiveXObject){
			res = new ActiveXObject("Microsoft.XMLHTTP");
		}else if(window.XMLHttpRequest){
			res = new XMLHttpRequest;
		}
		res.open("GET","test.php",true);
		res.onreadystatechange = function(){
			if(res.readyState == 4 ){
				if(res.status == 200){
					document.getElementById('sele').innerHTML = res.responseText;
				}
			}
		};
		res.send(null);
	}

jQuery 中的ajax
$.ajax()
$.load()
$.get()
$.post()
$.getScript()
$.getJSON()

1. load()获取静态数据文件
远程载入html代码并插入dom中
a.load('b.html .para');//b中类为para的内容添加到a中

2. get()和post()传递一些参数给服务器中的页面
	$('sele').click(function(){
		$.get('get1.php',{xx:xxx},function(data,status){
				//data为返回内容,可以是xml文档,json文件,html片段等
				//status为请求状态success,error,notmodified,timeut 4 种
			})	
	
	})

get将参数跟在url后边
post作为消息实体传送参数
get传输大小限制
post大得多,理论上没有限制
get请求到的数据会被浏览器缓存
post不会

3. getScript()与getJSON()
jQuery动态的添加jquery
$(document.createElement('script')).attr('src','https://cdn.bootcss.com/jquery/3.1.1/jquery.min.js').appendTo('head');

原生动态添加jQuery
var scr = document.createElement('script');
scr.setAttribute('src','https://cdn.bootcss.com/jquery/3.1.1/jquery.min.js');
var head = document.getElementsByTagName('head')[0];
head.appendChild(scr);


$.getScript('test.js');//加载js文件

$.getJSON('test.json');//加载JSON文件

4. ajax()方法

	$.ajax({
		type:"GET",
		url:'test.json',
		dataType:"json",
		timeout:1000,
		success:function(data){
			console.log(data.username);
		},
		complete:fucntion(){
			console.log(this);
		},
		error:function(){
			console.log(this);
		}
	})

序列化元素
serialize()方法，将DOM元素内容序列化为字符串
$('form').serialize()
serializeArray()，将DOM元素序列化后,返回JSON格式数据
param()方法,将数组或对象按照键/值对进行序列化

ajax全局事件
当ajax请求开始时，会触发ajaxStart方法，ajax请求结束会触发ajaxStop()方法值得注意的是这是个全局方法，即无论何处之哟啊哦有ajax请求发生时候就会触发他们
(可以设置加载时候的动画，这可以极大的改善用户的体验)
在$.ajax(options)中将global设置为false则不触发全局ajax事件

❑a && b&& c&&d：返回第一个可转换为false的元素值。
❑a||b||c||d：返回第一个可转换为true的元素值。

























































































































































































































































































































































