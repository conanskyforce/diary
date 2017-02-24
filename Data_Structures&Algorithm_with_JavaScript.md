
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

















































































































































































































































































































































