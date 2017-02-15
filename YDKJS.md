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































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































