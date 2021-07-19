# pyqtCuWi

### IconButton

#### Parameters


- `text (text)` (str) : The text shown above the button. (No default)
- `icon (filepath)` (str) : Icon shown above the button. (Default : None)
- `iconSize ((width,height))` (tuple) : Size of icon. (Default : None)
- `iconDirection ('left' or 'right')` (str) : Direction of the icon on the button. (Default : 'left')


#### Methods

- Get Info
    - `getText()` (str) : Returns the text of the button
    - `getIcons()` (dict) : Returns button icons 
- Set Info
    - `setText(text)` (str) : Sets the text of the button
    - `setIcon(filepath)` (str) : Sets the default icon of the button
    - `setHoverIcon(filepath)` (str) : Sets the hover icon of the button
    - `setPressIcon(filepath)` (str) : Sets the press icon of the button
    - `setIconSize((width,height))` (tuple) : Sets size of the buttons icon
    - `setIconDirection('left' or 'right')` (str) : Sets direction of the icon

#### Signals

- `hoverMouse` : Bool value returns when the mouse hovers over the button and leaves the button
- `pressMouse` : Bool value returns when mouse button is pressed

#### Example
```py
from PyQt5.QtWidgets import QApplication, QVBoxLayout,QWidget
from PyQt5.QtCore import QTimer
from pyqtCuWi import IconButton

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('IconButton')

        self.layout = QVBoxLayout()
        self.iconButton = IconButton(text = "IconButton",icon='assets/number-9.png',iconSize=(100,100),iconDirection='left')
        self.iconButton.setHoverIcon('assets/number-8.png')
        self.iconButton.setPressIcon('assets/number-7.png')

        self.layout.addWidget(self.iconButton)
        self.setLayout(self.layout)

        self.iconButton.hoverMouse.connect(self.hoverSignal)
        self.iconButton.pressMouse.connect(self.pressSignal)

    def hoverSignal(self, boolValue):
        if boolValue:
            print("Mouse over button.")
            self.iconButton.setIconDirection('left')

        else:
            print("Mouse left button.")
            self.iconButton.setIconDirection('right')


    def pressSignal(self,boolValue):
        if boolValue:
            print("Button pressed.")
            QTimer.singleShot(1000,self.changeIcons)

    def changeIcons(self):
            icons = self.iconButton.getIcons()
            if '9' in icons['manualIcon']:
                self.iconButton.setIcon('assets/number-6.png')
                self.iconButton.setHoverIcon('assets/number-5.png')
                self.iconButton.setPressIcon('assets/number-4.png')
            elif '6' in icons['manualIcon']:
                self.iconButton.setIcon('assets/number-3.png')
                self.iconButton.setHoverIcon('assets/number-2.png')
                self.iconButton.setPressIcon('assets/number-1.png')
            elif '3' in icons['manualIcon']:
                self.iconButton.setIcon('assets/number-9.png')
                self.iconButton.setHoverIcon('assets/number-8.png')
                self.iconButton.setPressIcon('assets/number-7.png')



if __name__ == '__main__':
    app = QApplication([])
    window = window()
    window.show()
    app.exec_()
```