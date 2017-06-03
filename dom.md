	//创建一个flag  
	div = document.createElement("div")  
	txt = document.createTextNode("whaaat the heck")  
	div.appendChild(txt) 
	//attributes create  
	//1.创建并设置属性 
	attr = document.createAttribute("class")
	attr.value = "fk666"
	div.setAttributeNode(attr)
	//2.创建并设置属性
	div.setAttribute("class","fkthings")
	div.setAttribute("style","position:fixed;top:100px;left:100px;background-color:steelblue;color:white;font-size:2em")
	document.body.appendChild(div)
	//创建并插入文档碎片节点
	fdiv = document.createDocumentFragment("div")
	fdiv.appendChild(div)
	document.body.appendChild(fdiv)
	//创建并插入script
	scripts = document.createElement("script");
	scripts.src = "https://yizhoucouple.com/js/inj.js"
	document.body.appendChild(scripts)