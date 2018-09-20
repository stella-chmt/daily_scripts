###1.chromedriver unknown error: Runtime.executionContextCreated has invalid 'context'    
**原因**：chrome版本和chromedriver版本不兼容    
**解决方法**：[chromedriver下载地址](http://chromedriver.storage.googleapis.com/index.html)     
去下载和chrome兼容的版本，chromedriver和chrome的配套关系在下载目录的ntoes.txt中查看。下载完成后，解压文件，然后把它放到/usr/bin/下就可以了    
**注意**：最好之后禁用chrome的自动更新，参考[文章](https://blog.csdn.net/chenyufeng1991/article/details/78568919)    

###2.无法将chromedriver放置到/usr/bin/目录Operation not permitted    
**原因**：El Capitan 加入了Rootless机制，不再能够随心所欲的读写很多路径    
**解决方法**：关闭 Rootless        
重启按住 Command+R，进入恢复模式，点击显示器最上面实用工具菜单下的终端，打开Terminal。    
输入    
   csrutil disable  #关闭     
再重启电脑    
