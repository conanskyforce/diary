
##什么是栈(Stack)
栈是一种特殊的结构,栈内的元素只能通过列表的一端访问,这一端成为栈顶。
类似于叠好的盘子,只能从上边取,加也只能从上边加,这又被成为‘后入先出’(LIFO,lsat in first out)

入栈使用push()方法,出栈使用pop()方法
pop()可以访问栈顶元素,但是调用该方法时,栈顶元素也被从栈里永久性的删除了,peek()方法则只返回栈顶元素,而不删除它

变量top来描述当向栈内压入元素,top增大,从栈内弹出元素,变量减小

push(),pop(),peek()是栈的3个主要方法,clear()方法清除栈内所有元素。
length属性记录栈内元素个数
empty属性表示栈内是否含有元素

用JavaScript模拟一个Stack类

	function Stack(){
		this.dataStore = [];
		this.top = 0;
		this.push = push;
		this.pop = pop;
		this.peek = peek;
		this.clear = clear;
		this.length = length;
	}

	function push(element){
		this.dataStore[this.top++] =element;
	}
	function pop(){
		return this.dataStore[--this.top];
	}
	function peek(){
		return this.dataStore[this.top-1];
	}
	function clear(){
		this.top = 0;
	}
	function length(){
		return this.top;
	}

##使用Stack类

将一个数字转换为指定数制

	function tranBase(num,base){
		var s = new Stack();
		do{
			s.push(num%base);
			num = Math.floor(num/=base);
		} while(num>0);
		var converted = '';
		while(s.length()>0){
			converted+=s.pop();
		}
		return converted;
	}
	tranBase(75,2);

判断是否是回文

	function isPalindrome(word){
		var s = new Stack();
		for(var i=0;i<word.length;++i){
			s.push(word[i])
		}
		var nword = '';
		while(s.length()>0){
			nword+=s.pop();
		}
		if(word==nword){
			return true;
		}else{
			return false;
		}
	}

栈模拟递归

	function fact(n){
		var s = new Stack();
		while(n>1){
			s.push(n--);
		};
		var res = 1;
		while(s.length()>0){
			res*=s.pop();
		};
		return res;
	}

#队列
队列是一种先进先出的数据结构(FIFO，first-in-first-out)，它被用在很多地方，比如提交操作系统执行的一系列进程，打印任务池，等一些模拟排队的情况。

队列的操作，
入队，排在最后
出对，排在最前面的最先出

数组模拟队列

	function Queue(){
		this.dataStore = [];
		this.enqueue = enqueue;
		this.dequeue = dequeue;
		this.front = front;
		this.back = back;
		this.toString = toString;
		this.empty = empty;
	}
//向队尾添加一个元素

	function enqueue(element){
		this.dataStore.push(element);
	}
//删除队首的元素

	function dequeue(){
		return this.dataStore.pop();
	}
//读取队首和队尾的元素

	function front(){
		return this.dataStore[0];
	}
	function back(){
		return this.dataStore[this.dataStore.length-1];
	}
//显示队列所有元素

	function toString(){
		var allEle = '';
		for(var i=0;i<this.dataStore.length;i++){
			allEle+=this.dataStore[i]+'\n';
		}
		return allEle;
	}
//判断队列是否为空

	function empty(){
		if(this.dataStore.length==0){
			return false;
		}
		else{
			return true;
		}
	}

优先队列

	function Patient(name,code){
		this.name = name;
		this.code = code;
	}
	function dequeue(){
		var pri = this.dataStore[0].code;
		for(var i=1;i<this.dataStore.length;++i){
			if(this.dataStore[i].code<pri){
				pri=1;
			}
		}
		return this.dataStore.splice(pri,1);
	}
	function toString(){
		var res = "";
		for(var i=0;i<this.dataStore.length;i++){
			res += this.dataStore[i].name+" code:"
				+ this.dataStore[i].code+'\n';
		}
		return res;
	}

##链表

JavaScript中数组的主要问题就是他们被实现为了对象，从而效率很低

P98

***
二叉树

实现二叉查找树(BST)






































































































































































































































































































































