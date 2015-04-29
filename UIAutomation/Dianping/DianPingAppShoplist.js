
var target = UIATarget.localTarget();

//target.logElementTree();
//通过logElementTree查到“美食”是target.frontMostApp().mainWindow().UIATableView()[0].UIATableCell()[0].UIAButton()-rect{{11,64},{88,87}}，没有name
target.tap({x:40, y:90})
target.delay(2);

var app = target.frontMostApp(); 
var window = app.mainWindow(); 
window.buttons()["附近"].tap();
target.delay(1);

//筛选区域为长宁区-中山公园
window.tableViews()[1].cells()["长宁区"].tap();
target.delay(1);
window.tableViews()[2].cells()["中山公园"].tap();
target.delay(1);
//target.logElementTree();