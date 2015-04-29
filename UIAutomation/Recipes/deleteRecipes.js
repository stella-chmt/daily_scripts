
var target = UIATarget.localTarget(); 
//target.logElementTree();

var app = target.frontMostApp(); 
var window = app.mainWindow(); 
var navigationBar = window.navigationBar(); 

oldCellsLength = window.tableViews()[0].cells().length;

//用editButtion删一条
//得到name为Edit的UIAButton对象
var editButton = navigationBar.buttons()["Edit"]; 
editButton.tap(); //触发点击操作

target.delay(1);

//window.logElementTree();
//通过这个发现原来，window这个变量会自动随着UIATarget.localTarget().frontMostApp().mainWindow()指向的真正window变化
//删掉最后一条记录
window.tableViews()[0].cells()[oldCellsLength - 1].buttons()[0].tap();
window.tableViews()[0].cells()[oldCellsLength - 1].buttons()[1].tap();
//window.logElementTree();
//navigationBar.buttons()["Done"].tap();
navigationBar.leftButton().tap(); //和上一句作用相同，一般navigationBar都有leftButton和rightButton，分布左右两侧，除非不是标准的navigationBar的leftItem，否则一般都能生效

target.delay(1);

newCellsLength = window.tableViews()[0].cells().length;

if(oldCellsLength == newCellsLength + 1)
{
    UIALogger.logPass("using edit button to delete test passed");
}
else
{
    UIALogger.logFail("using edit button to delete test failed");
}

//以下为录制的，点击Edit，点击最下面那个item左侧删除按钮，然后点击右侧出现的“delete”按钮，最后点击左上角的“Done”按钮
//target.frontMostApp().navigationBar().buttons()["Edit"].tap();
//target.frontMostApp().mainWindow().tableViews()[0].tapWithOptions({tapOffset:{x:0.07, y:0.62}});
//target.frontMostApp().mainWindow().tableViews()[0].cells()["Three Berry Cobbler"].tap();
//target.frontMostApp().navigationBar().buttons()["Done"].tap();


//-----------------------------------------------------------------------------------
//通过滑动删一条,dragInsideWithOptions不好使
//window.tableViews()[0].cells()[newCellsLength - 1].dragInsideWithOptions({startOffset:{x:0.8, y:0.8}, endOffset:{x:0.2, y:0.8}, duration:2});

//window.logElementTree();

//以下为录制的，滑动"Three Berry Cobbler"那条，露出右侧“delete”按钮，然后点击navigationBar里的“Done”
//target.frontMostApp().mainWindow().tableViews()[0].dragInsideWithOptions({startOffset:{x:0.85, y:0.62}, endOffset:{x:0.11, y:0.63}, duration:1.2});
//target.frontMostApp().navigationBar().leftButton().tap();


