# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2019 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.



import ix

import os, sys
import traceback, time, shutil, platform
from functools import wraps

try:
	from PySide2.QtCore import *
	from PySide2.QtGui import *
	from PySide2.QtWidgets import *
	psVersion = 2
except:
	from PySide.QtCore import *
	from PySide.QtGui import *
	psVersion = 1

import pyqt_clarisse


class Prism_Clarrise_Functions(object):
	def __init__(self, core, plugin):
		self.core = core
		self.plugin = plugin

	def err_decorator(func):
		@wraps(func)
		def func_wrapper(*args, **kwargs):
			exc_info = sys.exc_info()
			try:
				return func(*args, **kwargs)
			except Exception as e:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				erStr = ("%s ERROR - Prism_Plugin_Clarrise %s:\n%s\n\n%s" % (time.strftime("%d/%m/%y %X"), args[0].plugin.version, ''.join(traceback.format_stack()), traceback.format_exc()))
				args[0].core.writeErrorLog(erStr)

		return func_wrapper


	# @err_decorator
	# def startup(self, origin):
		
	# 	origin.writeToFile("PrimFunctions|StartUp")

	# 	qapp = QApplication.instance()

	# 	if qapp is None:
	# 		qapp = QApplication(sys.argv)

	# 	origin.timer.stop()

	# 	origin.writeToFile("PrimFunctions|qapp " + str(qapp))

	# 	w = QWidget()

	# 	origin.writeToFile("PrimFunctions|QWidget() " + str(w))

	# 	origin.messageParent = qapp

	# 	origin.startasThread()



	@err_decorator
	def instantStartup(self, origin):
	#	qapp = QApplication.instance()

		with (open(os.path.join(self.core.prismRoot, "Plugins", "Apps", "Fusion", "UserInterfaces", "FusionStyleSheet", "Fusion.qss"), "r")) as ssFile:
			ssheet = ssFile.read()

		ssheet = ssheet.replace("qss:", os.path.join(self.core.prismRoot, "Plugins", "Apps", "Fusion", "UserInterfaces", "FusionStyleSheet").replace("\\", "/") + "/")
		#ssheet = ssheet.replace("#c8c8c8", "rgb(47, 48, 54)").replace("#727272", "rgb(40, 40, 46)").replace("#5e90fa", "rgb(70, 85, 132)").replace("#505050", "rgb(33, 33, 38)")
		#ssheet = ssheet.replace("#a6a6a6", "rgb(37, 39, 42)").replace("#8a8a8a", "rgb(37, 39, 42)").replace("#b5b5b5", "rgb(47, 49, 52)").replace("#999999", "rgb(47, 49, 52)")
		#ssheet = ssheet.replace("#9f9f9f", "rgb(31, 31, 31)").replace("#b2b2b2", "rgb(31, 31, 31)").replace("#aeaeae", "rgb(35, 35, 35)").replace("#c1c1c1", "rgb(35, 35, 35)")
		#ssheet = ssheet.replace("#555555", "rgb(27, 29, 32)").replace("#717171", "rgb(27, 29, 32)").replace("#878787", "rgb(37, 39, 42)").replace("#7c7c7c", "rgb(37, 39, 42)")
		#ssheet = ssheet.replace("#4c4c4c", "rgb(99, 101, 103)").replace("#5b5b5b", "rgb(99, 101, 103)").replace("#7aa3e5", "rgb(65, 76, 112)").replace("#5680c1", "rgb(65, 76, 112)")
		#ssheet = ssheet.replace("#5a5a5a", "rgb(35, 35, 35)").replace("#535353", "rgb(35, 35, 41)").replace("#373737", "rgb(35, 35, 41)").replace("#858585", "rgb(31, 31, 31)").replace("#979797", "rgb(31, 31, 31)")
		#ssheet = ssheet.replace("#4771b3", "rgb(70, 85, 132)").replace("#638dcf", "rgb(70, 85, 132)").replace("#626262", "rgb(45, 45, 51)").replace("#464646", "rgb(45, 45, 51)")
		#ssheet = ssheet.replace("#7f7f7f", "rgb(60, 60, 66)").replace("#6c6c6c", "rgb(60, 60, 66)").replace("#565656", "rgb(35, 35, 41)").replace("#5d5d5d", "rgb(35, 35, 41)")
		#ssheet = ssheet.replace("white", "rgb(200, 200, 200)")
		if "parentWindows" in origin.prismArgs:
			origin.messageParent.setStyleSheet(ssheet)
		#	origin.messageParent.resize(10,10)
		#	origin.messageParent.show()
			origin.parentWindows = True
		else:
			qapp = QApplication.instance()
			qapp.setStyleSheet(ssheet)
			appIcon = QIcon(os.path.join(self.core.prismRoot, "Scripts", "UserInterfacesPrism", "p_tray.png"))
			qapp.setWindowIcon(appIcon)

			origin.writeToFile("PrimFunctions | instant | qapp  " + str(qapp))

		self.isRendering = [False,""]

		# ----------->
		# return False


	@err_decorator
	def startup(self, origin):
		#if not hasattr(self, "clarrise"):
		#	return False

		origin.timer.stop()
		
		origin.startasThread()
		
		# origin.writeToFile("PrimFunctions | starup | qapp  " + str(qapp))

		# return True




	@err_decorator
	def autosaveEnabled(self, origin):
		# get autosave enabled
		return False


	@err_decorator
	def onProjectChanged(self, origin):
		pass


	@err_decorator
	def sceneOpen(self, origin):

		print "---------------> sceneOpen() --->"

		if hasattr(origin, "asThread") and origin.asThread.isRunning():
			origin.startasThread()


	@err_decorator
	def executeScript(self, origin, code, execute=False, logErr=True):
		if logErr:
			try:
				if not execute:
					return eval(code)
				else:
					exec(code)
			except Exception as e:
				msg = '\npython code:\n%s' % code
				exec("raise type(e), type(e)(e.message + msg), sys.exc_info()[2]")
		else:
			try:
				if not execute:
					return eval(code)
				else:
					exec(code)
			except:
				pass


	@err_decorator
	def getCurrentFileName(self, origin, path=True):
		project_name = ix.application.get_factory().get_vars().get("PNAME").get_string()
		project_name += ".project"
		dir_name = ix.application.get_factory().get_vars().get("PDIR").get_string()
		fileName = os.path.join(dir_name, project_name)
		return fileName


	@err_decorator
	def getSceneExtension(self, origin):
		return self.sceneFormats[0]


	@err_decorator
	def saveScene(self, origin, filepath):

		'''
		try:
			project_name = ix.application.get_factory().get_vars().get("PNAME").get_string()
			dir_name = ix.application.get_factory().get_vars().get("PDIR").get_string()
			filename = os.path.join(dir_name, project_name)
			ix.save_project(filename)
			return True
		except:
			return False
		'''
		print "SaveScene =============================>>> filepath %s"%(filepath)

		try:
			ix.save_project(str(filepath))
			print "--------> SaveScene()"
			print filepath
			return True
		except:
			print "--------> Can't Save Scene"
			return False



	@err_decorator
	def getImportPaths(self, origin):
		val = ix.application.get_factory().get_vars().get("PrismImports")
		if val is None: 
			return False
		value = val.get_string()
		return value


	@err_decorator
	def getFrameRange(self, origin):
		startframe = ix.application.get_current_frame_range()[0]
		endframe = ix.application.get_current_frame_range()[1]

		return [startframe, endframe]


	@err_decorator
	def setFrameRange(self, origin, startFrame, endFrame):
		ix.application.set_current_frame_range(startframe, endFrame)


	@err_decorator
	def getFPS(self, origin):
		return ix.application.get_factory().get_time().get_fps()


	@err_decorator
	def setFPS(self, origin, fps):
		ix.application.get_factory().get_time().set_fps(fps)


	@err_decorator
	def getAppVersion(self, origin):
		return "1.0"
		

	@err_decorator
	def onProjectBrowserStartup(self, origin):
		origin.loadOiio()
	#	origin.sl_preview.mousePressEvent = origin.sliderDrag
		origin.sl_preview.mousePressEvent = origin.sl_preview.origMousePressEvent


	@err_decorator
	def projectBrowserLoadLayout(self, origin):
		pass


	@err_decorator
	def setRCStyle(self, origin, rcmenu):
		pass


	@err_decorator
	def openScene(self, origin, filepath):
		print "OpenScene ------------------------>>>> filePath" + str(filepath)
		fileName = os.path.splitext(os.path.basename(filepath))
		print "OpenScene ------------------------>>>> fileName" + str(fileName[-1])

		if str(fileName[-1]) == ".project":
			ix.load_project(str(filepath))
			return True
		else:
			QMessageBox.warning(self.core.messageParent,"Open Project", "Can't open files of type %s"%(str(fileName[-1])))


	@err_decorator
	def correctExt(self, origin, lfilepath):
		return lfilepath


	@err_decorator
	def setSaveColor(self, origin, btn):
		btn.setPalette(origin.savedPalette)


	@err_decorator
	def clearSaveColor(self, origin, btn):
		btn.setPalette(origin.oldPalette)


	@err_decorator
	def setProject_loading(self, origin):
		pass


	@err_decorator
	def onPrismSettingsOpen(self, origin):
		pass


	@err_decorator
	def createProject_startup(self, origin):
		pass


	@err_decorator
	def editShot_startup(self, origin):
		origin.loadOiio()


	@err_decorator
	def shotgunPublish_startup(self, origin):
		pass


	@err_decorator
	def sm_export_addObjects(self, origin):
		print "------------------> Func >> sm_export_addObjects"

		selectedObjects = []
		for i in ix.selection:
			selectedObjects.append(i)

		print "Selected objects" + str(selectedObjects)

		for i in selectedObjects:
			if not i in origin.nodes:
				origin.nodes.append(i)

		origin.updateUi()
		origin.stateManager.saveStatesToScene()


	@err_decorator
	def getNodeName(self, origin, node):
		print "--------------------------> getNodeName + %s"%(node)

		if self.isNodeValid(origin, node):
			try:
				return node.get_name()
			except:
				QMessageBox.warning(self.core.messageParent, "Warning", "Cannot get name from %s" % node)
				return node
		else:
			return "invalid"


	@err_decorator
	def selectNodes(self, origin):
		if origin.lw_objects.selectedItems() != []:
			nodes = []
			for i in origin.lw_objects.selectedItems():
				node = origin.nodes[origin.lw_objects.row(i)]
				if self.isNodeValid(origin, node):
					nodes.append(node)
			
			current_sel = [str(x) for x in ix.selection]
			for i in nodes:
			    if i not in current_sel:
			        ix.selection.add(i)


	@err_decorator
	def isNodeValid(self, origin, handle):
		return True


	@err_decorator
	def getCamNodes(self, origin, cur=False):
		sceneCams = [] 
		p_context = ix.get_item("project://")
		cameraArray = ix.api.OfObjectArray()
		p_context.get_all_objects("Camera", cameraArray)

		for cam in cameraArray:
		    sceneCams.append(str(cam))
		    
		print sceneCams

		if cur:
			sceneCams = ["Current View"] + sceneCams

		return sceneCams


	@err_decorator
	def getCamName(self, origin, handle):
		print "---------------------------> GetCam Name (Not Implemented Yet)"
		if handle == "Current View":
			return handle


		# return str(nodes[0])


	@err_decorator
	def selectCam(self, origin):
		if self.isNodeValid(origin, origin.curCam):
			select(origin.curCam)


	@err_decorator
	def sm_export_startup(self, origin):
		print "------------------> Func >> sm_export_startup"
		# this will extend the current state manger ui|export with some more options. And it varies for each extension

		origin.chb_wholeScene.setChecked(True)

		origin.w_convertExport.setVisible(False)
		origin.w_additionalOptions.setVisible(False)
		
		#origin.gb_objects.setVisible(False)
		#origin.lw_objects.setVisible(False)

		
		# w_ or chb_


	@err_decorator
	def sm_export_setTaskText(self, origin, prevTaskName):
		# in maya there's a set with the selected objects with the same name as export name for easy select
		print "------------------> Func >> sm_export_setTaskText"
		origin.l_taskName.setText(origin.nameWin.e_item.text())

		##### PRE-DONE!

	@err_decorator
	def sm_export_removeSetItem(self, origin, node):
		# remove the a set in maya
		print "------------------> Func >> sm_export_removeSetItem"

		#### NOT_NOW!!!!



	@err_decorator
	def sm_export_clearSet(self, origin):
		# clear sets in maya
		print "------------------> Func >> sm_export_clearSet"

		#### NOT_NOW!!!!



	@err_decorator
	def sm_export_updateObjects(self, origin):
		print "------------------> Func >> sm_export_updateObjects"

		# select the nodes inside the sets + the current selections too

		#### NOT_NOW!!!!


	@err_decorator
	def sm_export_exportShotcam(self, origin, startFrame, endFrame, outputName):
		result = self.sm_export_exportAppObjects(origin, startFrame, endFrame, (outputName + ".abc"), nodes=[origin.curCam], expType=".abc")
		result = self.sm_export_exportAppObjects(origin, startFrame, endFrame, (outputName + ".fbx"), nodes=[origin.curCam], expType=".fbx")
		return result


	@err_decorator
	def sm_export_exportAppObjects(self, origin, startFrame, endFrame, outputName, scaledExport=False, nodes=None, expType=None):

		if expType is None:
			expType = origin.cb_outType.currentText()

		if expType == ".project":
			project_name = ix.application.get_factory().get_vars().get("PNAME").get_string()
			project_name += ".project"
			dir_name = ix.application.get_factory().get_vars().get("PDIR").get_string()
			filename = os.path.join(dir_name, project_name)

			# this function duplicates the path??!!! why ?
			#self.core.saveScene(outputName)

			print "sm_export_exportAppObjects-----------> filename is %s"%(filename)
			print "sm_export_exportAppObjects-----------> outputname is %s"%(outputName)

			# ix.save_project(str(outputName))
			curFileName = self.core.getCurrentFileName()

			print "ExportAppProjects--------------------------->CurrentFileName%s"%(curFileName)

			self.core.copySceneFile(curFileName, outputName)

			return outputName
		else:
			return False


	@err_decorator
	def sm_export_preDelete(self, origin):
		print "------------------> Func >> sm_export_preDelete"

		# 1- delete the current set with the same current task name
		# l_taskname is the current selected taskname


	@err_decorator
	def sm_export_unColorObjList(self, origin):
		print "------------------> Func >> sm_export_unColorObjList"
		origin.lw_objects.setStyleSheet("QListWidget { border: 3px solid rgb(50,50,50); }")


	@err_decorator
	def sm_export_typeChanged(self, origin, idx):
		print "------------------> Func >> sm_export_typeChanged"

		# 1- check the extenstion (idx) type e.g. if .abc check the checkbox of exportName space
		# 2- check if .project --> setvisiable exportSene checkbox
		# 3- 


	@err_decorator
	def sm_export_preExecute(self, origin, startFrame, endFrame):
		print "------------------> Func >> sm_export_preExecute"

		# 1- some warning messages to be diaplayed 


		warnings = []

		return warnings


	@err_decorator
	def sm_export_loadData(self, origin, data):
		print "------------------> Func >> sm_export_loadData"

		# check those variables and add them to the data[]
		# Set those variables which are stored inside origin.variables

		# exportnamespaces
		# importreferences
		# deleteunknownnodes
		# deletedisplaylayers
		# preserveReferences



	@err_decorator
	def sm_export_getStateProps(self, origin):
		print "------------------> Func >> sm_export_getStateProps"

		# Set those variables which are stored inside origin.variables
		# exportnamespaces
		# importreferences
		# deleteunknownnodes
		# deletedisplaylayers
		# preserveReferences


		stateProps = {}

		return stateProps


	@err_decorator
	def sm_render_isVray(self, origin):
		return False


	@err_decorator
	def sm_render_setVraySettings(self, origin):
		pass


	@err_decorator
	def sm_render_startup(self, origin):
		pass


	@err_decorator
	def sm_render_getRenderLayer(self, origin):
		rlayerNames = []

		return rlayerNames


	@err_decorator
	def sm_render_setTaskWarn(self, origin, warn):
		if warn:
			origin.b_changeTask.setPalette(origin.warnPalette)
		else:
			origin.b_changeTask.setPalette(origin.oldPalette)


	@err_decorator
	def sm_render_refreshPasses(self, origin):
		pass


	@err_decorator
	def sm_render_openPasses(self, origin, item=None):
		pass


	@err_decorator
	def sm_render_deletePass(self, origin, item):
		pass


	@err_decorator
	def sm_render_preSubmit(self, origin, rSettings):
		pass


	@err_decorator
	def sm_render_startLocalRender(self, origin, outputName, rSettings):
		pass


	@err_decorator
	def sm_render_undoRenderSettings(self, origin, rSettings):
		pass


	@err_decorator
	def sm_render_getDeadlineParams(self, origin, dlParams, homeDir):
		pass


	@err_decorator
	def getCurrentRenderer(self, origin):
		return "Renderer"


	@err_decorator
	def getCurrentSceneFiles(self, origin):
		curFileName = self.core.getCurrentFileName()
		scenefiles = [curFileName]
		return  scenefiles


	@err_decorator
	def sm_render_getRenderPasses(self, origin):
		return []


	@err_decorator
	def sm_render_addRenderPass(self, origin, passName, steps):
		pass


	@err_decorator
	def sm_render_preExecute(self, origin):
		warnings = []

		return warnings


	@err_decorator
	def sm_render_fixOutputPath(self, origin, outputName):
		return outputName


	@err_decorator
	def getProgramVersion(self, origin):
		return "1.0"


	@err_decorator
	def sm_render_getDeadlineSubmissionParams(self, origin, dlParams, jobOutputFile):
		dlParams["Build"] = dlParams["build"]
		dlParams["OutputFilePath"] = os.path.split(jobOutputFile)[0]
		dlParams["OutputFilePrefix"] = os.path.splitext(os.path.basename(jobOutputFile))[0]
		dlParams["Renderer"] = self.getCurrentRenderer(origin)

		if origin.chb_resOverride.isChecked() and "resolution" in dlParams:
			resString = "Image"
			dlParams[resString + "Width"] = str(origin.sp_resWidth.value())
			dlParams[resString + "Height"] = str(origin.sp_resHeight.value())

		return dlParams


	@err_decorator
	def deleteNodes(self, origin, handles, num=0):
		pass


	@err_decorator
	def sm_import_startup(self, origin):
		pass


	@err_decorator
	def sm_import_disableObjectTracking(self, origin):
		self.deleteNodes(origin, [origin.setName])


	##TODO::search alternative builtin clarisse function to get the current node with the same name
	@err_decorator
	def sm_import_importToApp(self, origin, doImport, update, impFileName):

		print "----------------------------------------------->>>"
		print "sm_imporT_importToApp"
		print "----------------------------------------------->>>"
		print "origin = " + str(origin)
		print "doImport = " + str(doImport)
		print "Update = " + str(update)
		print "Filename = " + str(impFileName)
		print "----------------------------------------------->>>"

		fileName = os.path.splitext(os.path.basename(impFileName))
		current_context = ix.application.get_selection().get_slot_working_context("Global")

		current_file = ix.application.get_factory().item_exists(str(current_context) + "/" + str(fileName[0]))

		if current_file:
			print "File is already exists"
		else:	
			if not update:
			    print "File %s need to be imported" % (fileName[0])
			    if fileName[-1] == ".abc":
			    	ix.reference_file(current_context, str(impFileName))
			    
			    elif fileName[-1] == ".project":
			    	print "-------------> Filneme is project"
			    	ix.import_project(str(impFileName))

			    elif fileName[-1] == ".obj":
			    	obj = ix.import_geometry(str(impFileName))
			    	obj.rename("_".join(str(obj).split("/")[-1].split("_")[0:-1])) #remove _obj at the end of the .obj item name
			else:
				# get the version file to update its path
				version = list(fileName[0])[-1]
				prevVersions = list(reversed(range(int(version))))
				
				nameList = list(fileName[0])

				print "ImportToApp----------------------->>>> current version " + str(version)
				print "ImportToApp----------------------->>>> current version " + str(prevVersions)

				for v in prevVersions:

					# fileName[0]  = "ship_export"
					# fileName[-1] = ".obj"

					nameList[-1] = str(v)
					currentFileName = ''.join(nameList)
					print "version %s"%(v)
					print "currentFileName %s"%(currentFileName)

					current_file = ix.application.get_factory().item_exists(str(current_context) + "/" + str(currentFileName))

					if current_file is not None:
						current_file.get_attribute("filename").set_string(str(impFileName))
						current_file.rename(str(fileName[0]))
						break

				print "-----------------> Updating file."
				print current_file
				print currentFileName

		# ix.import_geometry(impFileName)
		# ix.import_scene(impFileName)

		result = True
		doImport = True

		return result, doImport


	@err_decorator
	def sm_import_updateObjects(self, origin):
		pass


	@err_decorator
	def sm_import_removeNameSpaces(self, origin):
		pass


	@err_decorator
	def sm_import_unitConvert(self, origin):
		pass


	@err_decorator
	def sm_playblast_startup(self, origin):
		frange = self.getFrameRange(origin)
		origin.sp_rangeStart.setValue(frange[0])
		origin.sp_rangeEnd.setValue(frange[1])


	@err_decorator
	def sm_playblast_createPlayblast(self, origin, jobFrames, outputName):
		pass


	@err_decorator
	def sm_playblast_preExecute(self, origin):
		warnings = []
		
		return warnings


	@err_decorator
	def sm_playblast_execute(self, origin):
		pass


	@err_decorator
	def sm_playblast_postExecute(self, origin):
		pass


	@err_decorator
	def onStateManagerOpen(self, origin):
		pass


	@err_decorator
	def sm_saveStates(self, origin, buf):
		print "---------------> Saving States"
		print buf

		custom_Var = ix.application.get_factory().get_vars().add(ix.api.OfVars.TYPE_CUSTOM, "PrismStates", ix.api.OfAttr.TYPE_STRING, ix.api.OfAttr.CONTAINER_SINGLE, ix.api.OfAttr.VISUAL_HINT_DEFAULT)
		custom_Var.set_string(buf)


	@err_decorator
	def sm_saveImports(self, origin, importPaths):
		custom_Var = ix.application.get_factory().get_vars().add(ix.api.OfVars.TYPE_CUSTOM, "PrismImports", ix.api.OfAttr.TYPE_STRING, ix.api.OfAttr.CONTAINER_SINGLE, ix.api.OfAttr.VISUAL_HINT_DEFAULT)
		custom_Var.set_string(importPaths)


	@err_decorator
	def sm_readStates(self, origin):
		
		print "---------------> Reading States"

		val = ix.application.get_factory().get_vars().get("PrismStates")

		if val is not None:
			value = val.get_string()
			print "States = " + str(value)
			return value


	@err_decorator
	def sm_deleteStates(self, origin):
		pass


	@err_decorator
	def sm_getExternalFiles(self, origin):
		extFiles = []
		return [extFiles, []]


	@err_decorator
	def sm_createRenderPressed(self, origin):
		origin.createPressed("Render")