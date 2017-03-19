时隔半月，再次翻开了有JavaScript圣经之称的JavaScript高级程序设计，转眼已过2016,2017又是一个新的开始，纵使寒风起，人生不言弃。

'user strict';开启严格模式
申明变量一定要用var，切记切记！！
JavaScript一共只有六种数据类型
Null
Undefined
Boolean
String
Number
Object--包括Array，Function，object，Null![](stop)

typeof返回的结果有这么几种
String
Number
Boolean
Undefined
Object--包括对象和null
Function

==比较undefined和null会得到相等的结果

Boolean类型有两个字面值true和false，区分大小写的哦

JavaScript中判断为false的值

false(Boolean)
空字符串(String)
0或NaN(Number)
null(Null)
undefined(Undefined)

isFinite(num)判断某个数是不是在Number.MAX_VALUE与Number.MIN_VALUE之间
任何数值除以0会返回NaN
NaN不与任何值相等，包括他自己
isNaN()判断是否"不是数值"

三个函数将非数值转换为数值

用于任何数据类型：
Number()
true--1  false--0
null--0
Undefined--NaN
字符串--只包含数值则转换成对应数字，空字符串转换成0
对象，调用对象valueOf()方法，如果转换为NaN，然后调用toString()方法


用于字符串：
parseInt()，空字符串，或字母开头返回NaN，其余从开始有数字的地方到第一个不是数字的地方结束
第二个参数为 使用的基数
parseFloat()，空字符串，或字母开头返回NaN，其余从开始有数字的地方到第二个小数点的地方结束，它只解析10进制，没有第二个参数，遇到0x开头，解析为0

##String 类型
1. 字符字面量
转义序列
\n --换行
\t --指标
\b --空格
\\ --斜杠
\' --单引号
\" --双引号
\xnn --十六进制表示的字符
\unnnn --十六进制表示的Unicode字符
字符串的length属性指的是转义过后的长度

转换字符串
除了null和Undefined没有之外，其余对象都有的toString()方法
还有一个更加万能的方法String(要转换的)
null返回'null'
Undefined返回'undefined'

要将某个值转换为字符串可以+''

##Object类型
Object对象是所有实例的基础
所有实例都继承了Object的方法
这些方法有
constructor 返回构造函数
hasOwnProperty() 检测给定属性只在当前对象中
isPrototypeOf() 是。。。的原型
propertyIsEnumerable() 检测戈丁属性是否能够使用for  in来枚举
toString() 返回对象的字符串
valueOf() 返回字符串，数值或布尔值，通常情况与toString()相同

#操作符
算数操作符，位操作符，关系操作符和相等操作符
应用于对象时候，一般都会调用对象 的valueOf()方法和toString()方法
##一元运算符
加减在前，则先算加减
应对于布尔值：false--0 true--1
应对于字符串：包含数字变为数字再加减，不包含变为NaN
应对于浮点数：直接加减1
应对于对象：调用toString()或valueOf()方法

##布尔操作符

1. 逻辑非 ！
2. 逻辑与&&，是个短路操作符（第一个结果为true，就不再求第二个了）
3. 逻辑或||，也是短路操作符

全等和等于
=== 既判断值也【判断类型
== 转换后再判断

for-in语句用来迭代对象的属性

arguments类数组才是函数实际接收的参数

#变量、作用域、内存
***

##基本类型和引用类型
五种基本类型：Undefined、null、Boolean、Number、String
一种引用类型：Object
基本类型按值访问，保存在栈内存中
引用类型的值是保存在内存中的对象，按引用访问，保存在堆内存中
不能直接操作对象的内存空间，实际上操作的是对象的引用（而不是实际的对象）
***
能给引用类型添加属性
不能给基本类型添加属性，虽然添加了也不会报错，但是之后访问变消失了
***
基本类型的变量复制结果两对象互不相干，对应内存中两个空间
复制引用类型结果还是会相互影响
***
所有函数的参数都是按值传递的
JS中的基本类型按值传递，对象类型按共享传递。
**在调用函数传参时，和引用传递的不同在于，共享传递对函数形参的赋值，不会影响实参的值，而增加传入形参对象的属性，会对原对象产生影响。**

检测类型--对于引用类型 typeof的帮助不大，但我们有
instanceof（...是...的实例）
person instanceof Person;//true
且所有引用类型的值都是Object的实例

##执行环境和作用域
***
每个执行环境都有一个与之关联的变量对象，环境中所有变量和函数都保存在这个对象中
全局执行环境是最外围的一个执行环境。宿主环境不同，全局执行环境也不一样。浏览器中，全局执行环境是window对象。
***
每个函数都有自己的执行环境（花括号之类的表达式）
作用域链，内层能访问外层，反之不成立

变量申明，使用var申明变量，会将变量自动添加到最接近的环境之中。
如果没用var则直接添加到全局环境中。

#引用类型

1. Object类型 
对象是某个特定引用类型的实例

var person = {};//与 new Object()相同

访问对象属性方法
.操作符
[]操作符，可以访问变量
2. Array类型
数组每一项可以保存任意类型的数据
创建数组
new Array(值/数组长度)
Array(值/数组长度)
访问数组值用方括号加基于0的数字索引
设置亦然，注意设置能改变数组长度
数组的长度length属性也是可写的

2.1 检测数组
arr instanceof Array
Array.isArray(arr)不受限于全局环境

2.2转换方法
arr.toString()返回的是字符串
arr.valueOf()返回的还是数组
调用alert方法会调用toString()方法
arr.join()方法默认逗号作为分隔符

2.3栈方法
栈数据结构的访问规则:后进先出(last in first out)
arr.push()添加数组值(末尾)，返回修改后数组长度
arr.pop()去除数组值(末尾)返回删除的那个值

2.4队列方法
队列数据结构的访问规则是FIFO(First In First Out)
arr.shift()删除第一项，并返回它
arr.unshift()插入到第一项，返回新数组的长度

2.5 重排序方法
arr.reverse()反转数组元素出现的顺序
arr.sort()会调用每项值的toString()方法，所以始终比较的都是字符串
可以接受一个比较函数作为参数
arr.sort(function(a,b){return a-b;})第一个应该位于第二个之前，则返回一个负数

2.6 操作方法
arr.concat()没参数相当于复制，参数包含二维数组也会被展开添加，但是只展开一层哦@。@
arr.slice()返回的起始和结束为止，含头不含尾
有一个参数是负数时候，用数组长度加上该数来确定位置
arr.splice(start,num_to_del[,replace])这个方法会改变原数组

2.7 位置方法
arr.indexOf(n,pos)查找该项在数组中位置，从pos处开始
arr.lastIndexOf()从末尾开始找

2.8迭代方法
传入这些方法的函数会接受三个参数，数组项的值,该项在数组中的位置,和数组对象本身
- every()每一项运行给定函数，每一项都返回true,则返回true
- filter()每一项运行给定函数，返回返回true的项组成的数组
- forEach()每一项运行给定函数，木有返回值
- map()每一项运行给定函数，返回每次函数调用的结果组成的数组
- some()每一项运行给定函数，任意一项返回true,则返回true
arr.every(function(item,index,arr){return item>=10;})
每项都大于10返回true
arr.filter(function(item,index,arr){return item>=10;})
返回大于10的项组成的数组
arr.some(function(item,index,arr){return item>=10;})
一些项大于10就返回true
arr.map(function(item,index,arr){return item>=10;})
返回每一项调用的结果组成的数组(true,false)组成
arr.forEach(function(item,index,arr){return item>=10;})
本身迭代，不返回

2.9 缩小方法
- reduce()
- reduceRight()
这俩方法都会迭代所有项,构建一个最终返回值
前者从左遍历，后者从右遍历
arr.reduce(function(prev,cur,idx,arr){
	return prev*cur;
});//求数组的积

3. Data类型
构建一个日期对象
var data = new Date(1896,11,16,18,22)

Data.now()方法返回现在距离1970年1月1日的毫秒数

3.1 继承方法
Date类型的valueOf()方法，返回的是日期的毫秒数，因此可以直接比较日期大小

3.2 日期格式化
...

3.3 Date类型的方法
var date = new Date()
date.getTime();//返回值与valueOf()相同，毫秒数
date.getFullYear()取得四位数年份
date.getMonth()取得月份
date.getDate()月份总的天数
date.getDay()星期几0表示周日
date.getHours()小时数0-23
date.getMinutes()分钟数0-59
date.getSeconds()秒数0-59
date.getMillSeconds()毫秒数

4.4 RegExp类型
reg = /pattern/igm;
reg = new RegExp('pattern','igm')

4.4.1 RegExp实例属性
reg.global;是否设置了g标志
reg.ignoreCase;是否设置了i标志
reg.lastIndex;匹配位置
reg.multiline;是否设置了m标志
reg.source;按字面量模式返回

4.4.2 RegExp 实例方法
reg.exec(string)返回包含第一个匹配信息的数组
数组第一项是与reg匹配的字符串
其余项是匹配组匹配的字符串

reg.test(string)匹配返回true,否则返回false

4.3 RegExp 构造函数属性
RegExp.$_
RegExp.$&
RegExp.$+
RegExp.$`
RegExp.$*
RegExp.$'

5. Function类型
函数也是对象所有函数都是Function对象的实例

5.1 没有重载
函数名唯一

5.2函数申明与函数表达式
函数申明会有变量提升

5.3作为值的函数
函数名本身就是变量，所以函数也可以作为值来使用
函数名不加圆括号表示的是函数变量

5.4 函数内部属性
this
arguments
arguments.callee
caller

5.5 函数属性和方法
length属性表示希望接受的命名参数的个数
prototype属性表示产生实例对象的原型
apply()和call()方法，为了是在特定的作用域中调用函数，能扩充函数作用域！！
funcname.call(this,arguments)为了是在当前作用域中调用funcname的方法
第一个参数是当前作用域this指向的对象,函数内调用this指向的就是当前作用域this
如果要调用别的作用域
myfunc.call(obj)就将myfunc中的this指向obj对象!!!
apply(this,[array])
call(this,arr1,arr2..])
bind()方法与call类似，但创造了一个函数的实例

6. 基本包装类型
3种特殊的引用类型
Boolean
Number
String
引用类型与基本包装类型的主要区别就是对象的生存期
自动创建的基本包装类型的对象，只存在于一行代码执行的一瞬间，然后被立即销毁，这也是为什么我们不能为基本类型添加属性和方法。

var a='string'
a.valueOf();
//相当于
n=new String('string')-->
n.valueOf()-->
n= null-->被立即销毁

而 b = new String('string2');不一样，已经是一个对象了

6.1 Boolean类型
typeof操作符对基本类型返回的是 Boolean
对引用类型返回的则是 Object
其次 Boolean 对象是Boolean类型的实例，所以instanceof操作符测试Boolean对象返回的是true，而基本类型返回的是false
false instanceof Boolean;//false
new Boolean(false) instanceof Boolean;//true
typeof(new Boolean(false));//object

6.2 Number 类型

toString()返回几进制数值的字符串形式
toFixed()方法返回需要的小数点位数的数值
toExponential()返回指数表示法
toPrecision()方法返回固定大小的格式

6.3 String类型

String类型的每个实例都有length属性
- 字符方法
- charAt()和charCodeAt()接受一个参数，基于0的字符位置
- charAt()返回对应位置的字符<==>方括号操作符访问字符
- charCodeAt()返回对应位置字符的编码

- 字符串操作方法
- concat()拼接字符串<==>+操作符
- slice(start,end)第二个参数可选，负数时加长度
- substring(start,end)第二个参数可选，负数时置零
- substr(start,num)num指返回字符个数，第一个负数加长度，第二个负数置零

以上几种方法都是返回一个基本类型的字符串，对原始字符串没有影响

- 字符串位置方法
- indexOf()类似数组
- lastIndexOf()类似数组

- trim()方法
- 删除前边和后边的空格

- 字符串大小写转换
- string.toLowerCase()转换为小写
- string.toUpperCase()转换为大写

- 字符串的匹配
- string.match(/xxxx/);//与调用reg.exec(string)返回的数组相同
- string.search(/xxx/);//返回第一个匹配项的所有，没找到返回-1
- string.replace(/sda/g,'xfa')将所有匹配到的项，替换为'xfa',第二个参数也可以是个函数接受的参数包括,匹配的元素,位置,原始文本
- string.split()基于制定的分隔符键字符串风分割,然后存放在数组当中,也可以接收第二个参数,用于制定数组的大小,超出长度的不返回

- localeCompare()
- string.localeCompare(string2)
- string改排在string2之前则返回-1，否则返回1，相等返回0

- fromCharCode()
- String.fromCharCode(num1,num2,num3);//接收一伙多个字符编码,然后将它们转换成一个字符串

- HTML方法
- 不建议使用

##7 单体内置对象
不依赖于数组环境的对象  
7.1 Global对象  
Global对象是兜底对象,  
isNaN(),isFinite(),parseInt(),alert()等都是global对象的方法  

1. URI编码方法Global  
- encodeURI()用于对URI某一段进行编码,不对冒号,反斜杠进行编码  
- encodeURIComponent()对发现的任何非标准字符串进行编码  
实践中更多的是对查询字符串参数进行URI编码
与之相对的是decodeURI()只能解用encodeURI()方法编码的字符串,decodeURIComponent()方法可以解一切字符串

2. eval()方法,这个方法就像一个JavaScript解析器

3. Global对象的属性
- Undefined
- NaN
- Infinity
- Object
- Array
- Function
- Boolean
- String
- Number
- ...

4. window对象
- web浏览器内部,global对象就是window对象一部分的实现

7.2 Math对象

1. Math对象属性
- 一些可能用到的特殊值
2. min()和max()方法,用于确定一组数组中的最大或最小值
Math.max(1,65,8,7,61,13);//65
对数组使用
var arr = [xx,x,x,x,,x]
var max = Math.max.apply(Math,arr)
3. 舍入
- Math.ceil()向上取整
- Math.floor()向下取整
- Math.round()四舍五入
4. random()方法
- Math.random()获取一个0到1之间的随机数，不包括0和1  
	选择x到y之间的任意数
	function selectFrom(x,y){
	var choices = y-x+1;
	return Math.floor(Math.random()*choices+x);
	}
	selectFrom(2,15);//2到15之间的任意整数,包括2和15
5. 其他方法
- Math.abs()绝对值
- Math.sqrt()平方根
- ...

##面向对象的程序设计

属性类型
1. 数据属性
修改属性默认的特性
Object.defineProperty()
接受三个参数,属性所在对象,属性名字,和描述符对象,这个对象的属性必须是
configurable,
enumerable,
writable,
value,
设置对应值,修改对应特性
2. 访问器属性
configurable
enumerable
set写入属性时调用
get读取属性时调用
_表示只能通过对象的方法访问的属性

定义多个属性
Object.defineProperties()
接收两个对象参数,第一个对象是要添加和修改属性的对象，
第二个对象的属性与第一个对象中要添加或修改的属性一一对应。

读取属性的特性
Object.getOwnPropertyDescriptor()取得给定属性的描述符

##创建对象
1. 工厂模式
function factory(){
var o = new Object()
o.xx=xx;
return 0;
}

2. 构造函数模式
function Myfunc(a,b,c){
this.a=a;
this.b=b;
this.c=c;
this.func=function(){
console.log(this.a)
};
}
newfunc = new Myfunc(s,dag,e)
newfunc 是Myfunc的实例
注意调用时候用了new 
不同实例的同名函数实际上是不相等的,因为函数实例化的过程中,都新创建了一个作用域
原型模式：
使用原型对象，让所有实例共享它所包含的属性和方法
`
只要创建了一个新函数,该函数就有一个prototype属性，指向这个函数的原型对象,原型对象自动获得constructor属性,指向函数本身,当调用构造函数创建一个新实例之后,该实例的内部都将包含一个指针,指向构造函数的原型对象,这个指针一般 __proto__。
`
可以通过isPrototypeOf()...是...的原型对象
Object.getPrototypeOf(xx)返回xx的原型对象
对象属性,实例属性优先级屏蔽原型属性
obj.hasOwnProperty('na');//na属性是否只在obj中,不在原型中
'na' in obj;//'na'属性在obj中
function propertyInPrototype(obj,name){
    return !object.hasOwnProperty(name) &&(name in obj);
}
使用for-in循环的时候,返回的是所有能够通过对象反问的,可枚举的属性
Object.key()返回对象可枚举属性的字符串数组

对象字面量重写原型

	Person.prototype = {
		constructor:Person,
	    name:"xxx",
	    age:22,
	    func:function(){
		return this.name+this.age;
		}
	};

	==>因为上述constructor属性变为可遍历了，所以还需要修改如下
	Person.prototype = {
	    name:"xxx",
	    age:22,
	    func:function(){
		return this.name+this.age;
		}
	};
	Object.defineProperty(Person.prototype,'constructor',{
	enumerable:false,
	value:Person
	});
注意以上包含的constructor属性
记住，实例中的指针(__proto__)指向原型对象(也就是构造函数的prototype属性),而不是构造函数

来看一个例子
function Person(){
};
var allen = new Person();
Person.prototype = {
	constructor:Person,
	name:"allen",
	age:28,
	dosth:function(){
	console.log("Hello Mr "+this.name) 
	}
};
allen.__proto__=Person.prototype;//思考为什么要加上这一行
allen.dosth();
//已经创建了实例的情况下重写原型,就会切断现有实例与新原型之间的联系
原生引用类型都在其构造函数的原型上定义了这些方法
一般都不会直接修改原生对象的原型,而是按需添加方法

结合使用构造函数模式和原型模式
构造函数定义实例属性，原型模式用于共享方法和共享属性

再来看一个例子
function arraypush(){
	var earr=[];
	earr.push(arguments)
	return earr;
}
arraypush(1,3,5,7);//[Arguments[4]]

function arraypush(){
	var earr=[];
	earr.push.apply(earr,arguments)
	return earr;
}
arraypush(1,3,5,7);//[1, 3, 5, 7]达到目的

稳妥构造函数--道神(不使用this 与new的情况下)

##继承
a.prototype指向b的实例,则a的实例继承了b的方法,a的原型指向b的原型

默认原型都是Object的实例,因此默认原型都会包含一个内部指针,指向Object.prototype

确定原型和实例之间的关系 instanceof .. 是..的实例
Object.create()方法规范了原型式继承
接受两个参数,作为新对象原型的对象和(可选的)一个为新独享定义额外属性的对象

	Object.create(obj)
	<===>
	function cp(obj){
	function F(){}
	F.prototype = o;
	return new F()  
	}

#7.函数表达式

函数非标准的那么属性,指向函数指定的名字
函数申明:(函数声明提升)
function myFunc(){}

函数表达式(创建一个匿名函数,并将其赋值给myFunc,匿名函数的name属性是空字符串)
var myFunc = function(){}不会变量提升

7.1 函数递归是一个函数通过名字调用自身  

	var factorial = (function f(num){
		if (num<=1){
			return 1;
		}
		else{
			return num*f(num-1);
		}
	});

7.2 闭包--有权访问另一个函数作用域中的变量的函数
懈怠包含它函数的作用域  

7.2.1 闭包所保存的是整个变量对象,而不是某个特殊值(只能取得包含函数中任何变量的最后一个值)

	function arrFunc(){
		var arr=[];
		for(var a=0;a<10;a++){
			arr[a] = function(){
			return i;
			}
		}
	}

世纪的结果是arr的每一项都是10
改善：(通过定义一个匿名函数,并将立即执行该匿名函数的结果赋值给数组)

	function arrFunc(){
		var arr=[];
		for(var a=0;a<10;a++){
			arr[a] = function(){
			return function(){
				return num;
				};
			}(i);
		}
		return arr;
	}

7.2.2 关于this对象
匿名函数的执行环境具有全局性,因此其this对象通常指向window

	var myObject = {
		name:"this object",
		getNameFunc:function(){
			var that = this;
			return function(){
				return that.name;
			};
		}
	};

myObject.getNameFunc;//指的是一个函数
	function(){
			var that = this;
			return function(){
				return that.name;
			};
		}
myObject.getNameFunc();//调用这个函数

	function(){
		return that.name;
	};

myObject.getNameFunc()();//调用这个函数的函数

	"this object"

7.3 没有块级作用域

只有函数块,函数作用域

匿名函数模仿块级作用域  
	(function(){
		//这里是块级作用域
	})();

7.4 私有变量

私有变量包括函数的参数、局部变量和在函数内部定义的其它函数
如果函数内部创建一个闭包，那么闭包通过自己的作用域链也可以访问这些变量，而利用这一点，就可以创建用于访问私有变量的公有方法
，我们把这种方法成为特权方法

	function MyObject(){
		var private = 10;
		function privateFunc(){
			return false;
		}
		this.publicMethod = function(){
			private++;
			return privateFunc();
		};
	}
构造函数的缺点就是针对每个实例都会创建一组新方法

7.4.1 静态私有变量

	(function(){
	
		var private = 10;
		
		function privateFunc(){
			return false;
		}
		
		MyObject = function(){
		};
		Myobject.prototype.publicMethod = function(){
			private++;
			return privateFunc();
		};
	})();

私有变量和函数是由实例所共享的

7.4.2 模块模式
单例模式,值得是只有一个实例的对象.
	
	var singleton = {
		name:value,
		method:function(){
			//
		}
	};

	var singleton = function(){
		var private = 10;
		function privateFunc(){
			return false;
		}
		return {
			publicProperty:true,
			publicMethod:function(){
				private++;
				return privateFunc();
			}
		};
	}();

返回对象的匿名函数

7.4.3 增强模块模式

	var singleton = function(){
		var private = 10;
		function privateFunc(){
			return false;
		}
		var object =new CustomType();

		object.publicProperty:true;
		object.publicMethod:function(){
				private++;
				return privateFunc();
			};
		return object;
	}();

#8. BOM(浏览器对象模型)

8.1 window对象,表示浏览器的一个实例,既是JavaScript访问浏览器窗口的一个借口M又是ECMAScript规定的Global对象

8.1.1 全局作用域
所有在全局作用域中申明的变量,函数都会变成window对象的属性和方法,大全局变量不能通过delete操作符删除,而直接在window对象上定义的属性则可以.

###窗口位置
获得浏览器窗口相对于屏幕左边和上边的位置

var leftPos = (typeof window.screenLeft == "number")? window.screenLeft : window.screenX;

var topPos = (typeof window.screenTop == "number")? window.screenTop : window.screenY;

console.log("top: "+topPos+"\n"+"left: "+leftPos)

###移动窗口(chrome被禁用?)
window.moveTo(0,0)

###窗口大小
window.innerWidth(页面视图区域)
window.innerHeight
window.outerWidth(整个浏览器)
window.outerHeight

console.log("innerWidth: "+window.innerWidth+"\n"+"innerHeight: "+window.innerHeight)

console.log("outerWidth: "+window.outerWidth+"\n"+"outerHeight: "+window.outerHeight)

document.documentElement.clientWidth(页面视口),相较于innerWidth,不包括滚动条的宽度,chrome里边是13px
document.documentElement.clientHeight
等价于
document.body.clientWidth
document.body.clientHeight

console.log("clientWidth: "+document.documentElement.clientWidth+"\n"+"clientHeight: "+document.documentElement.clientHeight)

8.1.5 导航和打开窗口

setTimeout(function,delay)

for(var a=0;a<9999;a++){clearTimeout(a)}

setInterval亦然
开发一般使用超时调用

8.1.7 系统对话框

alert('alert')
confirm("are you sure?")
var promptContent = prompt("what's you name?");//单机确定prompt获取输入值，单机取消prompt为null

8.2 location对象
window.location ===document.location;//true
查询字符串参数
解析查询字符串，然后返回包含所有参数的一个对象  
	function getQuery(){
		var qs = (location.search.length>0?location.search.substring(1):""),
		args={},
		items =qs.length?qs.split("&"):[],
		item = null,
		name=null,
		value=null,
		i = 0,
		len = items.length;
		for(i=0;i<len;i++){
			item = items[i].split("=");
			name = decodeURIComponent(item[0]);
			value = decodeURIComponent(item[1]);
			if(name.length){
				args[name] = value;
			}
		}
		return args;
	}

8.3 navigator对象

8.3.1 检测插件
navigator.plugins有以下属性
name
description
filename
length

8.4 screen对象

#9.0 客户端检测

9.1 能力检测
先检测最常用的特性以保证代码最优化
9.2 怪癖(浏览器特殊行为检测)
9.3 用户代理检测

#10 DOM

Node类型
每个节点都有一个nodeType属性，表明节点的类型
元素节点--1
属性节点--2
文本节点--3
文档节点--9

.nodeName属性--元素的标签名
.nodeVlaue属性--元素节点的值

每一个节点都有一个childNodes属性,保存着一个NodeList对象,NodeList是一种类数组对象,可以通过方括号来访问，并且也有length属性，但它并不是Array的实例,另外值得注意的一点是这是基于DOM结构动态执行查询的结果

someNode.childNodes[0]
someNode的第一个子元素
someNode.childNodes.item(1)
someNode的第二个子元素

将NodeList对象转换为数组
var someNode = document;
someNode.childNodes;
var arrayOfNodes = Array.prototype.slice.call(someNode.childNodes,0);
someNode.childNodes;

每个节点都有一个parentNode属性,之下那个文档中的父节点
包含在childNodes列表中的每个节点相互之间都是同胞节点,可以使用
previousSibling属性和
nextSibling属性访问
第一个节点的previousSibling属性为null
最后一个节点nextSibling属性为null
父节点的firstChild指向第一个节点
父节点的lastChild指向最后一个节点
即
someNode.firstChild===someNode.ChildNodes[0]
someNode.lastChild===someNode.ChildNodes[someNode.ChildNodes.length-1]

someNode.hasChildNodes();//有一个或以上子节点则返回true
所有节点都具有的最后一个属性是ownerDocument,指向整个文档的文档节点

3. 操作节点

插入一个节点到末尾：
parentNode.appendChild(newNode);//向父节点的childNodes列表末尾添加一个节点
插入一个节点到某处：
parentNode.insertBefore(newNode,someNode);//向某个节点之前插入新节点
替换节点：
parentNode.replaceChild(newNode,someNode);//替换某处的节点为新节点
移除节点：
parentNode.removeChild(someNode);//移除某个节点

someNode.cloneNode();//true为深复制,false为浅复制

10.1.2 Document 类型
浏览器中document对象表示整个HTML页面
nodeType值为9
nodeName值为"#document"
nodeValue值为null
parentNode值为null
ownerDocument值为null

1. 文档子节点
documentElement属性,指向HTML页面中的<html>元素
即：
document.documentElement===document.childNodes[1];//true
body属性,指向body元素

所有浏览器都支持这两个属性

2. 文档信息

title属性,浏览器窗口的标题栏或标签页上的名称
URL属性,包含页面完整的URL
domain属性,只包含页面的域名
referrer属性,链接到当前页面的那个URL

3. 查找元素

document类型的两个方法
.getElementById();//返回的是单个元素
.getElementsByTagName();//返回的是与NodeList类似的动态集合

HTMLDocument类型才有的方法
.getElementsByName()

4. 特殊集合

document.forms等价于document.getElementsByTagName('form')
document.images等价于document.getElementsByTagName('img')
document.links等价于document.getElementsByTagName('a')

5. DOM一致性检测

document.implementation属性就是为此提供相应信息和功能的对象
DOM1级,规定一个方法

document.implementation.hasFeature()

6. 文档写入

write();//文档写入
writeln();//文档写入,末尾添加换行符 \n
open();//
close();//

10.1.3 Element 类型
nodeType值为1
nodeName值为元素标签名
nodeValue值为null
parentNode可能是document或Element

tagName和nodeName都返回标签名

HTML元素存在的标准特性
id--
title--
lang--
dir--
className--对应class

2. 取得特性(一般常见的特性,都能通过DOM元素本身的属性来访问)

.getAttribute();//可以返回自定义特性,返回的是字符串

所以开发中一般使用的都是对象的属性,只有在取得自定义特性值的情况下,才会使用getAttribute()方法

3. 设置特性

div.setAttribute('title','xxx')
亦可以直接给属性赋值来设置属性(不能添加自定义属性)
上述等价于
div.title ='xxx'
删除特性
div.removeAttribute('someAttr')

4. attributes属性
是一个属性的动态集合,然而太麻烦,不如上边的方法

5. 创建元素

document.createElement('tagName')方法创建新元素

var newDoc = document.createElement('div');
newDoc.innerText = "hello mimasang";
newDoc.style="width:100%;height:50px;background-color:#f5f5f5;background-image:url(http://tp3.sinaimg.cn/2488256110/50/22837397701/1);";
document.body.appendChild(newDoc);

6. 元素的子节点
注意包含空格文本节点
元素节点也有
.getElementsByTagName()

10.1.4 Text 类型

nodeType值为3
nodeName值为#text
nodeValue值为包含文本
parentNode是Element
没有子节点
可以通过nodeValue或data属性访问Text节点包含的文本

1. 创建文本节点
document.createTextNode()

string='xxx'
var myText = document.createTextNode(string);
var myDiv = document.createElement('div');
myDiv.appendChild(myText);
document.body.appendChild(myDiv);

父元素调用normalize()方法会合并两个或以上子文本元素

10.1.4 Comment类型

nodeType值为8
nodeName值为#comment
nodeValue值为注释内容
parentNode可能是Element或Document
没有子节点

10.1.6 CDATASection类型

nodeType值为4
nodeName值为#cdata-section
nodeValue值为CDATA区域中的内容
parentNode可能是Element或Document
没有子节点

10.2 DOM操作

动态加载外部脚本

	function loadScript(url){
		var script = document.createElement('script');
		script.type="text/javascript";
		script.src=url;
		script.text = 'function myFunc(){...}'
		document.body.appendChild(script);
	}
	loadScript('xxx.js');

动态加载外部样式
	
	functionloadStyles(url){
		var link = document.createElement('link');
		link.rel="stylesheet";
		link.type="text/css";
		link.href=url;
		var head = document.getElementByTagName('head')[0];
		head.appendChild(link);
	}
	loadStyles('xxx.css');

#11 DOM扩展

***
我觉得这道题特别具有说服力,也解决了我长久以来困扰的call,与apply的用法问题

	function every(collection, pre) {
	  // Is everyone being true?
	  return Array.prototype.every.call(collection,function(ele){
	    return !!ele[pre];
	  });
	}
	every函数判断collection数组里是不是每个值都有pre为属性的对象,是返回true,不是返回false.

***
#13 事件

事件就是用户或浏览器执行某种动作，例如click，load，mouseover之类，响应某个事件的函数就叫事件处理程序(事件侦听器)，事件处理程序的名字以‘on’开头。
<button onclick="func()"></button>
这种方式缺点：
1.耦合过于紧密
2.时差问题,点击时候可能事件处理程序不具备执行条件
3.作用域链在不同浏览器中会导致不同结果

DOM0级制定时间处理程序被认为是元素的方法
btn.onclick=function(){...};
btn.onclick=null;删除时间处理程序

DOM2级事件处理程序
btn.addEventListener('click',myfunc,false);
,可以添加多个事件处理程序
btn.removeEventListener('click',myfunc,false);
没法移除匿名函数

IE事件处理程序
btn.attachEvent('onclick',myfunc);
btn.detachEvent('onclick',myfunc);

跨浏览器事件处理程序

	var EventUtil = {
		addHandler:function(element,type,handler){
			if(element.addEventListener){
				element.addEventListener(type,handler,false);
			}else if(element.attachEvent){
				element.attachEvent('on'+type,handler);
			}
			else{
				element['on'+type] = handler;
			}
		},
		getEvent:function(event){
			return event?event:window.event;
		},
		getTarget:function(event){
			return event.target||event.srcElement;
		},
		preventDefault:function(event){
			if(event.preventDefault){
				event.preventDefault();
			}else{
				event.returnVlaue = false;
			}
		},
		removeHandler:function(element,type,handler){
			if(element.removeEventListener){
				element.removeEventListener(type,handler,false);
			}else if(element.detachEvent){
				element.detachEvent('on'+type,handler);
			}else{
				element['on'+type] = null;
			}
		},
		stopPropagation:function(event){
			if(event.stopPropagation){
				event.stopPropagation();
			}else{
				event.cancelBubble = true;
			}
		},
		getRelatedTarget:function(event){
			if(event.relatedTarget){
				return event.relatedTarget;
			}else if(event.toElement){
				return event.toElement;
			}else if(event.fromElement){
				return event.fromElement;
			}else{
				return null;
			}
		},
		getButton:function(event){
			if(document.implementation.hasFeature("MouseEvents","2.0")){
				return event.button;
			}else{
				switch(event.button){
					case 0:
					case 1:
					case 2:
					case 3:
					case 5:
					case 7:
						return 0;
					case 2:
					case 6:
						return 2;
					case 4:
						return 1;
				}
			}
		},
		getWheelDelta:function(event){
			if(event.wheelDelta){
				return (client.engine.opera&&client.engine.opera<9.5?
					-event.wheelDelta:event.wheelDelta);
			}else{
				return -event.detail * 40;
			}
		},
		getCharCode:function(event){
			if(typeof event.charCode == "number"){
				return event.charCode;
			}else{
				return event.keyCode;
			}
		},
		getClipboardText:function(event){
			var clipboardData = (event.clipboardData||window.clipboardData);
			return clipboardData.getData('text');
		},
		setClipboardText:function(event,value){
			if(event.clipboardData){
				return event.clipboardData.setData('text/plain',value);
			} else if(window.clipboardData){
				return window.clipboardData.setData('text',value);
			}
		}
	};

EventUtil.addHandler(btn,'click',handler);

EventUtil.removeHandler(btn,'click',handler);

事件对象

event对象的属性
preventDefault()阻止默认行为cancelable设置为true时,才能取消默认行为
stopPropagation()阻止冒泡
currentTarget正在处理事件的那个元素和this都是指向绑定事件处理器的元素
target事件目标
eventPhase表示当前位于事件流的哪个阶段，1为捕获阶段，2为处于目标对象上，3为冒泡阶段。2阶段时，this，target，currentTarget相等。
通过一个函数处理多个事件,利用type属性

IE中的事件对象,DOM0级添加事件处理程序时候,event作为window对象的一个属性存在
attachEvent添加的话,就会有一个event对象作为参数被传入时间内处理程序函数中。

事件属性
cancelBubble 默认为false,设置为true就能取消冒泡
returnValue 默认为true,设置为false取消世家默认行为
srcElement 事件的目标
type 被触发事件类型

跨浏览器事件对象

强化版的eventUtil

事件类型
UI事件,交互事件
焦点事件,获取/失去焦点
鼠标事件,
滚轮事件
文本事件,
键盘事件,
合成事件,
变动事件,
变动名称事件,

unload事件一般用于清除引用以避免内存泄漏

UI事件
1.load事件
加载完成后触发,图像上也可以触发load事件

2.unload事件
卸载后触发

3.resize事件
浏览器被调整高度或宽度时触发

4.scroll滚动事件

##焦点事件
主要是blur和focus,但他俩不会冒泡
focusin和focusout冒泡

##鼠标与滚轮事件

鼠标事件:
click
mousedown
mouseenter
mouseleave
mousemove
mouseout
mouseover
mouseup
只有mouseenter和mouseleave不会冒泡

滚轮事件:
mousewheel

视口中的位置
clientX
clientY
页面中的位置
pageX
pageY
页面没有滚动时候,这两者相等

pageX = document.body.scrollLeft+event.clientX
pageY = document.body.scrollLeft+event.clientY

屏幕坐标位置
screenX
screenY

移入和移出的相关事件
relatedTarget

	var EventUtil = {
		/..
		getRelatedTarget:function(event){
			if(event.relatedTarget){
				return event.relatedTarget;
			}else if(event.toElement){
				return event.toElement;
			}else if(event.fromElement){
				return event.fromElement;
			}else{
				return null;
			}
		}
		//..
	};

鼠标事件
对于mousedown和mouseup事件来说，其event对象存在一个button属性,表示释放或按下。
0表示左键
1中建
2右键
	var EventUtil = {
		/..
		getButton:function(event){
			if(document.implementation.hasFeature("MouseEvents","2.0")){
				return event.button;
			}else{
				switch(event.button){
					case 0:
					case 1:
					case 2:
					case 3:
					case 5:
					case 7:
						return 0;
					case 2:
					case 6:
						return 2;
					case 4:
						return 1;
				}
			}
		}
		//..
	};

鼠标滚轮事件

跨浏览器解决方案

	getWheelDelta:function(){
		if(event.wheelDelta){
			return (client.engine.opera&&client.engine.opera<9.5?
				-event.wheelDelta:event.wheelDelta);
		}else{
			return -event.detail * 40;
		}
	}

	(function(){
		function func(event){
			console.log(Event.getWheelDelta(EventUtil.getEvent(event)));
		}
		EventUtil.addHandler(document,"mousewheel",func);
		EventUtil.addHandler(document,"DOMMousewheel",func);
	}());

键盘事件
keydown
keypress
keyup

任何可以获得焦点的时间都能够触发keypress,keydown,keyup
只有编辑区才能触发textInput时间

获得字符编码

HTML 5 事件

1.contextmenu事件(鼠标右键上下文菜单)
$('div#div2').oncontextmenu = function(e){e.preventDefault()}

2.beforeunload事件，卸载之前弹出对话框问用户是否真的想卸载本页面。
window.onbeforeunload = function(e){
msg = "over?";
e.returnValue = msg
return msg;
}

3.DOMContentLoaded事件在形成完整的DOM树之后就会触发。
EventUtil.addhandler(document,"DOMContentLoaded",function(event){alert("Content loaded")});
不支持DOMContentLoaded的浏览器可以在页面加载期间设置一个0毫秒的超时调用
setTimeout(function(){//},0);

4.readystatechange事件
支持readystatechange事件的每个对象都有一个readyState属性

##内存和性能
每个函数都是对象,都会占用内存,内存中对象越多,性能就越差,范根DOM次数越多，整个页面的交互也就越差

事件委托
利用事件冒泡管理一类型的所有事件

移除事件处理程序

##模拟事件

模拟按键单击事件
var btn = document.getElementById('myBtn');

var event = document.createEvent('MouseEvents');

event.initMouseEvent('click',true,true,document.defaultView,0,0,0,0,0,false,false,false,false,0,null);

btn.dispatchEvent(event);

模拟键盘事件
var textbox = document.getElementById('xyTextbox');

if(document.implementation.hasFeature('KeyboardEvents','3.0')){
event = document.createEvent('KeyboardEvent');
event,initKeyboardEvent('keydown',true,true,document.defaultView,'a',0,"shift",0)
}
textbox.dispatchEvent(event);

IE中的事件模拟
var btn = document.getElementById('mybtn');

var event = document.createEventObject();

event.screenX = 100;
event.screenY = 0;
event.clientX = 0;
event.clientY = 0;
event.ctrlKey = false;
event.altKey = false;
event.shiftKey = false;
event.button = 0;
btn.fireEvent('onclick',event);

#14章 表单脚本

HTML中表单偶<form>元素表示，在JavaScript中对应的则是HTMLFormElement类型
HTMLFormElement也有它自己独有的属性和方法
acceptCharset
action
elements
length
method
name
reset()
submit()

取得form元素引用的方式有好几种，
var form = document.getElementsByTagName('form')[0]...
document.forms取得所有表单

提交表单

<input type="submit" value="submit form">
<button type="submit"></button>
<input type="image" src="xxx.gif">
上述右焦点的情况按下回车键就会提交表单

Event.addHandler(form,'submit',function(event){
//取得事件对象
event.EventUtil.getEvent(event);
//阻止默认事件
EventUtil.preventDefault(event);
})

JavaScript中调用submit也能提交表单
var form = document.getElementById('myForm');
form.submit();

重置表单
<input type="reset" value="reset form"/>
<button type="reset"></button>

表单字段
表单都有elements书，表示表单中所有元素的集合
var form=document.forms[0]
var field1 = form.elements[0]
var field2 = form.elements['textbox1'];//有可能返回的是NodeList

多次重复提交表单解决方案
EventUtil.addHandler(form,'submit',function(e){
e. = EventUtil.getEvent(e);
var target = EventUtil.getTarget(e);
var btn = target.elements['submit-btn'];
btn.disabled = true;
})

共有的表单字段方法
focus()和blur()

默认情况下，只有表单字段可以获得焦点，但是对于其他元素，如果将其tabIndex设置为-1，然后调用focus()方法，也可以让这些元素获得焦点。

设置文本框的值
var textbox = document.forms[0].elements['textbox1'];
textbox.value = "some new value";

选择文本

文本框获得焦点时，选择所有的文本，这是一种非常常见的做法，特别是文本框包含默认值的时候，免去了用户一个个的删除
EventUtil.addHandler(textbox,'focus',function(e){
e = EventUtil.getEvent(e);
var target = EventUtil.getTarget(e);
target.select();
})

也有一个select事件
选择文本框中文本时候，触发select事件
取得用户在文本框中选择的文本
	
	function getSelectText(tbox){
		return tbox.value.substring(tbox.selectionStart,tbox.selectionEnd);
	}

输入框屏蔽特定字符，检测keypress时间对应的字符编码，然后再决定如何响应

	屏蔽非数字值字符，但不会屏蔽触发keypress事件的基本按键
	EventUtil.addHandler(textbox,"keypress",function(event){
		event = EventUtil.getEvent(event);
		var target = EventUtil.getTarget(event);
		var charcode = EventUtil.getCharCode(event);
		if(!/\d/.test(String.fromCharCode(charCode))&&charCode>9&&!event.ctrlKey){
			EventUtil.preventDefault(event);
		}
	})

JavaScript动态添加选项
方法1：
var newOption = document.createElement("option");
newOption.appendChild(document.createTextNode('option text');
newOption.setAttribute('value','option value');
selectbox.appendChild(newOption);
方法2：
var newOption = new Option('option text','option value');
selectbox.appendChild(newOption);//IE8及之前版本有问题
方法3：
var newOption = new Option('Option text','Option value');
selectbox.add(newOption,undefined);

移除选项
selectbox.option[0]=null
selectbox.remove(0)

移动和重排选项
selectbox1.appendChild(selectbox.option[0]);

表单序列化

* 表单字段的名称和值进行URL编码，使用&分隔
* 不发送禁用表单字段
* 只发送勾选的单选框和复选框
* 不发送type为reset和button的按钮
* 多选选择框中每个选中值单独一个条目
* select元素的值是选中option的value的值，如果option没有value，则为option元素的文本值

	function serialize(form){
	var parts = [];
	field = null;
	i,
	len,
	optLen,
	option,
	optValue;
	for( i=0;len=form.elements.length;i<len;i++){
		field = form.elements[i];
		switch(field.type){
			case "select-one":
			case "select-multiple":
			if(field.name.length){
				for(j=0;optLen=field.options.length;j<optLen;j++){
					option = field.option[j];
					if(option.selected){
						optValue = "";
						if(option.hasAttribute){
							optValue = (option.hasAttribute('value')?
										option.value:option.text);
						}else{
							optValue = (option.attribute['value'].specifid?
										option.value:option.text);
						}
						parts.push(encodeURIComponent(field.name)+ "="+
							encodeURIComponent(optValue));
					}
				}
			}
			break;
			case undefined:
			case 'file':
			case "submit":
			case 'reset':
			case 'button':
				break;
			case 'radio':
			case 'checkbox':
				if(!field.checked){
					break;
				}
			default:
				if(field.name.length){
					parts.push(encodeURIComponent(field.name)+"="+
								encodeURIComponent(field.value));
				}			
			}
		}
		return parts.join('&');
	}

#错误处理

	try{
		//maybe error
	} catch(error){
		console.log(error.message);
	}

只要包含finally句子，无论try还是catch语句块中的return都将被忽略,

7中错误类型
Error
EvalError
RangeError
ReferenceError
SyntaxError
TypeError
URIError

Error是基本类型
EvalError是在eval()发生一场了时候抛出
RangeError值数值超出范围
ReferenceError找不到对象
SyntaxError语法错误
TypeError类型错误
URIError，URI格式不正确

throw new ReferenceError("this is a ReferenceError");

自定义错误

function customError(msg){
	this.name = "customError";
	this.message = msg;
}
customError.prototype = new Error();

throw new customError("this is a customError");

常见错误类型
类型转换错误
数据类型错误
通信错误

530
避免浏览器响应JavaScript错误的方法
- 可能发生错误的地方使用try-catch语句
- 使用window.error时间处理程序，可以接受try-catch不能处理的所有错误
- 明确什么是知名错误什么是非致命错误
- 判断最可能发生错误的地方
- 类型转换
- 未充分检测数据类型
- 发送给服务器或从服务器接收到的数据有错误

如果用DOM 0 级的2个方法赋值的事件监听函数不能在capturing阶段捕捉到事件

#JavaScript和XML

对于XML的XPath

#20章 JSON——一种结构化表示数据的格式

JSON可以表示三种类型的值
1. 简单值，可以表示字符串，数值，布尔值和null，但不支持undefined
字符串必须双引号
2. 对象，对象-有序的键值对
3. 数组

JSON.stringify()将JavaScript对象序列化为JSON字符串
JSON.parse()将JSON字符串解析为原生的JavaScript的值

JSON.stringify()传入的第二个参数可以是数组也可以是函数，传入函数的时候，会传入两个参数，属性名和属性值

JSON.stringify()第三个参数用于控制结果中的缩进和空白符

通过对象上调用toJSON()方法，返回其自身的JSON数据

#Ajax与Comet

创建XMLHttpRequest对象

	var xhr = new XMLHttpRequest();
	针对ie5,ie6
	var xmlhttp;
	if(window.XMLHttpRequest){
		xmlhttp = new XMLHttpRequest();
	}
	else{
		xmlhttp = new ActiveXObject('MicroSoft.XMLHTTP');
	}
	
XHR对象的方法
open方法
xhr.open('GET','xxx.php',false);//"GET"方法，发送到xxx.php，不使用异步
xhr.send();
发送同步请求之后，JavaScript代码会等到服务器响应之后在继续执行。
而受到响应之后，数据会自动填充XHR对象的属性
responseText：作为响应体被返回的文本
responseXML：作为响应体被返回的XML文档
status：响应的HTTP状态
statusText：HTTP状态的说明

发送异步请求
可以通过检测XHR对象的readyState属性来获得当前活动阶段
0未初始化
1启动，已经调用open方法
2发送已经调用send方法
3接受接收到部分数据
4已经接受到全部响应数据

readyState属性每变化一次，都会触发一次readystatechange事件，所以可以像下边这样写ajax

	var xhr;
	if(window.XMLHttpRequest){
		xhr = new XMLHttpRequest();
	}else{
		xhr = new ActiveXObject('Microsoft.XMLHTTP');
	}
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4){
			if(xhr.status >= 200&&xhr.status<300||xhr.status==304){
				alert(xhr.responseText);
			}else{
				alert("xhr.status: "+xhr.status);
			}
		}else{
			alert('xhr.readyState: '+xhr.readyState);
		}
	}
	xhr.open('GET','/');
	xhr.send(null);

HTTP头部信息
XHR对象的setRequestHeader方法能够设置发送ajax信息的HTTP头部信息

XHR对象的getResponseHeader()方法可以获得传入头部字段名称对应的信息
getAllResponseHeaders()方法获得全部头部信息

GET请求，通常用于获得和查询数据
而已将查询字符串最佳到URL末尾，但需要正确的编码才行，且所有的键值对都必须由&分隔。

	添加URL参数函数
	function addURLParam(url,name,value){
		url += (url.indexOf("?")==-1?"?":"&");
		url += encodeURIComponent(name) + "=" +encodeURIComponent(value);
		return url;
	}
	
POST请求，通常用于向服务器发送被保存的数据。POST请求可以包含非常多的数据，而且格式不限。

从性能的角度来看的话，发送相同的数据，GET请求的速度是POST两倍。

XMLHttpRequest 2 级别

FormData对象

var form = new FormData();
form.append('name','conan');
使用FormData的好处就是不用设置头部，XHR对象能够自动识别传入的数据类型是FormData

超时设定

给xhr的timeout属性设置一个值后，在规定时间内没有收到响应，就会触发timeout事件，进而调用ontimeout事件处理程序。

重写xhr响应的mime类型

xhr.overrideMimeType('text/xml');

##进度事件

6个进度事件
loadstart：接受到响应数据的第一个直接时触发
progress:在接收响应期间持续不断的触发
error：在请求发生错误时触发
abort：在因为调用abort()方法二总之连接时触发
load：在接收到完整的响应诗句触发
loadend：通信完成，或者触发error，abort，load后触发

每个请求都是以loadstart事件开始，然后是一个或多个progress事件，然后触发error，abort或load事件中的一个，最后触发loadend事件。

创建一个进度指示器的实例

	function createXHR(){
		var xhr;
		if(window.XMLHttpRequest){
			xhr = new XMLHttpRequest();
		}else{
			xhr = new ActiveXObject('Microsoft.XMLHTTP');
		}
		return xhr;
	}
	var xhr = createXHR();
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4){
			if(xhr.status == 200){
				console.log(xhr.status+" "+xhr.statusText);
				console.log('xhr.readyState: '+xhr.readyState);
			}
		}
	}
	var bar = document.createElement('div');
		bar.style.width = "200px";
		bar.style.height = "5px";
		bar.style.position = 'absolute';
		bar.style.top = "200px";
		bar.style.left = "200px";
		bar.style.backgroundColor = "red";
		bar.id ="bar";
		document.body.appendChild(bar);
	xhr.onprogress = function (event){
		var bar = document.getElementById('bar');
		if(event.lengthComputable){
			bar.width =bar.width*(event.position/event.totalSize);
		}
	}
	xhr.open('GET','/');
	xhr.send(null);

跨域CORS（cross-origin-resources sharing，跨资源共享）。
CORS背后的基本思想，就是使用自定义的HTTP头部让浏览器与服务器进行沟通，从而决定请求或相应应该成功，还是应该失败。

发送请求的时候，添加一个origin头部
Origin:http://www.conans.top
如果服务器认为这个请求可以接受
Access-Control-Allow-Origin:http://www.conans.top
请求和响应都不包含cookie信息

IE对CROS的实现

	var xdr = new XDomainRequest();
	xdr.onload = function(){
		alert(xdr.responseText);
	}
	xdr.onerror = function (){
		alert("an error occurred");
	};
	xdr.timeout = 1000;
	xdr.ontimeout = function(){
		alert("request timeout")
	}
	xdr.open('get','/');
	xdr.send(null);

jsonp原理，通过script标签引入js文件，这个js文件载入成功后会执行我们在url参数中制定的函数，并且回吧我们需要的json数据作为参数传入

jquery方便的进行jsonp操作

$.getJSON('http://conans.top?callback=?',function(json){console.log(json)})


	function locator(json){
		console.log("your ip address is : "+json.ip+"\n"+"city: "+json.city+"\n"+json.region_name)
	}
	var script = document.createElement('script');
	script.src = "http://freegeoip.net/json/?callback=locator";
	document.body.insertBefore(script,document.body.firstChild);

#22章 高级技巧

1. 高级函数
安全类型检测

	function isArray(value){
		return Object.prototype.toString.call(value) == "[object Array]";
	}
	function isFunction(value){
		return Object.prototype.toString.call(value) == "[object RegExp]";
	}
	function isRegExp(value){
		return Object.prototype.toString.call(value) == "[object RegExp]";
	}

惰性载入，结束老是重复if判断语句的方法

1. 函数被调用时候再处理函数。
2. 申明函数的时候就制定适当的函数。

函数绑定

	function bind(fn,context){
		return function(){
			return fn.apply(context,arguments);
		};
	}

函数科里化，函数模块化，常见于预先设定参数,一般通过闭包，绑定call和apply

创建科里化函数的通用方式

	function curry(fn){
		var args = Array.prototype.slice.call(arguments,1);
		console.log(args);
		return function (){
			var innerArgs = Array.prototype.slice.call(arguments);
			console.log(innerArgs);
			var finalArgs = args.concat(innerArgs);
			console.log(finalArgs);
			return fn.apply(null,finalArgs);
		};
	}
	
	function add(num1,num2){
		return num1+num2;
	}
	curriedAdd = curry(add,5,12);//22

对象防篡改

1. 不可扩展
Object.preventExtensions(obj);
之后便不能添加新的属性和方法了.
Object.isExtensible(obj);
检测对象是否可扩展

2. 密封对象
Object.seal(obj);
不能删除或增加属性或方法了
Object.isSealed()方法能够确定对象是否被密封

3. 冻结对象
Object.freeze(obj);
不可扩展，又是密封，writable属性又会被设置为false
但是定义[[set]]函数，访问器属性仍然是可写的。
Object.isFrozen()判断对象是否被冻结

JavaScript定时器时间间隔表示何时将定时器的代码添加到队列，而不是何时实际执行代码

##JavaScript的strict模式

- 所有变量都必须var申明
- 禁止使用with改变作用域
- 创建eval作用域
- 禁止this指向全局作用域
- 禁止caller与arguments
- 禁止删除变量
- 删除修改不可变对象的属性时，显示报错
- 对象不能有重名属性,函数不能有重名参数
- 禁止8进制表示法
- 禁止使用arguments.callee即无法在匿名函数内部调用自身了
- 等

判断一个值是否是NaN

	function IsNaN(value){
		return typeof(value)==='number'&&isNaN(value);
	}

	function IsNaN(){
		return value!=value;
	}

parseInt的返回值只可能两种，十进制整数，或者NaN

Base64转码

btoa()

	function BaseEncode(a){
		return btoa(encodeURIComponent(a))
	}

	function BaseDecode(a){
		return decodeURIComponent(atob(a))
	}
	
函数执行时所在的作用域，是定义时的作用域，而不是调用时所在的作用域。

将arguments转换为真正的数组
方法1
	var args = Array.prototype.slice.call(arguments);
	
	var args = [];
	for(var a=0;a<arguments.length;a++){
		args.push(arguments[a]);
	}

自定义错误类型

	function MyError(msg){
	this.message = msg||'MyError default msg';
	this.name = "MyError";
	}
	MyError.prototype = new Error();
	MyError.prototype.constructor = MyError;

console的assert方法接受两个参数,第一个是表达式,第二个是表达式不为真弹出的对象

	var count = 0;
	function countUp(){
		try{
			return count;
		}finally{
			count++;
		}
	}
	countUp();//0
	count;//1

return语句执行在前，
但是显示在finally显示之后

	function f() {
	  try {
	    console.log(0);
	    throw 'bug';
	  } catch(e) {
	    console.log(1);
	    return true; // 这句原本会延迟到finally代码块结束再执行
	    console.log(2); // 不会运行
	  } finally {
	    console.log(3);
	    return false; // 这句会覆盖掉前面那句return
	    console.log(4); // 不会运行
	  }
	
	  console.log(5); // 不会运行
	}
	
	var result = f();
	// 0
	// 1
	// 3
	
	result
	// false

随机数生成
	//返回随机数[min,max)
	function randNum(min,max){
		return Math.random()*(max-min)+min;
	}
	//返回随机数[min,max]
	function randInt(min,max){
		return Math.floor(Math.random()*(max-min+1))+min;
	}
	//返回随机字符
	function randomStr(length){
		var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		alphabet+="abcdefghijklmnopqrstuvwxyz";
		alphabet+="0123456789-_";
		var str = "";
		for(var a=0;a<length;a++){
			var rand = Math.floor(Math.random()*alphabet.length);
			str += alphabet.substring(rand,rand+1);
		}
		return str;
	}
	randomStr(12);

[^]包含一切字符
\d，0-9之间数字[0-9]
\D，0-9之间数字之外[^0-9]
\w，任意数字字母下划线[A-Za-z0-9_]
\W，任意非数字字母下划线[^A-Za-z0-9_]
\s，空格，包括制表、空格、断行[\t\r\n\v\f]
\S，非空格[^\t\r\n\v\f]
\b，匹配词边界，边界没有数字字母相连接
\B，非边界

	/\bworld/.test('hello-world') // true
	/\bworld/.test('hello2world') // false

	// 正常匹配
	var url = /(http|ftp):\/\/([^/\r\n]+)(\/[^\r\n]*)?/;
	
	url.exec('http://google.com/');
	// ["http://google.com/", "http", "google.com", "/"]
	
	// 非捕获组匹配
	var url = /(?:http|ftp):\/\/([^/\r\n]+)(\/[^\r\n]*)?/;
	
	url.exec('http://google.com/');
	// ["http://google.com/", "google.com", "/"]

console.assert(exp,args);//exp成立时，输出args参数

命令行api
$(selector);//返回一个数组,实际上就是document.querySelectorAll()
$()==$$()
$x(xpath);//返回一个数组包含XPath表达式的所有DOM元素

Object.defineProperty(obj,ele,{xx:xx});//默认writable,enumerable,configurable都为false.
writable为false，不可写
enumerable为false,不可遍历,属性不出现在for...in和Object.keys(),和JSON.stringify()方法中,但是in可以描述
Object.getOwnPropertyNames()方法返回自身所有属性,包括不可枚举属性
configurable为false,不可重新定义所有属性也不可delete属性,但writable可以有true改为false
对于value,只要writable和configurable有一个为true,就允许改动

值得一提的是var申明的变量configurable默认为false
var a = 6;
JSON.stringify(Object.getOwnPropertyDescriptor(window,'a'),null,2);
"{
  "value": 6,
  "writable": true,
  "enumerable": true,
  "configurable": false
}"
//可重写，可遍历不可删除
writable为false则不可以被重写,

一般情况，系统原生的属性都是不可枚举的
所以
Object.keys(Object);//[]
Object.keys(Object.prototype);//[]
Object.keys([]);//[]

Object.getOwnPropertyNames(Object.prototype);
// ['hasOwnProperty',
//  'valueOf',
//  'constructor',
//  'toLocaleString',
//  'isPrototypeOf',
//  'propertyIsEnumerable',
//  'toString']

存读函数:
setter---set
getter---get
1.直接通过定义对象的时候定义
	var o = {
		get g(){
			return 'getter';
		},
		set g(value){
			return 'setter'+value;
		}
	}
2.通过Object.defineProperty()定义
	var o = {};
	Object.defineProperty(o,'year',{
		get:function(){
			return new Date().getFullYear();
		},
		set:function(v){
			return new Date(v).getFullYear();
		}
	})

利用存取器,实现数据对象与DOM对象的双向绑定
	Object.defineProperty(user,'name',{
		get:function(){
			return document.getElementById('foo').value;
		},
		set:function(newValue){
			document.getElementById('foo').value = newValue;
		},
		configurable:true
	});

#OOP
构造函数的三个特点
函数体内部使用了this关键字
生成对象的时候,必须调用new
构造函数名第一个字母大写(不是强制)

可以在构造函数内部第一行加上'use strict'，this将指向undefined

new命令原理

1.创建一个空对象
2.将这个空对象的原型指向构造函数的prototype属性
3.将空对象赋值给函数内部的this对象
4.返回this对象

如果构造函数内部有return语句，且返回的是对象，那就返回这个对象，
如果没有，就返回this对象。

new命令总是返回一个对象,要么是实例对象,要么是return语句返回的对象

##this关键字
总是返回一个对象,当前属性或方法所在的对象
this会随着环境的切换而切换

1.全局环境this指向顶层对象
浏览器中就是window
nodejs中就全局指向global,模块指向module.exports
2.构造函数中的this指向调用属性/方法的对象
3.将对象的方法赋值给另一个对象的时候，this会指向最终对象
	看3个例子
	1.
	var o = {
		a:'alooo',
		b:'xixixi',
		f:function(){
			console.log(this)
		}
	}
	o.f();//Object {a: "alooo", b: "xixixi", f: function}

	2.
	var o = {
		a:'ooo',
		b:'xixixi',
		f:function(){
			return Array.prototype.map.call(this.b,function(ele,idx,arr){
		'use strict'
		return this.a+ele;
	}).join('');
		}
	}
	o.f();//TypeError Cannot read property of undefined

	3.
	var o = {
		a:'ooo',
		b:'xixixi',
		f:function(){
			that = this;
			return Array.prototype.map.call(this.b,function(ele,idx,arr){
		'use strict'
		return that.a+ele;
	}).join('');
		}
	}
	o.f();//"oooxoooioooxoooioooxoooi"

绑定this的方法

Function.prototype.call()方法
call方法传入的应该是一个对象,如果参数空,null,undefined，默认为全局对象
Function.prototype.call(obj,arg1,arg2,....)
第一个为要绑定this的对象，后边的是函数调用时候需要的参数

Function.prototype.apply()方法
与call唯一区别就是后边的参数跟数组
Function.prototype.apply(obj,[arg1,agr2,...])

function f(x,y){
  console.log('x: '+x)
  console.log('y: '+y)
  console.log('x+y: '+x+y);
}
f.call(null,[1,1])
//x: 1,1
//y: undefined
//x+y: 1,1undefined

bind方法用于将函数体内的this绑定到某个对象，然后返回一个新函数

	var add = function (x, y) {
	  console.log(x);
	  console.log(this.m);
	  console.log(y);
	  console.log(this.n);
	  return x + this.m + y + this.n;
	}
	var obj = {
	  m: 2,
	  n: 2
	};
	var newAdd = add.call(obj, 5);
	newAdd();
	//5
	//2
	//undefined
	//2

	var add = function (x, y) {
	  console.log(x);
	  console.log(this.m);
	  console.log(y);
	  console.log(this.n);
	  return x + this.m + y + this.n;
	}
	var obj = {
	  m: 2,
	  n: 2
	};
	var newAdd = add.bind(obj, 5);
	newAdd(9);//18
	//5
	//2
	//9
	//2

band的polyfill

	if(!('band' in Function.prototype)){
		Function.prototype.bind = function(){
			var fn = this;
			var context = arguments[0];
			var args = Array.prototype.slice.call(arguments,1);
			return function(){
				return fn.apply(context,args);
			}
		}	
	}
















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































