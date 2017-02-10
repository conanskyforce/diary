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














