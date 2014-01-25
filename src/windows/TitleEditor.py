""" 
 @file
 @brief This file loads the title editor dialog (i.e SVG creator)
 @author Noah Figg <eggmunkee@hotmail.com>
 @author Jonathan Thomas <jonathan@openshot.org>
 
 @section LICENSE
 
 Copyright (c) 2008-2014 OpenShot Studios, LLC
 (http://www.openshotstudios.com). This file is part of
 OpenShot Video Editor (http://www.openshot.org), an open-source project
 dedicated to delivering high quality video editing and animation solutions
 to the world.
 
 OpenShot Video Editor is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 OpenShot Video Editor is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with OpenShot Library.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *
from PyQt5 import uic
from classes import info, ui_util, SettingStore, qt_types, UpdateManager
from classes.logger import log

# Title Editor Dialog
class TitleEditor(QDialog):
	ui_path = os.path.join(info.PATH, 'windows','ui', 'title-editor.ui')
		
	def __init__(self):

		#Create dialog class
		QDialog.__init__(self)

		#Load UI from designer
		ui_util.load_ui(self, self.ui_path)
		
		# Add color picker
		newColor = QColorDialog.getColor(Qt.white)
		#self.color_picker = Color(self)
		#self.widgetForm.layout().addWidget(self.color_picker)

		#Init UI
		ui_util.init_ui(self)
