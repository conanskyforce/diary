#webpack教程


npm init;//初始化一个package.json配置环境文件
npm install -g webpack --save-dev;//安装webpack并将其保存在开发环境依赖
webpack aim.js aim.bundle.js ;//将aim.js 打包为aim.bundle.js文件

npm install css-loader style-loader --save-dev;//安装css与style loader

webpack.config.js;//webpack配置文件

module.exports = {
	entry:__dirname+'app/main.js',
	output:{
		path:'./dist/js',
		filename: 'bundle.js'
	}
}

package.json;//配置文件script 配置webpack运行时候的参数
...
"script":{
	"test":"...",
	"webpack":"webpack --progress --display-module --colors --display-reason"
}
...
