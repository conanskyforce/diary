时隔半月，再次翻开了有JavaScript圣经之称的JavaScript高级程序设计，转眼已过2016,2017又是一个新的开始，纵使寒风起，人生不言弃。

'user strict';开启严格模式
申明变量一定要用var，切记切记！！
JavaScript一共只有六种数据类型
Null
Undefined
Boolean
String
Number
Object--包括Array，Function，object，Null

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
- string.replace(/sda/g,'xfa')将所有匹配到的项，替换为'xfa',第二个参数也可以是个函数
- 



























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































