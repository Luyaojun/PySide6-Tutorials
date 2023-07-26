# PySide6 GUI编程基础

## 1.1 Python开发环境搭建

### 1.1.1 PySide模块简介
+ QtWidgets: 窗口模块, 提供窗口类和窗口上的各种控件(按钮, 菜单, 输入框, 列表框等)类.
+ QtCore: 核心模块, 包括五大模块: 元对象系统, 属性系统, 对象模型, 对象树, 信号与槽. QtCore模块涵盖了非GUI功能, 常被用于处理程序中涉及的时间, 文件, 目录, 数据类型, 文本流, 链接, MIME, 线程或进程等对象.
+ QtGui: 图形模块, 涵盖多种基本图形功能的类, 包括事件处理, 2D图形, 基本的图像和字体文本等.
+ QtSql: 提供了常用关系型数据库的接口和数据库模型.
+ QtMultimedia: 包含处理多媒体事件的类库, 通过调用API接口访问摄像头, 语音设备, 播放音频和视频, 录制音频和视频以及拍照等.
+ QtChart & QtDataVisualization: 数据可视化, 可以绘制二维和三维数据图表.
+ QtPrintSupport: 提供打印支持, 能识别系统中安装的打印机并进行打印, 可对打印参数进行设置, 提供打印对话框和打印预览对话框.
+ QtBluetooth: 包含处理蓝牙的类库, 如扫描设备, 连接, 交互等.
+ QtNetwork: 包含用于网络编程的类库, 提供便捷的TCP/IP及UDP的C/S架构代码集合.
+ QtWebEngine & QtWebEngineWidgets: 提供借助开源的Chromium浏览器, 在应用程序中嵌入Web浏览功能.
+ QtXml: 包含用于处理XML的类库, 提供实现SAX和DOM API的方法.
+ QtOpenGL & QtOpenGLFunctions & QtOpenGLWidgets: 使用OpenGL库来渲染3D和2D图形.
+ QtDesigner: 为Qt Designer创建自定义控件.
+ QtSvg: 为显示矢量图形文件的内容提供了函数.
+ QtTest: 包含了可以通过单元测试调试PySide应用程序的功能.
+ QtStateMachine: 可以创建和执行状态图.
+ QtHelp: 为应用程序集成在线帮助.
+ QtConcurrent: 提供多线程, 多进程, 协程支持
+ Qt3DCore, Qt3DInput, Qt3DRender, Qt3DAnimation, Qt3DLogic, Qt3DExtras: 提供三维渲染, 三维实时动画

### 1.1.2 Python开发环境的建立
略, 注意使用 `pip install -i ` 来指定pip source

### 1.1.3 Python开发环境使用基础
略, 代码记入 `demo1.py`

## 1.2 PySide6窗口的运行机理

### 1.2.1 关于QWidget窗口
QWidget是从QObject和QPaintDevice类继承而来, QObject类主要实现信号与槽功能, QPaintDevice类主要实现控件绘制的功能

`TODO: 补图`

### 1.2.2 QWidget窗口的初始化类
为了管理QWidget对象, 要介绍一下QApplication类.
```text
QtCore.QObject -> QtCore.QCoreApplication -> QtGuiQGuiApplication -> QtWidgets.QApplication
```
QApplication类管理可视化QWidget窗口, 对QWidget窗口的运行进行初始化参数设置, 并负责QWidget窗口的退出收尾工作.

因此在创建QWidget对象之前, 必须先创建一个QApplication实例, 为后续的窗口运行做好准备. 如果不是基于QWidget类的程序, 可以使用QGuiApplication类. 如果是非GUI程序, 可以使用QCoreApplication, 以免初始化占用不必要的资源.

