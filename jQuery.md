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
$('ul').append($('<li class="active">雪梨</li>'));//创建li节点,将其添加到ul节点中

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
$('div').replaceWith('<li>someNode</li>')
$('<li>someNode</li>').replaceAll('div')

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











































































































































































































































































































































































































