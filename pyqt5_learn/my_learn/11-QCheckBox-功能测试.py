# 0. 导入需要的包和模块
import sys

from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QCheckBox 功能测试")
window.resize(500, 500)

# print(QCheckBox.__bases__)

cb = QCheckBox("&Python", window)
cb.setIcon(QIcon("xxx.png"))
cb.setIconSize(QSize(60, 60))
cb.setTristate(True)
# cb.setChecked(True)
# cb.setCheckState(Qt.PartiallyChecked)
cb.setCheckState(Qt.Checked)

# cb.stateChanged.connect(lambda state: print(state))
cb.toggled.connect(lambda isChecked: print(isChecked))
# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())
