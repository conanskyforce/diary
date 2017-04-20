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
3. 






















































































































































































































































































































