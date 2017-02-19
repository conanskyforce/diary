
加载jQuery库
<script type="text/javascript" src=".../../jquery.js"></script>
$等价于jQuery
	
	等待动漫元素加载完毕执行JavaScript
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



















































































































































































































































































































































































































































