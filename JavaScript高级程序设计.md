所有的值都将是这6种类型：
string，number，null，boolean，undefined和Object
***
一般我们说的类型：
string,number,null,undefined，boolean，array，Object，function
***
typeof 的结果：值得一提的是null结果也是Object，这实际是是设计者最初的一个失误，但现在修复也已经是不可能的了。无中生有的null
string,number,boolean,undefined,object
console.log(typeof(undefined))------undefined
console.log(typeof(123))------number
console.log(typeof('134'))------string
console.log(typeof([]))------object
console.log(typeof({}))------object
console.log(typeof(function(){}))------function
console.log(typeof(true))------boolean
console.log(typeof(null))-----object
console.log(typeof(/^dG$/))-----object
null不能和Object区分哦!
还有NaN只能通过isNaN(NaN),NaN和它自己都不相等,对于未申明的变量执行typeof也返回undefined哦!
任何操作数与NaN进行比较，结果都是false
NaN==NaN//false
NaN!=Nan//true
如果定义的变量在将来准备用于保存对象，最好将对象初始化为null，用于空对象指针。
undefined派生自null
所以undefined==null//返回true

对于任何数据类型都能够调用Boolean()函数，结果总是返回一个Boolean值。

isFinite(Number.MAX_VALUE*2)判断最大值的2倍是否有穷，显然不是。

数值转换
Number()可以将任何数据类型转换为数值
Number(undefined)返回NaN
Number(null)返回0
Number("")返回0
parseInt()用于将字符串转换为数值
parseInt('')返回NaN，能够识别八进制，删除多余字符串
parseInt('',16)转换成1进制
parseFloat()用于将字符串转换为数值

数值，布尔值，对象，字符串值都有toString()方法
但是null和undefined没有这个方法。

String()能够对任何值进行字符串转换
null返回'null'
undefined返回'undefined'

Object的每个实例都具有下列属性和方法
1.constructor:创建当前对象的函数
2.hasOwnProperty():检查自身有没有某个属性(不包括从原型继承的属性)
3.isPrototypeOf():是否对象的原型
4.propertyIsEnumerable():孰能能否用for-in语句枚举
5.toLocalString():
6.toString():返回对象的字符串表示
7.valueOf():返回对象的字符串，数值，或布尔值表示

switch语句在比较时使用的是全等操作符，因此不会发生类型转换

函数接受参数是有arguments类数组来完成的，arguments具有arguments[0]访问法，length属性。arguments对象中的值会自动反应到对应的命名参数。
arguments[1]=10，函数每次都将把第二个参数设置为10

##变量、作用域和内存问题
4.1基本类型和引用类型
基本类型：undefined，null，Boolean，Number，string
引用类型：对象

instanceof 补充 typeof
person instanceof Object//person是Object吗
colors instanceof Array//colors是Array吗
pattern instanceof RegExp//pattern是RegExp吗

所有引用类型都是Object的实例，所以
instanceof能够区分null和Object，判断它是哪一种引用类型
Array.isArray()能够判断是不是数组

if和for循环中定义的变量没有块级作用域
访问局部变量比访问全局变量要快，不用沿着作用链一直向上找，节省时间

###第五章，引用类型P102

对象是某个特定引用类型的实例
5.1Object对象
创建Object实例的方式有两种：
1.var person = new Obeject();
person.name = "conan";
person.age = 25

2.对象字面量的属性名会自动转换为字符串
var person = {
	name:"conan",
	age:25
};

5.2Array 数组
1.var colors = new Array()

2.var colors = [1,2,'',true,undefined]

Array.isArray(arr)判断arr是不是数组
它也有toString()方法
arr.join(""),以不同的分隔符来构建这个字符串
不给join传递参数，或传入undefined，则默认用逗号作为分隔符
null，undefined，在join(),toLocalStrin(),toString(),valueOf()返回空字符串

push(),pop()方法，从数组末尾添加，删除元素
unshift()，shift()方法，从数组头部添加，删除元素

reverse(),sort()方法进排序
arr.sort(function(x,y){return x-y})

concat()拼接数组
arr1.concat(arr2,123)

slice()切片
arr.slice()//数组复制
arr.slice(1,3)//s索引1到索引3不包括3

splice(a,c,b,d)//从a出删除c项，增加b和d

arr.indexOf('a')//'a'在数组arr中的索引

迭代方法：
every()//每一项都true，返回true
filter()//返回返回true的项目组成的数组
forEach()//对数组每一项运行函数
map()//map()嘛，映射
some()//有一项返回true结果就是true
reduce()和reduceRight()//从左和从右开始。
***
看某个程序执行所耗费时间
var start = Date.now();
console.log('asd');
var stop = Date.now();
result = stop - start;
<====>
var start = new Date();
console.log('asd');
var stop = new Date();
result = stop - start;

var start = new Date();
console.log('asd');
var stop = new Date();
result = stop - start;
console.log(start.valueOf())
console.log(stop.valueOf())
***

使用不带圆括号的函数名是访问函数指针，而不是调用函数

函数申明会被变量提升(hoist)
函数申明放在前边

this、arguments、callee
arguments用来保存实际参数
arguments的callee属性是一个指针， 指向拥有这个arguments对象的函数!
function abc(){
	return arguments.callee//返回函数名
	//<==>等价于return abc
	}

阶乘递归函数:
function factorial(num){
	if(num<=1){
	return 1;
}	else{
	return num*arguments.callee(num-1);
}
}
n=factorial
n(5)//120

this引用的是函数以执行的环境对象

函数的属性和方法
每个函数都包含两个属性，length和prototype
length表示函数希望接受的命名参数的个数，

每个函数都包含两个方法：apply()和call()，用于设置函数this的指向。apply()接受两个参数，第一个是(其中运行函数的作用域)this，第二个是参数数组，也可以是arguments。
.apply(this,arguments|[])//数组
.call(this,num1,num2)//逐条列举

bind()方法，创建一个函数的实例，其this值会被绑定到传给bind()函数的值。

函数的toLocalString(),toString(),valueOf()方法都返回函数代码

charAt()和charCodeAt()
索引位置字符串，索引位置字符串编码

var str= 'Hello ,My friends';
var charat = '';
var charcodeat="";
for(var i=0;i<str.length;i++){
	charat+=str.charAt(i);
	charcodeat+=str.charCodeAt(i)+',';
}
console.log(charat)//Hello ,My friends
console.log(charcodeat)//72,101,108,108,111,32,44,77,121,32,102,114,105,101,110,100,115,
charCodeAt()//对应索引值的字符编码
<===>
fromCharCode()//字符编码转为字符串
String.fromCharCode(72,101,108,108,111,32,44,77,121,32,102,114,105,101,110,100,115)

字符串操作方法：

slice()
substr()//第二个参数是返回参数的个数
substring()

搜索指定字符串的位置，没找到返回-1
indexOf()
lastIndexOf()

字符串的match()方法，本子上与exec()相同，返回的是数组，数组第一项是与整个模式匹配的字符串，之后的每一项是捕获组匹配的字符串。

字符串的search()方法，返回字符串中第一个匹配项的索引，没有找到则返回-1。

字符串的replace()方法

string.replace(/[\/\\\*]*/g,"ABC")//将字符串中\,*替换为ABC

split()指定分隔符将字符串分割成子字符串并放在数组之中。

URI编码方法

encodeURI()方法对整个URI编码
encodeURIComponent()对后边一段进行编码，主目录下的URI，对所有非标准字符都进行编码。特别是查询字符串参数，post的信息等等

对应方法：
decodeURI()//只能解码encodeURI部分
decodeURIComponent()//解码任何特殊编码

eval()里边的脚本会被执行，是种非常危险的方法。

我需要(a,b)之间的任意(整数)数值

Math.floor(Math.random()*(b-a)+a)

P157

第六章、面向对象的程序设计

1.数据属性
var person = {};
Object.defineProperty(person,"name",{
	writable:false,
	value:"conan",
	enumerable:false,
	configurable:false
});
alert(person.name);//"conan"
2.访问器属性
var book = {
	name : "conan biography",
	num : 2
};
Object.defineProperty(book,'choose',{
	get:function(){
	return "you choose "+this.name;
	},
	set:function(val){
	this.num = val;
	}
})
book.choose//you choose conan biography
book.choose = 'find me lady'
book.num //'find me lady'


var book= {};
Object.defineProperties(book,{
	_year:{
		value:2016
	},
	edition:{
		value:"v1.0"
	},
	year:{
		get:function(){
			return Date.now()
		},
		set:function(newv){
			if(newv==2016){
				this.editon="v1.0";
			}else if(newv>2016){
				this.edition="v1.1";
			}else{
				this.edition="v0.9";
			}
		}
	}
})

###工厂模式
function createPerson(name,age,job){
	var o = new Obejct();
	o.name = name;
	o.age =age;
	o.job =job;
	o.sayName = function(){
		console.log("hello "+this.name);
	};
	return o;
}
var p1 = createPerson("conan",24,"PE");
var p2 = createPerson("steve",32,"PM");
构造函数：
function Person(name,age,job){
	this.name = name;
	this.age = age;
	this.job = job;
	this.sayName =function(){
	console.log("hello "+this.name);
	}
}
var p1 = new Person("jobs",32,"PW");
var p2 = new Person('kelly',22,"SG");
p1.constructor == Person
p2.constructor == Person
p1 instanceof Person//true
p1 instanceof Object//true
Person instanceof Object//true

构造函数的prototype属性指向一个对象，也就是通过调用构造函数而创建的那个实例对象的原型对象。

所有原型对象都会自动获得一个constructoer属性，这个属性包含一个自称prototype属性所在函数的指针。
function Person(){
}
Person.prototype.constructor == Person

每个构造函数创建的实例，都有一个属性__proto__指向构造函数的原型对象

Person//构造函数
prototype//构造函数有这么个属性
Person.prototype//这个属性也是一个对象，叫原型对象
constructor//原型对象有这么个属性
Person.prototype.constructor//原型对象的这么个属性指向构造函数本身

a.isPrototypeOf(b)//a是b上边的原型
Person.protype.isPrototypeOf(person1);//

Object.getPrototypeOf(a)//取得a对象的原型
Object.getPrototypeOf(person1);//Person.prototype;

hasOwnProperty()//检测一个属性是否只存在于对象实例中

in操作符，原型上如果有这个属性也会返回true

返回原型中的属性
function hasPrototypeProperty(object,name){
	return !object.hasPrototypeProperty(name)&&(name in object)
}

取得对象上所有可以枚举的实例属性，可以使用Object.keys()方法。

Object.getOwnpropertyNames()//得到所有实例属性，不论他是否可枚举。

组合使用构造函数模式和原型模式
function Person(name,age,job){
	this.name=name;
	this.job=job;
	this.age=age;
	this.friends = ["conan","steve","bill"]
};
Person.prototype = {
	constructor:Person,
	sayName:function(){
		console.log(this.name);
	}
};
var p1 = new Person();
var p2 = new Person();
p1.friends.push("elong");
p1.friends//["conan","steve","bill","elong"]
p2.friends//["conan","steve","bill"]
p1.friends==p2.friends//false
上边这个例子当中，实例属性都是花在构造函数中定义的，而由实例
共享的属性constructor和方法则是在原型中定义的。

每个构造函数都有一个原型对象，原型对象都包含一个指向构造函数的指针，实例都包含一个指向原型对象的内部指针。

确定原型和实例之间的关系
a instanceof b//a是b的原型
a.prototype.isPrototypeOf(b)//a.prototype是b的原型对象

###函数表达式

var myfunc=function(){
	//do something here.
}

严格模式下仍然行得通哦
var factorial = (function f(num){
	if(num<=1){
		return 1;
	}else{
		return num*f(num-1);
	}
});
b=factorial;
factorial=null;
b(4)//仍然有效

**闭包**

匿名函数可以用来模仿块级作用域
(function () {
	// block intervene area...
})();
创建一个函数，并立即执行
(function(){
	var now = new Date();
	if(now.getMonth()==0&&now.getDate()==1){
		alert("元旦快乐!");
	}
})();
这种思路牛逼啊，像定时炸弹一样。

特权方法：能够访问私有变量和私有函数的公有方法!

##第八章 BOM

BOM和核心是window，它表示浏览器的一个实例。
####全局作用域
在全局作用域中申明的变量，函数都会成为window对象的属性和方法。
在chrome中都支持
浏览器距离屏幕左上角左边距离
window.screenLeft
window.screenX
浏览器距离屏幕左上角上边距离
window.screenTop
window.screenY

//被禁用
window.moveTo(0,0)//移到左上角
window.moveTo(200,300)//移到左上角对准屏幕的200,300点
window.moveBy(0,100)//向下移动100
window.moveBy(-100,0)//像左移动100

window.innerWidth//可视区域宽
window.outerWidth//浏览器宽
window.innerHeight//可视区域高
window.outerHeight//浏览器高

页面视口的大小
document.body.clientWidth||document.documentElement.clientWidth;
document.body.clientHeight||document.documentElement.clientWHeight;

window.open("http://www.baidu.com","_blank","height=400,width=400,top=10,left=10,menubar=no")

if(confirm("are u sure?")){
	//confirm 为 yes 才执行本段
}

var result = prompt("What's ur name?","");
if(result!=null){
	alert("hello"+result);
}
解析查询端字符串，返回一个参数对象
(function getquerystring(){
	var qs=(location.search.length>0?location.search.substring(1):''),
	args={},
	items = qs.length?qs.split("&"):[],
	item =null,
	name = null,
	value = null,
	i=0,
	len=items.length;
	for(i=0;i<len;i++){
		item = items[i].split("=");
		name = decodeURIComponent(item[0]);
		value = decodeURIComponent(item[1]);
		if(name.length){
			args[name] = value;
		}
	}
	return args;
})();

##客户端检测

##第十章DOM
p266

每个节点都有一个childNodes属性，保存着一个NodeList对象
var firstChild=someNode.childNodes[0]
var secondChild=someNode.childNodes.item(1)//someNode.childNodes[1];
var count=someNode.childNodes.length;
someNode.firstChild=someNode.childNodes[0]
someNode.lastChild=someNode.childNodes[someNode.childNodes.length-1]
关于特性:
a.getAttribute("mydefine")//可以获得自定义特性
a.mydefine//这个却不一定能用哦，IE居然能用!
所以开发过程中一般只使用对象的属性，只有在取得自定义特性值的前提下，才回去用getAttribute()方法
a.setAttribute('href','http://www.conanskyforce.github.io')//
a.id="asdv",a.href="xxx"//特性(原生就有的)可以直接赋值
removeAttribute()//

var div=document.createElement('div')
var div=document.createElement('<div id="myid" class="myclass"></div>')
div.id="mydiv"
div.className="myclass"
document.body.appendChild(div)

元素的所有子节点，IE会忽略ul中li之间的空白，其他浏览器会将其当做文本节点
for(var i=0;i<element.childNodes.length;i++){
	if(element.childNodes[i].nodeType==1){
		//do sth here
	}
}
Text类型
nodeType为3
nodeName为#Text类型
nodeValue为文本包含的值
var txt=document.createTextNode('<em>emphasize</em>');
var div=document.createElement('div');
div.appendChild(txt);
document.body.appendChild(div);

包含一个以上文本节点的父元素使用normalize()方法，将文本节点合一，拼接起来

var attr=document.createAttribute('href')//创建新的特性节点
attr.value='http://baidu.com';
element.setAttributeNode(attr);

####动态脚本
加载名为123.js的js脚本
function loadscript(url){
	var script=document.createElement('script');
	script.src=url;
	script.type="text/javascript";
	document.body.appendChild(script);
}
loadscript(url);
亦或:
function loadscript(url){
	var script=document.createElement('script');
	var sccontent= document.createTextNode("function myfunc(url){alert(\"Hello!\"+url)}");
	//或者 script.text='function myfunc(){alert("Hello")';
	script.type="text/javascript";
	script.appendChild(sccontent);
	document.body.appendChild(script);
}
loadscript(url);

####动态样式
创建并加载123.css(link方式)
function loadStyles(css){
	var link=document.createElement('link');
	link.rel="stylesheet";
	link.type="style/css";
	link.href=css;
	var head = document.getElementsByTagName('head')[0];
	head.appendChild(link);
}
loadStyles(css);
创建style标签来加载样式

var style=document.createElement('style');
var stylecontent=document.createTextNode('body{color:red}');
style.appendChild(stylecontent);
var head= document.getElementsByTagName('head')[0];
head.appendChild(style);

####DOM扩展
1.querySelector()返回第一个
2.querySelectorAll()返回所有
返回Nodelist中每一个元素，可以使用方括号方法，也可以使用.item(i)方法
p307
document.readyState有两种状态
loading和complete
if(document.readyState=="complete"){
	//window.onload=function(){}
}

document.compatMode浏览器采用了那种渲染模式
CSS1Compat---标准模式
BackCompat---混杂模式

document.head==document.getElementsByTagName('head')[0]

HTML5规定，可以为元素添加非标准的属性，但要添加前缀data-
data-whatever='';//提供与渲染无关的信息或者提供语义。
ele.dataset.whatever//访问自定义的属性

element.children==element.childNodes
mydiv.style.cssText=""//将重写mydiv的css样式!

offsetWidth,offsetHeight//元素宽高，包括边框内边距，内容
clientWidth,clientHeight//元素宽高，不包括边框

scrollLeft//被隐藏在内容区域左边的宽度
scrollTop//被隐藏在内容区域上方的高度，向下滚，则变大
scrollHeight,scrollWidth//没有滚动条情况下内容区域的宽高

跨浏览器确定文档的总高度
var docWidth=Math.max(document.body.scrollWidth||document.documentElement.scrollWidth,document.body.clientWidth||document.documentElement.clientWidth);
var docHeight=Math.max(document.body.scrollHeight||document.documentElement.scrollHeight,document.body.clientHeight||document.documentElement.clientHeight);

function backToTop(){
	if(document.body.scrollTop!=0){
		document.body.scrollTop=0;
	}
	if(document.body.scrollLeft!=0){
		document.body.scrollLeft=0;
	}
}
setInterval(backToTop,100);

HTML指定事件处理程序---直接在元素中onclick="function(){}"

DOM0级事件
myele.onclick=function(){
	//this指向元素本身！
}
myele.onclick=null可以删除事件
DOM2级事件
addEventListener()和
removeEventListener()

myele.addEventListener('click',func,false//冒泡);
removeEventListener()无法移除匿名参数

var EventUtil = {
	addHandler:function(element,type,handler){
		if(element.addEventListener){
			element.addEventListener(type,handler,false);
		}else if(element.attachEvent){
			element.attachEvent('on'+type,handler);
		}else{
			element["on"+type]=handler;
		}
	},
	removeHandler:function(element,type,handler){
		if(element.removeEventListener){
			element.removeEventListener(type,handler,false);
		}else if(element.detachEvent){
			element.detachEvent("on"+type,handler);
		}else{
			element["on"+type] = null;
		}
	}
};
var div = document.getElementsByTagName('div')[0]
handler=function(){
	//sth here
}
EventUtil.addHandler(div,'click',handler);

P374事件对象
DOM中的事件对象

var btn = document.getElementsByTagName('btn')[0];
btn.onclick=function(event){
	console.log(event.target);
}
0级事件
<input type="button" value="click me" onclick="alert(event.type)"/>
var btn=document.getElementsByTagName('input')[0];
var handler = function(event){
	switch(event.type){
		case "click":
			alert("clicked");
			event.preventDefault();//阻止默认行为
			event.stopPropagation();//阻止冒泡
			break;
		case "mouseover":
			event.target.style.backgroundColor="red";
			break;
		case "mouseout":
			event.target.style.backgroundColor="";
			break;
	}
};

btn.conclick = handler;
btn.onmouseover = handler;
btn.onmouseout = handler;

IE中的事件对象

DOM0级事件中，event是window对象的一个属性
使用attachEvent()方法的时候，也能通过window对象来反问event对象，不过
也能作为一个参数传递

IE中的事件属性方法
cancelBubble=true ==> stopPropagation()
returnValue=false ==>preventDefault() 
srcElement ==>target
type

#事件类型

UI事件
load：加载完成之后触发
unload：卸载完全之后触发
abort：停止下载过程中
error：当发生错误时触发
select：选择文本框中字符时候触发
resize：窗口大小变化时候触发
scroll：时候触发
焦点事件
blur：失去焦点时候
focus：获得焦点时候，不冒泡
focusin：获得焦点，冒泡
鼠标与滚轮事件
click：单击时候触发
dbclick：双击时候触发
mousedown：按下鼠标键触发
mouseenter：移入时触发，不冒泡
mouseleave：离开时候触发，不冒泡
mousemove：在内部移动时候触发
mouseout：移出时候触发
mouseover：移入时候触发
moouseup：释放按键时触发
(1)mousedown
(2)mouseup
(3)click
(4)mousedown
(5)mouseup
(6)click
(7)dbclick

var btn=document.getElementsByTagName('body')[0];
btn.onmousemove=function(e){
	console.log("clientX: "+e.clientX+"\n"+'clientYY: '+e.clientY)
	console.log("pageX: "+e.pageX+"\n"+'pageY: '+e.pageY)
}
clientX +scrollLeft == pageX
clientY +scrollTop == pageY

screenX:相对于电脑屏幕的x
screenY:相对于电脑屏幕的y

鼠标滚轮事件

document.onmousewheel=function(e){
	alert(e.wheelDelta);
}

键盘与文本事件
keydown：按下键盘任意字符时，按住不放，会重复触发此事件
keypress：按下键盘任意字符时，按住不放，会重复触发此事件
keyup：释放键盘触发

p421
内存和性能
交互过多，性能下降---事件委托
在父元素绑定一个事件，然后由子元素的冒泡传递到父元素处理
不需要的程序太多--
移除带有事件处理程序的元素时候，手工移除事件处理程序
tbn.onxxx = null

模拟事件

<input	type="image" src="xxx.jpg"/>
图像提交表单
<input type="reset" value="reset form">

ES6最新引入的Iterable类型，Array,Map,Set都是属于Iterable理性的值，都能够使用for of迭代
for of修正了for in 对数组，字符串存在的一些问题。
for in 对于Array和String来说，遍历的其实是index!
Iterable内置有forEach()方法
arr.forEach(function(ele,indes,arr){
	//do sth here.
})

set.forEach(function(ele,sameele,set){
	//do sth here.
})

map.forEach(function(value,key,map){
	//do sth here.
})

javascript 中arguments关键字，指向函数内部实际传入的参数，是个类数组哟
arguments.callee指向函数名称！
不定义任何形参都能拿到参数并使用参数。
ES6引入rest参数，表示不定形参

在for循环等语句块中
ES6引入的新的关键字let代替var可以声明块级作用域。
const用于声明常量，具有块级作用域

apply
接受两个参数，第一个是this要绑定在谁身上，第二个是函数本身。
普通函数this绑定为null。
var xiaoming={
	name:"conan",
	birthday:1991,
	age:function(){
	var that=this;//在进一层的时候this就不是当前对象啦
		function getAge(){
		var year=new Date().getFullYear();
		return year-that.birthday;
		}
		return getAge();
	}
};
xiaoming.age();

注意
var arr=['1','2','3','3']
var r=arr.map(Math.pow)
r//1,2,9,9

var arr=['1','2','3']
var r=arr.map(function(x){
	return x*x;
})
r//1,4,9

闭包
pow2(x)==>x*x
pow3(x)==>x*x\*x
try{
	function make_pow(n){
		return function(x){
			return Math.pow(x,n)
		}
	}
	throw new Error("测试")
}catch(e){
	alert("错误： "+e)
}finally{
	console.log('finished!')
}
pow2=make_pow(2);
pfow3=make_poe(3);

try{
	//需要检测部分
}catch(e){
	//抛出错误
}finally{
	//最后怎样
}

Error对象，TypeError，ReferenceError

try{
	...
}catch(e){
	if(e instanceof TypeError){
	alert("TypeError!");
}else if(e instanceof Error){
	alert(e.message);
}else{
	alert("Error: "+e);
}
}

throw new Error("错误")//抛出一个新错误，直接到catch语句

#离线应用与客户端缓存

navigator.onLine属性检测是否联网,是,返回true,否,返回false
HTML5定义两个事件,online和offline,这两个事件在window对象上触发
应用缓存applicationCache
数据储存
--
--

最佳实践
- 可维护性的代码
1.可解释,其他人一上手就能理解并明白它的意图,无需开发人员的完整解释
2.直观性,不管操作过程是多么复杂
3.可适应性,修改不需要重写
4.可扩展,必须考虑到将来的扩展性
5.可调试性
6.一般4个空格的缩进,制表符在不同文本编辑器中不同
7.函数和方法,注释其目的,用于完成的任何,是否有返回值,参数等等
8.大段代码前,放注释
9.复杂的算法,加注释
10.hack加注释
11.变量和函数命名:
变量名为名词如car,person等,函数名以动词开始,如getName(),返回布尔值的函数一般以is开头,变量和函数使用合乎逻辑的名字.
12.初始化变量,告诉大家,这个变量将来会是什么类型的
13.保证HTML和JavaScript的松散耦合
14.尊重对象,不是你的对象,不要随便重写原型,定义属性和方法
15.避免全局变量,可以创建一个对象,让函数,变量在其中
16.减少null的使用
17.使用常量,多处要用到的值,编为一个常量,用于给用户显示的字符串,都应该被抽取出来,方便国际化,推荐一个公共地方储存URL,将来可能改变的值,应该被抽取出来作为一个常量

- 保证代码性能
1.注意作用域,访问全局变量总是比局部变量慢,因为要遍历作用域,减少花在作用域链上的时候，就能增加脚本的整体心累了.
2.避免with语句,他会加长作用域链
3.用到多次对象属性的时候,将其保存在变量中
4.优化循环,
a.减值迭代
b.简化终止条件
c.简化循环体
d.do-while这种后测试循环更快
e.展开循环,如果循环次数确定,展开直接调用还会快点duff展开.
f.避免双重解释
g.原生方法比较快,Math对象的方法容易被忽略哦,switch语句比较快哦,位运算符比较快.
h.最小化语句数量,一个var申明多个变量
i.插入迭代值,value[i];i++ -> value[i++];
j.使用字面量方法创建数组和对象
k.
l.
m.
n.
o.
p.
q.
p692

- 部署代码































































































































































*******
//设置定时器
setInterval(
function(){
document.body.scrollTop+=2000;
for(var i=0;i<$(".imgpage li").length;i++){
console.log($('.imgpage li')[i].getAttribute("data-objurl"))}},200)
//解除定时器
for(var i=0;i<99999;i++){
	clearInterval(i);
}
*******



*****
str="";
strf="";
for(var i=0;i<str.length;i++){
strf+=str.charCodeAt(i)+',';
}
strf=strf.substring(0,strf.length-1);
String.fromCharCode(strf);
*****






