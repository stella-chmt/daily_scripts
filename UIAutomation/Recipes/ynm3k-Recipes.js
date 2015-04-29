

#import "../tuneup_js/tuneup.js"
#import "../ynm3k/robot4ios/importAll.js"

var target = UIATarget.localTarget(); 
var app = target.frontMostApp(); 

test("增加一个菜单，通过判断总菜单数量变化来判断测试是否成功", function(target, app){       
          
     oldCellsLength = Finder.findElementsByClassType("TableCell").length;
     
     
     //用Add按钮加一条
     Finder.findElementsByName("Add").tap();
     Finder.findElementByValue("Recipe Name").setValue("包子");
     Finder.findElementsByName("Save").tap();
     target.delay(1);
     Finder.findElementsByNameAndClassType("Recipes","Button").tap();
     
     newCellsLength = Finder.findElementsByClassType("TableCell").length;
     
     assertEquals(newCellsLength, oldCellsLength+1);
     
     });

test("删除最后一个菜单，通过判断总菜单数量的变化来判断测试是否成功", function(target, app){
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
     
     assertEquals(newCellsLength, oldCellsLength-1);
     });



