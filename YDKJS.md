函数会被先声明后赋值
函数申明会被提升,但是函数表达式不会被提升

函数优先，变量其次

无论通过何种手段将内部函数传递到所在词法作用域以外，它都会持有对原始定义作用域的引用，舞灵在何处执行这个函数都会使用闭包。

闭包和循环啊

	for (var i=1; i<=5; i++) {
		(function(j) {
			setTimeout( function timer() {
			console.log( j );
			}, j*1000 );
		})(i);
	}

	for (let i=1; i<=5; i++) {
		setTimeout( function timer() {
			console.log( i );
		}, i*1000 );
	}

单例模块模式

	var foo = (function CoolModule(id) {
		function change() {
			// 修改公共 API
			publicAPI.identify = identify2;
		}
		function identify1() {
			console.log( id );
		}
		function identify2() {
			console.log( id.toUpperCase() );
		}
		var publicAPI = {
			change: change,
			identify: identify1
		};
		return publicAPI;
	})( "foo module" );
	
	foo.identify(); // foo module
	foo.change();
	foo.identify(); // FOO MODULE

##现代模块管理机制

	var MyModules = (function Manager(){
		var modules = {};
	
		function define(name,deps,impl){
			for(var i=0;i<deps.length;i++){
				deps[i] = modules[deps[i]];
			}
			modules[name] = impl.apply(impl,deps);
		}
		function get(name){
			return modeuls[name];
		}
		return {
			define:define,
			get:get
		};
	})();
	
	MyModules.define("bar",[],function(){
		function hello(who){
			return "Let me introduce: " + who;
		}
		return {
			hello:hello
		};
	});
	
	MyModules.define("foo",["bar"],function(bar){
		var hungry = "hippo";
	
		function awesome(){
			console.log(bar.hello(hungry).toUpperCase());
		}
		return {
			awesome:awesome
		};
	});

	var bar =MyModules.get("bar");
	var foo =MyModules.get("foo");
	
	console.log(bar.hello("hippo"));//Let me introduce: hippo
	foo.awesome(); // LET ME INTRODUCE: HIPPO

## ES6模块加载机制
	
	// bar.js
		function hello(who) {
				return "Let me introduce: " + who;
			}
		export hello;
***
	// foo.js
	// 仅从 "bar" 模块导入 hello()
		import hello from "bar";
		var hungry = "hippo";
		function awesome() {
			console.log(
				hello( hungry ).toUpperCase()
			);
		}
		export awesome;
***
	// baz.js
		// 导入完整的 "foo" 和 "bar" 模块
		module foo from "foo";
		module bar from "bar";
		console.log(
			bar.hello( "rhino" )
		); // Let me introduce: rhino
		foo.awesome(); // LET ME INTRODUCE: HIPPO

import将一个模块中的一个或多个API导入当前作用域,module会将整个模块API导入
***
##附录A 词法作用域和动态作用域
大部分语言都是基于词法作用域,JavaScript亦如此(词法作用域是一套关于引擎如何寻找变量以及会在何处找到变量的规则)
和动态作用域的区别
动态作用域的作用域链式基于调用栈的，而不是代码中的作用域嵌套
词法作用域是在写代码或者说定义时确定的，而动态作用域是在运行时确定的。(this也是！)词法作用域关注函数在何处申明，动态作用域关注函数从何处调用。

	function foo() {
		console.log( a ); // 2
	}
	function bar() {
		var a = 3;
		foo();
	}
	var a = 2;	
	bar();

ES6添加了一个特殊的词法形式用于函数申明，叫做箭头函数，用当前的词法作用域覆盖了this本来的值。

this是在运行的时候绑定的,取决于函数的调用方式,

#this全面解析
strict 模式this不能绑定到全局变量上,为undefined

回调函数丢失this绑定是非常之常见的

硬绑定
bind(..)会返回一个硬编码的新函数,它会吧参数设置为this的上下文并调用原始函数

判断this
1.函数是否在new中调用(new 绑定) ,this绑定的是新创建的对象
var bar = new foo()

2.this是否荣光call,apply(显式绑定),this绑定的是制定的对象
var bar = obj1.foo()

3.函数是否在某个上下文对象中调用(隐式绑定),thiss绑定的是哪个上下文对象
var bar = obj1.foo()

4.如果都不是,使用默认绑定,严格模式绑定到undefined,否则绑定到全局对象

例外：
传入null到如下，实际上是默认绑定
apply,call,bind可以对参数进行科里化

//把数组展开

	foo.apply(null,[2,3])

更加安全的this——DMZ

	function foo(a,b){
	    console.log("a: "+a+",b: "+b)
	}
	var O = Object.create(null);//O表示‘我希望this是空’
	
	foo.apply(O,[2,3]);//a:2,b:3
	
	var bar = foo.bind(O,2);
	bar(3);// a:2,b:3

间接引用，最容易发生在赋值时候,会引用默认绑定 

ES6中的箭头函数根据的是词法作用域来决定this(ES6之前用that = this)

对象中，属性名永远都是字符串

所有普通的Prototype链最终都会指向内置的Object.prototype

构造函数有一个prototype属性,这个属性是通过构造函数生成对象的原型对象,这个原型对象还有个constructor属性,指向构造函数本身.
通过构造函数生成的对象也能通过原型委托查找到constructor这个属性.当你替换了构造函数.prototype(重写原型),constructor属性并不会自动获得哦.

用new调用了才叫构造函数.

把Bar.prototype关联到Foo.prototype的方法
//ES6之前
Bar.prototype = Object.create(Foo.prototype);
//ES6的方法
Object.setPrototypeOf(Bar.prototype,Foo.prototype);

Object.create()会创建一个新对象，并将它关联到我们制定的对象,这样我们就可以充分发挥Prototype的微粒，而且避免不必要的麻烦(比如使用new的构造函数调用会生成.prototype和.constructor引用)

Object.create(null)会创建一个拥有空[[prototype]]链接的对象，这个对象法务进行委托,由于这个对象没有原型链,所以instanceof操作符无法进行判断，总是返回false,这类特殊的空[[prototype]]对象通常被称作字典，他们完全不会受到原型链的干扰，非常适合用来储存数据。

Object.create()的polyfill代码
//ES5之前的环境

	if(!Object.create){
		Object.create = function(o){
			function F(){};
			F.prototype = o;
			return new F();
		}
	}


You Dont Know JS中篇

JavaScript内置类型一共七种
null
undefined
boolean
string
number
object
symbol
除对象外，其他对象被称为基本类型
可以用typeof进行判断，
但是null判断例外typeof null为object
typeof function(){}为function(object子类型)
typeof []为object(object子类型)
typeof 运算符总是返回一个字符串...

	var a;
	a; // undefined
	b; // ReferenceError: b is not defined

	var a;
	typeof a; // "undefined"
	typeof b; // "undefined"(未被申明更合适)

判断某个变量存不存在或者有没有被申明

	if(typeof myVar ！=='undefined'){}

访问不存在的对象属性(甚至是在全局对象window上)不会产生ReferenceError

建议用对象来存放键值对
用数组来存放数字索引

类数组转换为数组

	function foo() {
		var arr = Array.prototype.slice.call( arguments );
		arr.push( "bam" );
		console.log( arr );
	}
	foo( "bar", "baz" ); // ["bar","baz","bam"]

ES6中也有等价方法

	var arr = Array.from(arguments);

字符串和数组反转

arr.reverse()
string.split("").reverse().join("")

NaN是JavaScript种唯一一个不等于自身的值

简单值(标量，基本类型的值)总是通过值复制的方式来赋值/传递,包括null,undefined,字符串,数字,布尔和ES6中的symbol,是不可更改的

复合值——对象(包括数组，封装对象,函数),总是通过引用复制的方式来赋值/传递

原生函数作为构造函数时候，可以不用new
new String('fk')
等价于
String('fk')

toJSON()应该返回一个能够被字符串化的安全的JSON值,而不是返回一个JSON字符串

假值的布尔强制类型转换结果为false

undefined
null
false
+0，-0和NaN
""

假值以外的值都是真值

字符串和数字之间的转换是通过String()和Number()这两个内建函数来实现的                                

将日期对象转换为时间戳

	new Date().getTime()
	Date.now()

旧浏览器polyfill

	if(!Date.now){
		Date.now = function(){
			return +new Date()
		};
	}

~myString.indexOf(..)
如果找不到，返回-1,~后为0，其他情况~后都不为0

解析和转换
	var a = "42";
	var b = "42px";
	Number( a ); // 42
	parseInt( a ); // 42
	Number( b ); // NaN
	parseInt( b ); // 42

parseInt()针对的是字符串值

从 ES5 开始 parseInt(..) 默认转换为十进制数，除非另外指定。如果你的代码需要在 ES5之前的环境运行，请记得将第二个参数设置为 10 。

显示强制类型转换为布尔值最常用的还是!!

	var a = "0";
	var b = [];
	var c = {};
	var d = "";
	var e = 0;
	var f = null;
	var g;
	!!a; // true
	!!b; // true
	!!c; // true
	!!d; // false
	!!e; // false
	!!f; // false
	!!g; // false

+ 作为数字加法操作是可互换的，即 2 + 3 等同于 3 + 2 。作为字符串拼接操
作则不行，但对空字符串 "" 来说， a + "" 和 "" + a 结果一样。

	function onlyOne() {
		var sum = 0;
		for (var i=0; i < arguments.length; i++) {
			// 跳过假值，和处理0一样，但是避免了NaN
			if (arguments[i]) {
			sum += arguments[i];
			}
		}
		return sum == 1;
	}
	var a = true;
	var b = false;
	onlyOne( b, a ); // true
	onlyOne( b, a, b, b, b ); // true
	onlyOne( b, b ); // false
	onlyOne( b, a, b, b, b, a ); // false

	ES5中等价方法
	function onlyOne() {
		var sum = 0;
		arg = Array.prototype.slice.call(arguments);
		return arg.reduce(function(x,y){
			return sum+x+y
		})===1;
	}
	var a = true;
	var b = false;

以下情况发生布尔值隐式强制类型转换
1. if()判断语句
2. for()条件判断表达式
3. while()和do...while()条件判断表达式
4. ?:三元运算符条件判断表达式
5. ||逻辑或和&&逻辑与左边的操作数

||和&&首先对第一个操作数执行条件判断，如果不是布尔值就进行布尔类强制类型转换，然后再执行条件判断，

||如果判断结果为true就返回第一个，第一个不为true就返回第二个
&&如果判断结果为true就返回第二个，第一个不为true就返回第一个
最后还会发生隐式强制类型转换
	a || b;
	// 大致相当于(roughly equivalent to):
	a ? a : b;
	a && b;
	// 大致相当于(roughly equivalent to):
	a ? b : a;

常见的||用法(赋予默认值)

	a = a ||'sth1';
	b = b ||'sth2';

	function foo() {
		console.log( a );
	}
	var a = 42;
	a && foo(); // 42

	== 允许在相等比较中进行强制类型转换，而 === 不允许。

==比较中，会将两边转换为数字然后比较
	
	"0" == false; // true 
	false == 0; // true 
	false == ""; // true 
	false == []; // true 
	"" == 0; // true 
	"" == []; // true
	0 == []; // true 

如果两边的值中有 true 或者 false ，千万不要使用 == 。
如果两边的值中有 [] 、 "" 或者 0 ，尽量不要使用 == 。
这时最好用 === 来避免不经意的强制类型转换。这两个原则可以让我们避开几乎所有强制
类型转换的坑。

[] + {}; // "[object Object]"
{} + []; // 0

第一行代码中，{}被当做一个空对象来处理，[]被转换为""，{}被转换为"[object Object]"
第二行代码中，{}被当做一个独立的代码块，但不执行任何操作，最后将[]显示强制类型转换为0

	&& 运算符的优先级高于 || ，而 || 的优先级又高于 ? : 。

程序的一部分现在运行,而另一部分则在将来运行,现在和将来之间有段间隙,在这段间隙中,程序没有活跃执行,事实上,程序中现在运行的部分和将来运行的部分之间的关系就是异步编程的核心.

根据一个值的形态(具有哪些属性)对这个值的类类型做出一些嘉定，这种类型检查一般用术语 鸭子类型(duck typing)来表示,如果看起来像只鸭子，叫起来像只鸭子，那它就一定是只鸭子。

对Promise的鸭子类型检测
	
	if (
		p !== null &&
		(
			typeof p === "object" ||
			typeof p === "function"
		) &&
		typeof p.then === "function"
	) {
		// 假定这是一个thenable!
	}
	else {
	// 不是thenable
	}

然而其他,或其原型链上有then属性的对象也容易会被认为是Promise.

Promise.resolve()将含有thenable属性的对象封装为可信任的Promise对象

***
判断值的类型的方法
Object.prototype.toString.apply(obj);
typeof obj;
a instanceof obj;

值的类型
number
string
boolean
null
undefined
Object(Object,array,null,function,..)

typeof 能检测出来的类型
number
string
boolean
undefined
Object(Object,null,array,...)
function

有意思的
var toString = Object.prototype.toString;
function getType(obj){return toString.call(o).slice(8,-1);};
但是new Number(1)却会返回Number


匿名函数的执行
	!function(){}()

	(function(){})()

	(function(){}())

Object.defineProperty(obj,someProperty,{....});//默认所有的标签都是false.

获取对象的属性标签
Object.getOwnPropertyDescriptor({a:''},'a');//obj为要查看的对象,key为要查看的对象属性的key值.
Object {value: "", writable: true, enumerable: true, configurable: true}

Object.keys(obj);//获取obj对象上所有的key

修改属性的值可以通过赋值修改也可以通过defineProperty修改属性的value

a={a:11};//Object {a:10}
b = Object.create(a);
Object.isFrozen(a);//false
Object.isFrozen(b);//false
pofb = Object.getPrototypeOf(b);//Object {a:11}
pofa = Object.getPrototypeOf(pofb);//Object {}

Object.isFrozen(a);//false
Object.isFrozen(pofb);//false
Object.isFrozen(pofa);//true

Object.freeze(b);
Object.freeze(Object.getPrototypeOf(b));

Object.isFrozen(a);//true
Object.isFrozen(b);//true

序列化
JSON.stringify(obj);//将对象序列化为JSON字符串
注意，
1. 对象如果有值为undefined,则不会出现在序列化后的结果中
2. NaN,Infinity 转换为null,时间转换为UTC时间格式. 

JSON.parse(string);//将JSON字符串解析为obj对象

自定义toString()方法,valueOf()方法

in操作符对数组来说访问的是索引!!

对象转换先看valueOf()方法,再看toString()方法

遍历二维数组
	var arr=[[1,5,5],[null],[461,,0]]
	for(var i=0;i<arr.length;i++){
		for(var j=0;j<arr[i].length;j++){
			console.log(arr[i][j]);
		}
	}

稀疏数组并不好友从0开始的连续索引

重复某个字符串制定次数
	function repeatString(str,n){
		return new Array(n+1).join(str);
	}

reverse()会对原数组进行修改
splice()会对原始数组进行修改

concat()不会
slice()不会
***















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































