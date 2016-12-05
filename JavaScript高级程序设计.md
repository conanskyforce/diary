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
instanceof能够区分null和Object，
Array.isArray()能够判断是不是数组

if和for循环中定义的变量没有块级作用域
访问局部变量比访问全局变量要快，不用沿着作用链一直向上找，节省时间











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











