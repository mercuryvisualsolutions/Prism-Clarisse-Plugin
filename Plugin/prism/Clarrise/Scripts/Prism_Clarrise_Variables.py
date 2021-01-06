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



class Prism_Clarrise_Variables(object):
	def __init__(self, core, plugin):
		self.version = "v1.2.0.0"
		self.pluginName = "Clarrise"
		self.pluginType = "App"
		self.appShortName = "Clarrise"
		self.appType = "3d"
		self.hasQtParent = False
		self.sceneFormats = [".project"]
		self.appSpecificFormats = self.sceneFormats
		self.outputFormats = [".project"] 	#[".abc", ".obj", ".fbx", ".project"]	
		self.appColor = [255,255,255]
		self.appVersionPresets = ["1.0", "1.1"]
		self.renderPasses = []
		self.preferredUnit = "centimeter"
		self.platforms = ["Windows"]
		self.colorButtonWithStyleSheet = True