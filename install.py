import os
import shutil
import maya.cmds as mc


def Run():
    projDir = os.path.dirname(os.path.abspath(__file__))
    projName = os.path.split(projDir)[-1]

    mayaScriptDir = os.path.join(mc.internalVar(uad=True), "scripts")
    pluginDestDir = os.path.join(mayaScriptDir, projName)

    srcDirName = "src"
    assestsDirName = "assets"

    if os.path.exists(pluginDestDir):
        shutil.rmtree(pluginDestDir)

    os.makedirs(pluginDestDir, exist_ok=True)

    shutil.copytree(os.path.join(projDir, srcDirName), os.path.join(pluginDestDir, srcDirName))
    shutil.copytree(os.path.join(projDir, assestsDirName), os.path.join(pluginDestDir, assestsDirName))

    def CreateShelfButtonForScript(scriptName):
        currentShelf = mc.tabLayout("ShelfLayout", q=True, selectTab = True)
        mc.setParent(currentShelf)
        iconImage = os.path.join(pluginDestDir, assestsDirName, scriptName + ".png")
        mc.shelfButton(c=f"from {projName}.src import {scriptName}; {scriptName}.Run()", image=iconImage)


    CreateShelfButtonForScript("LimbRigger")
    CreateShelfButtonForScript("TrimSheetUVBuilder")