# Copyright 2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
include(GrPython)

GR_PYTHON_INSTALL(
    FILES
    __init__.py
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
    COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
    FILES
    gr_ramp_source.py
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
    COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
    FILES
    gr_step_source.py
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
    COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
    FILES
    ramp_hierblock.py
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
    COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
    FILES
    step_hierblock.py
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
    COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
    FILES
    Numerator.py
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
    COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
     FILES
     Denominator.py
     DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
     COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
     FILES
     Calculator.py
     DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
     COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
     FILES
     Bode.py
     DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
     COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
	 FILES
	 Roots.py
     DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
     COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
     FILES
	 Comparator.py
     DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
     COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
     FILES
	 Max_val.py
     DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
     COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
     FILES
     plzr_plt.py
     DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
     COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
     FILES
	 Response.py
     DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
     COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
	  FILES
	  matplotsink.py
	  DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
	  COMPONENT "input_python"
)

GR_PYTHON_INSTALL(
	 FILES
	 plot_sink.py
	 DESTINATION ${GR_PYTHON_DIR}/gnuradio/input
	 COMPONENT "input_python"
)










########################################################################
# Handle the unit tests
########################################################################
if(ENABLE_TESTING)

list(APPEND GR_TEST_PYTHON_DIRS
    ${CMAKE_BINARY_DIR}/gr-input/python
)
list(APPEND GR_TEST_TARGET_DEPS gnuradio-input)

include(GrTest)
file(GLOB py_qa_test_files "qa_*.py")
foreach(py_qa_test_file ${py_qa_test_files})
    get_filename_component(py_qa_test_name ${py_qa_test_file} NAME_WE)
    GR_ADD_TEST(${py_qa_test_name} ${PYTHON_EXECUTABLE} ${PYTHON_DASH_B} ${py_qa_test_file})
endforeach(py_qa_test_file)
endif(ENABLE_TESTING)
