#CSS布局解决方案
<pre>
写在前边，顺便也将之前学的markdown复习与巩固一下
1.标题
# 一级标题
## 二级标题
### 三级标题
2.列表
* 无序列表
1 有序列表
3.引用
> 我是引用
4.图片与链接
![]() 图片链接
[]() 普通链接
5.粗体与斜体
*内容* 斜体
**内容** 粗体
6.代码 
`...` 包含
7.分割线
*** 
8.那就是html的很多标签md都能用哦！！ 
</pre>
##布局居中
###水平居中
		背景：
		<div class="parent">
			<div class="child">CHILD</div>
		</div>
>1. inline-block+text-align  
>子元素设置<code>display: inline-block</code> ,宽度将随着内容的变化而变化  
>父元素设置text-align  
>这种方式兼容性好,但是影响后代元素.  
2. table + margin  
>子元素设置display:table
>子元素设置margin: 0 auto;  
3. abosolute + transform;  
>父元素设置position:relative;
>子元素设置position:absolute;
>子元素设置top:50%;
>子元素设置transform:translateY(-50%);
>缺点在于兼容性吧
4. flex + justify-content  
>父元素display:flex;justifyy-content:center;
>或者子元素margin:0 auto;
###垂直居中  
>1. table-cell+vertical-align  
>display:table-cell;转换为单元格,再对子元素垂直对齐  
2. absolute + transform
>父元素position:relative;
>子元素position:absolute;
>子元素top:50%;transform:translateY(-50%);  
3. flex + align-items
>只需要设置父元素display:flex;align-items:center;
###水平垂直都居中
1. inline-block + text-align + table-cell + vertical-align

		.parent{
			text-align:center;
			display:table-cell;
			vertical-align:middle;
		}
		.child{
			display:inline-block;
		}
2. absolute + transform

		.parent{
			postion:relative;
		}
		.child{
			position:absolute;
			top:50%;
			left:50%
			transform:translate(-50%,-50%);
		}
3. flex + justify-content + align-items

		.parent{
			display:flex;
			justify-content:center;
			slign-items:center;
		}
##多列布局
1. 定宽+自适应  

		.left{
		    float: left;
		    width: 100px;
		}
		.right{
		    margin-left: 120px;
		}
2. 等分布局

		.parent{
		    margin-left: -20px;
		}
		.column{
		    float: left;
		    width: 25%;
		    padding-left: 20px;
		    box-sizing: border-box;
		}
##响应式布局
		<meta name="viewport" content="width=device-width,initial-scale=1.0,user-scalable=no" />
		@media screen and (min-width:360px) and (miax-width:768px) {
		//styles
		}
**Q&A**  
为什么要优化页面  
1.提升网页响应速度  
2.增强可阅读性与可维护性  
3.对搜索引擎，阅读器友好  
如何优化   

<ul>
	<li>减少请求
	<ul>
		<li>图片合并</li>
		<li>CSS文件合并，减少css内联样式</li>
		<li>避免import方式引入css文件</li>
	</ul>
	</li>
	<li>减小文件大小
	<ul>
		<li>选择合适的图片格式</li>
		<li>png(小图标)</li>
		<li>jpg(大图,色彩丰富)</li>
		<li>代码压缩工具</li>
		<li>css值缩写</li>
	</ul>	
	</li>
	<li>页面性能
	<ul>
		<li>加载顺序，css在head，js在底部</li>
		<li>减少标签数量</li>
		<li>避免需要消耗性能的属性，filter，border-radius，gradients</li>
		<li>图片设置宽高，房子重绘</li>
	</ul>	
	</li>
	<li>可读写，可维护性
	<ul>
		<li>开发之前定好规范，多人协助时，更加方便</li>
		<li>语义化，对seo，阅读器更加友好</li>
		<li>尽量避免hack，hack尽量统一</li>
		<li>模块化</li>
		<li>注释</li>
	</ul>
	</li>
</ul>










































































































































































































































































































