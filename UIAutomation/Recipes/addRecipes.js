
//树的根，UIATarget对象
var target = UIATarget.localTarget(); 
target.logElementTree();
//返回一个UIAApplication对象，可以理解为整个app
var app = target.frontMostApp(); 
//一个UIAWindow对象，当前窗口对象（app运行时会有多个显示页面/窗口）
var window = app.mainWindow(); 
//var window = app.windows()[1]; //这个的作用同上一句
//得到name为Recipes的navigationBar对象（window的navigationBar对象同样可以有多个，所以window.navigationBars()得到的是一个数组）
//var navigationBar = window.navigationBars()["Recipes"]; 
var navigationBar = window.navigationBar(); //这个的作用同上一句,因为一般一个window只会有一个navigationBar

oldCellsLength = window.tableViews()[0].cells().length;


//用Add按钮加一条
navigationBar.buttons()["Add"].tap();
window.textFields()[0].setValue("包子");
window.navigationBar().buttons()["Save"].tap();
target.delay(1);
window.navigationBar().buttons()["Recipes"].tap();

newCellsLength = window.tableViews()[0].cells().length;

if (newCellsLength == oldCellsLength + 1)
{
    UIALogger.logPass("add test passed!");
}
else
{
    UIALogger.logFail("add test failed!");
}

