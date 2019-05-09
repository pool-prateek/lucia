# Copyright (C) 2018  LuciaSoftware and it's contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see https://github.com/LuciaSoftware/lucia/blob/master/LICENSE.

# this is a simple testing game, used to show the features of lucia.
# Add this repository's lucia package to the PYTHON PATH, so this example can find the lucia module.
import sys
sys.path.append(".")
import time

print("Importing lucia")
import lucia

print("Initializing lucia")
lucia.initialize()

print("Showing the window")
test = lucia.show_window()

while lucia.running:
	lucia.process_events()
	time.sleep(0.05)
	if lucia.key_pressed(lucia.SDLK_a):
		lucia.output.speak("a is pressed")
	if lucia.key_down(lucia.SDLK_s):
		#lucia.output.speak("s is being held down")
		print("LOL")
	if lucia.key_pressed(lucia.SDLK_ESCAPE):
		lucia.quit()
		sys.exit()