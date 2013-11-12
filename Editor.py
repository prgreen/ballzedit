#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore
import sys, json
 
import LevelEditorUI, PropertyEditDialogUI, ShapeEditUI

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class Entity(QtGui.QGraphicsItem):

    def __init__(self):
        super(Entity, self).__init__()

        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QtGui.QGraphicsItem.DeviceCoordinateCache)
        self.setZValue(1)

        self.size = 20

    def boundingRect(self):
        adjust = 2.0
        return QtCore.QRectF(-self.size/2 - adjust, -self.size/2 - adjust, self.size + adjust,
                self.size + adjust)

    def paint(self, painter, option, widget):
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.darkGray)

        painter.drawRect(-self.size/2, -self.size/2, self.size, self.size)

    def itemChange(self, change, value):
        if change == QtGui.QGraphicsItem.ItemPositionHasChanged:
            print "moved", self.scenePos().x(), self.scenePos().y()

        return super(Entity, self).itemChange(change, value)

    def mousePressEvent(self, event):
        # TODO remove, this is just for debugging
        print "clicked"
        self.size +=5
        self.update(self.boundingRect())
        super(Entity, self).mousePressEvent(event)

ROLE_TO_COLOR = {"static":"yellow", "dynamic":"brown", "hitter":"red", "ball":"green", "goal":"blue"}
DEFAULT_FRICTION = 0.5
DEFAULT_ELASTICITY = 0.7
DEFAULT_GRAVITY = 100
DEFAULT_DAMPING = 0.7
DEFAULT_SIZE = 400
EDITED_SHAPE = None

class RectEntity(Entity):
    def __init__(self, role="static", x=0, y=0, w=20, h=20, friction=DEFAULT_FRICTION, elasticity=DEFAULT_ELASTICITY):
        super(RectEntity, self).__init__()

        self.shape = "box"
        self.role = role
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.friction = friction
        self.elasticity = elasticity

        self.setPos(self.x, -self.y)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.scene().removeItem(self)
    def boundingRect(self):
        adjust = 2.0
        return QtCore.QRectF(-self.w/2 - adjust, -self.h/2 - adjust, self.w + adjust,
                self.h + adjust)
    def paint(self, painter, option, widget):
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QColor(ROLE_TO_COLOR[self.role]))

        painter.drawRect(-self.w/2, -self.h/2, self.w, self.h)
    def itemChange(self, change, value):
        if change == QtGui.QGraphicsItem.ItemPositionHasChanged:
            self.x = self.scenePos().x()
            self.y = -self.scenePos().y()

        return super(Entity, self).itemChange(change, value)
    def mouseDoubleClickEvent(self, event):
        self.shape_edit = ShapeEditDialog()

        self.shape_edit.roleEdit.setText(self.role)
        self.shape_edit.xEdit.setText(str(self.x))
        self.shape_edit.yEdit.setText(str(self.y))
        self.shape_edit.wEdit.setText(str(self.w))
        self.shape_edit.hEdit.setText(str(self.h))

        self.shape_edit.frictionEdit.setText(str(self.friction))
        self.shape_edit.elasticityEdit.setText(str(self.elasticity))

        global EDITED_SHAPE
        EDITED_SHAPE = self
        self.shape_edit.show()
    def updateShape(self):
        self.update(self.boundingRect())

class CircleEntity(Entity):
    def __init__(self, role="ball", x=0, y=0, r=10, friction=DEFAULT_FRICTION, elasticity=DEFAULT_ELASTICITY):
        super(CircleEntity, self).__init__()

        self.shape = "circle"
        self.role = role
        self.x = x
        self.y = y
        self.r = r
        self.friction = friction
        self.elasticity = elasticity

        self.setPos(self.x, -self.y)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.scene().removeItem(self)
    def boundingRect(self):
        adjust = 2.0
        return QtCore.QRectF(-self.r - adjust, -self.r - adjust, 2*self.r + adjust,
                2*self.r + adjust)
    def paint(self, painter, option, widget):
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QColor(ROLE_TO_COLOR[self.role]))

        painter.drawEllipse(-self.r, -self.r, self.r*2, self.r*2)
    def itemChange(self, change, value):
        if change == QtGui.QGraphicsItem.ItemPositionHasChanged:
            self.x = self.scenePos().x()
            self.y = -self.scenePos().y()
        return super(Entity, self).itemChange(change, value)
    def mouseDoubleClickEvent(self, event):
        self.shape_edit = ShapeEditDialog()

        self.shape_edit.roleEdit.setText(self.role)
        self.shape_edit.xEdit.setText(str(self.x))
        self.shape_edit.yEdit.setText(str(self.y))
        self.shape_edit.rEdit.setText(str(self.r))

        self.shape_edit.frictionEdit.setText(str(self.friction))
        self.shape_edit.elasticityEdit.setText(str(self.elasticity))

        global EDITED_SHAPE
        EDITED_SHAPE = self
        self.shape_edit.show()
    def updateShape(self):
        self.update(self.boundingRect())


class LineEntity(QtGui.QGraphicsLineItem):
    def __init__(self, role="static", x1=0, y1=0, x2=10, y2=10, thickness=0, friction=DEFAULT_FRICTION, elasticity=DEFAULT_ELASTICITY):
        super(LineEntity, self).__init__(x1, -y1, x2, -y2)

        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QtGui.QGraphicsItem.DeviceCoordinateCache)
        self.setZValue(1)

        self.shape = "segment"
        self.role = role
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.thickness = thickness
        self.friction = friction
        self.elasticity = elasticity

        pen = QtGui.QPen(QtGui.QColor(ROLE_TO_COLOR[self.role]))
        pen.setWidth(self.thickness)
        self.setPen(pen)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.scene().removeItem(self)

    def itemChange(self, change, value):
        if change == QtGui.QGraphicsItem.ItemPositionHasChanged:
            x = self.pos().x()
            y = self.pos().y()
            self.x1 = self.line().x1() + x
            self.y1 = -self.line().y1() - y
            self.x2 = self.line().x2() + x
            self.y2 = -self.line().y2() - y

        return super(LineEntity, self).itemChange(change, value)
    def mouseDoubleClickEvent(self, event):
        self.shape_edit = ShapeEditDialog()

        self.shape_edit.roleEdit.setText(self.role)
        self.shape_edit.x1Edit.setText(str(self.x1))
        self.shape_edit.x2Edit.setText(str(self.x2))
        self.shape_edit.y1Edit.setText(str(self.y1))
        self.shape_edit.y2Edit.setText(str(self.y2))
        self.shape_edit.thicknessEdit.setText(str(self.thickness))

        self.shape_edit.frictionEdit.setText(str(self.friction))
        self.shape_edit.elasticityEdit.setText(str(self.elasticity))

        global EDITED_SHAPE
        EDITED_SHAPE = self
        self.shape_edit.show()
    def updateShape(self):
        self.update(self.boundingRect())

class ShapeEditDialog(QtGui.QDialog, ShapeEditUI.Ui_Dialog):
    def __init__(self, parent=None):
        super(ShapeEditDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Shape Property Editor")
    def accept(self):
        global EDITED_SHAPE
        # save all valid changes in shape object
        try:
            EDITED_SHAPE.x = float(self.xEdit.text())
        except:
            pass
        try:
            EDITED_SHAPE.y = float(self.yEdit.text())
        except:
            pass
        try:
            EDITED_SHAPE.w = float(self.wEdit.text())
        except:
            pass
        try:
            EDITED_SHAPE.h = float(self.hEdit.text())
        except:
            pass
        try:
            EDITED_SHAPE.r = float(self.rEdit.text())
        except:
            pass
        try:
            EDITED_SHAPE.role = str(self.roleEdit.text())
        except:
            pass
        try:
            EDITED_SHAPE.x1 = float(self.x1Edit.text())
        except:
            pass
        try:
            EDITED_SHAPE.y1 = float(self.y1Edit.text())
        except:
            pass
        try:
            EDITED_SHAPE.x2 = float(self.x2Edit.text())
        except:
            pass
        try:
            EDITED_SHAPE.y2 = float(self.y2Edit.text())
        except:
            pass
        try:
            EDITED_SHAPE.thickness = float(self.thicknessEdit.text())
        except:
            pass
        try:
            EDITED_SHAPE.friction = float(self.frictionEdit.text())
        except:
            pass
        try:
            EDITED_SHAPE.elasticity = float(self.elasticityEdit.text())
        except:
            pass

        if isinstance(EDITED_SHAPE, Entity):
            EDITED_SHAPE.setPos(EDITED_SHAPE.x, -EDITED_SHAPE.y)
        if isinstance(EDITED_SHAPE, LineEntity):
            EDITED_SHAPE.setLine(EDITED_SHAPE.x1-EDITED_SHAPE.pos().x(),-EDITED_SHAPE.y1-EDITED_SHAPE.pos().y(),EDITED_SHAPE.x2-EDITED_SHAPE.pos().x(),-EDITED_SHAPE.y2-EDITED_SHAPE.pos().y())
            pen = QtGui.QPen(QtGui.QColor(ROLE_TO_COLOR[EDITED_SHAPE.role]))
            pen.setWidth(EDITED_SHAPE.thickness)
            EDITED_SHAPE.setPen(pen)
            EDITED_SHAPE.setPos(EDITED_SHAPE.x1-EDITED_SHAPE.line().x1(), -EDITED_SHAPE.line().y2()-EDITED_SHAPE.y2)
        EDITED_SHAPE.updateShape()

        super(ShapeEditDialog, self).accept()

class PropertyEditDialog(QtGui.QDialog, PropertyEditDialogUI.Ui_mainDialog):
    def __init__(self, parent=None):
        super(PropertyEditDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("General/Info Property Editor")

class LevelEditor(QtGui.QMainWindow, LevelEditorUI.Ui_mainWindow):
    def __init__(self, parent=None):
        super(LevelEditor, self).__init__(parent)
        self.setupUi(self)
        self.edit = PropertyEditDialog(self)
        self.connectActions()

        self.level_txt = ""
        self.level_json = None

    def connectActions(self):
        self.actionExit.triggered.connect(QtGui.qApp.quit)
        self.actionOpen.triggered.connect(self.openLevel)
        self.actionGeneral.triggered.connect(self.openEdit)
        self.actionSave.triggered.connect(self.saveLevel)

        self.edit.titleLineEdit.textChanged.connect(self.titleLineChanged)
        self.edit.descriptionLineEdit.textChanged.connect(self.descriptionLineChanged)
        self.edit.gravityLineEdit.textChanged.connect(self.gravityLineChanged)
        self.edit.dampingLineEdit.textChanged.connect(self.dampingLineChanged)
        self.edit.sizeLineEdit.textChanged.connect(self.sizeLineChanged)

        self.BoxButton.clicked.connect(self.createBox)
        self.CircleButton.clicked.connect(self.createCircle)
        self.SegmentButton.clicked.connect(self.createSegment)
        #TODO bounds
    def createBox(self):
        try:
            e = RectEntity()
            self.scene.addItem(e)
        except:
            pass
    def createCircle(self):
        try:
            e = CircleEntity()
            self.scene.addItem(e)
        except:
            pass
    def createSegment(self):
        try:
            e = LineEntity("static",0,0,20,20,5)
            self.scene.addItem(e)    
        except:
            pass
    def titleLineChanged(self, text):
        if not "info" in self.level_json:
            self.level_json["info"] = {}
        if not "title" in self.level_json["info"]:
            self.level_json["info"]["title"] =""
        self.level_json["info"]["title"] = str(text)
    def descriptionLineChanged(self, text):
        if not "info" in self.level_json:
            self.level_json["info"] = {}
        if not "description" in self.level_json["info"]:
            self.level_json["info"]["description"] =""
        self.level_json["info"]["description"] = str(text)
    def gravityLineChanged(self, text):
        if not "general" in self.level_json:
            self.level_json["general"] = {}
        if not "gravity" in self.level_json["general"]:
            self.level_json["general"]["gravity"] = DEFAULT_GRAVITY
        if is_number(self.level_json["general"]["gravity"]):
            self.level_json["general"]["gravity"] = float(str(text))
    def dampingLineChanged(self, text):
        if not "general" in self.level_json:
            self.level_json["general"] = {}
        if not "damping" in self.level_json["general"]:
            self.level_json["general"]["damping"] = DEFAULT_DAMPING
        if is_number(self.level_json["general"]["damping"]):
            self.level_json["general"]["damping"] = float(str(text))
    def sizeLineChanged(self, text):
        if not "general" in self.level_json:
            self.level_json["general"] = {}
        if not "size" in self.level_json["general"]:
            self.level_json["general"]["size"] = DEFAULT_SIZE
        if is_number(self.level_json["general"]["size"]):
            self.level_json["general"]["size"] = float(str(text))
            self.displayLevel()
    def openLevel(self):
        fileName = QtGui.QFileDialog.getOpenFileName(
                        self,
                        "Open level file",
                        QtCore.QDir.homePath(),
                        "JSON Level File (*.json)"
                    )
        if fileName:
            self.level_txt = open(fileName).read()
            if self.level_txt == "":
                QtGui.QMessageBox.warning(self, "ERROR", "File cannot be empty.")
                return

            self.level_json = json.loads(self.level_txt)
            self.displayLevel()
    def openEdit(self):
        #if a level is loaded, load dialog, else show alert
        if self.level_json is None:
            QtGui.QMessageBox.warning(self, "ERROR", "Open a level file first.")
        else:
            self.edit.show()
            #TODO replace try/except with if key in dict:
            try:
                self.edit.titleLineEdit.setText(self.level_json["info"]["title"])
            except:
                pass
            try:
                self.edit.descriptionLineEdit.setText(self.level_json["info"]["description"])
            except:
                pass
            try:
                self.edit.gravityLineEdit.setText(str(self.level_json["general"]["gravity"]))
            except:
                pass
            try:
                self.edit.dampingLineEdit.setText(str(self.level_json["general"]["damping"]))
            except:
                pass
            try:
                self.edit.sizeLineEdit.setText(str(self.level_json["general"]["size"]))
            except:
                pass
            


    def displayLevel(self):
        #draw all entities in graphics view
        self.scene = QtGui.QGraphicsScene(self)

        #TODO REMOVE
        #e1 = RectEntity("hitter", 200, 150, 10)
        #self.scene.addItem(e1)
        
        for e in self.level_json["entities"]:
            if "friction" not in e:
                e["friction"] = DEFAULT_FRICTION
            if "elasticity" not in e:
                e["elasticity"] = DEFAULT_ELASTICITY

            if e["shape"] == "circle":
                item = CircleEntity(e["role"], e["x"], e["y"], e["r"], e["friction"], e["elasticity"])
                self.scene.addItem(item)
            elif e["shape"] == "box":

                item = RectEntity(e["role"], e["x"], e["y"], e["w"], e["h"], e["friction"], e["elasticity"])
                self.scene.addItem(item)
            elif e["shape"] == "segment":
                if "thickness" not in e:
                    e["thickness"] = 0
                item = LineEntity(e["role"], e["x1"], e["y1"], e["x2"], e["y2"], e["thickness"], e["friction"], e["elasticity"])
                self.scene.addItem(item)
        
        try:
            for e in self.level_json["general"]["bounds"]:
                rectangle = self.scene.addRect(e["x"] - e["w"]/2, -e["y"] - e["h"]/2, e["w"], e["h"], QtGui.QColor('red'), QtGui.QColor(0,0,0,0))
                rectangle.setFlag(QtGui.QGraphicsItem.ItemIsMovable) 
                #rectangle.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
                rectangle.setZValue(-1)
        except:
            pass        
        self.graphicsView.setBackgroundBrush(QtGui.QColor('black'))
        
        # 0,0 cross
        self.scene.addLine(-5, 0, 5, 0, QtGui.QColor(255,255,255,128))
        self.scene.addLine(0, -5, 0, 5, QtGui.QColor(255,255,255,128))
        
        size = 400
        try:
            size = self.level_json["general"]["size"]
        except:
            pass
        #top left
        self.scene.addLine(-size/2, -size*3/8, -size/2+5, -size*3/8, QtGui.QColor(255,255,255,128))
        self.scene.addLine(-size/2, -size*3/8, -size/2, -size*3/8+5, QtGui.QColor(255,255,255,128))
        #top right
        self.scene.addLine(size/2, -size*3/8, size/2-5, -size*3/8, QtGui.QColor(255,255,255,128))
        self.scene.addLine(size/2, -size*3/8, size/2, -size*3/8+5, QtGui.QColor(255,255,255,128))
        #bottom left
        self.scene.addLine(-size/2, size*3/8, -size/2+5, size*3/8, QtGui.QColor(255,255,255,128))
        self.scene.addLine(-size/2, size*3/8, -size/2, size*3/8-5, QtGui.QColor(255,255,255,128))
        #bottom right
        self.scene.addLine(size/2, size*3/8, size/2-5, size*3/8, QtGui.QColor(255,255,255,128))
        self.scene.addLine(size/2, size*3/8, size/2, size*3/8-5, QtGui.QColor(255,255,255,128))
        
        self.graphicsView.setScene(self.scene)

        #TODO make scale absolute (or only first time)
        #self.graphicsView.scale(2,2)
    def mouseMoveEvent(self, event):
        pos_scene = self.graphicsView.mapToScene(event.pos())
        msg = str(pos_scene.x()-self.graphicsView.pos().x()) + "," + str(-pos_scene.y()+self.graphicsView.pos().y()+self.menubar.size().height())
        self.statusbar.showMessage(msg)
        super(LevelEditor, self).mouseMoveEvent(event)

    def saveLevel(self):
        if not self.level_json is None:
            # remove all entities
            self.level_json["entities"] = []
            # check all items and generate appropriate entities
            items = [item for item in self.scene.items() if isinstance(item,Entity) or isinstance(item,LineEntity)]
            for i in items:
                entity = {}
                if i.shape == "box":
                    entity["role"] = i.role
                    entity["shape"] = "box"
                    entity["x"] = i.x
                    entity["y"] = i.y
                    entity["w"] = i.w
                    entity["h"] = i.h
                    entity["friction"] = i.friction
                    entity["elasticity"] = i.elasticity
                elif i.shape== "circle":
                    entity["role"] = i.role
                    entity["shape"] = "circle"
                    entity["x"] = i.x
                    entity["y"] = i.y
                    entity["r"] = i.r
                    entity["friction"] = i.friction
                    entity["elasticity"] = i.elasticity
                elif i.shape== "segment":
                    entity["role"] = i.role
                    entity["shape"] = "segment"
                    entity["x1"] = i.x1
                    entity["y1"] = i.y1
                    entity["x2"] = i.x2
                    entity["y2"] = i.y2
                    entity["friction"] = i.friction
                    entity["elasticity"] = i.elasticity
                self.level_json["entities"].append(entity)

            # save dialog
            fileName = QtGui.QFileDialog.getSaveFileName(
                        self,
                        "Save level file",
                        QtCore.QDir.homePath(),
                        "JSON Level File (*.json)"
                    )
            if fileName:
                f = open(fileName, "w")
                f.write(json.dumps(self.level_json, indent=4, sort_keys=True))
                f.close()
    def main(self):
        self.show()

 
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    
    levelEditor = LevelEditor()
    levelEditor.setWindowTitle("Ballz Level Editor")
    levelEditor.main()
    app.exec_()
    print (json.dumps(levelEditor.level_json, indent=4, sort_keys=True))