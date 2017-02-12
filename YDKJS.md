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





