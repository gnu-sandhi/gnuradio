#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Apr  7 16:42:08 2015
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import gr, blocks
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import gnuradio.input.Comparator
import gnuradio.input.Denominator
import gnuradio.input.Numerator
import gnuradio.input.Response
import gnuradio.input.plot_sink
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.plot_sink_0_0 = gnuradio.input.plot_sink.plot_sink_f(
			self.GetWin(),
			title="Scope Plot",
			vlen=1,
			decim=1,
			gsz=500,
			zoom=0,
		)
		self.Add(self.plot_sink_0_0.win)
		self.plot_sink_0 = gnuradio.input.plot_sink.plot_sink_f(
			self.GetWin(),
			title="Scope Plot",
			vlen=1,
			decim=1,
			gsz=500,
			zoom=0,
		)
		self.Add(self.plot_sink_0.win)
		self.const_source_x_0_3_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 1)
		self.const_source_x_0_3 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 0)
		self.const_source_x_0_2 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 0)
		self.const_source_x_0_1 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 3)
		self.const_source_x_0_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 36)
		self.const_source_x_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 36)
		self.blocks_file_meta_sink_0 = blocks.file_meta_sink(gr.sizeof_float*1, "test.grc", samp_rate, 1, blocks.GR_FILE_FLOAT, False, 1000000, "", False)
		self.blocks_file_meta_sink_0.set_unbuffered(False)
		self.Transfer_function_Response_0 = gnuradio.input.Response.Response(2,12,0,500,1)
		self.Transfer_function_Numerator_0 = gnuradio.input.Numerator.Numerator(2)
		self.Transfer_function_Denominator_0 = gnuradio.input.Denominator.Denominator(2)
		self.Comparator_0 = gnuradio.input.Comparator.Comparator(36, 5, -5)

		##################################################
		# Connections
		##################################################
		self.connect((self.Transfer_function_Denominator_0, 0), (self.Transfer_function_Response_0, 1))
		self.connect((self.Transfer_function_Numerator_0, 0), (self.Transfer_function_Response_0, 0))
		self.connect((self.const_source_x_0_3_0, 0), (self.Transfer_function_Denominator_0, 0))
		self.connect((self.const_source_x_0_0, 0), (self.Transfer_function_Denominator_0, 2))
		self.connect((self.const_source_x_0_1, 0), (self.Transfer_function_Denominator_0, 1))
		self.connect((self.const_source_x_0_3, 0), (self.Transfer_function_Numerator_0, 2))
		self.connect((self.const_source_x_0_2, 0), (self.Transfer_function_Numerator_0, 1))
		self.connect((self.const_source_x_0, 0), (self.Transfer_function_Numerator_0, 0))
		self.connect((self.Transfer_function_Response_0, 0), (self.Comparator_0, 0))
		self.connect((self.Comparator_0, 0), (self.plot_sink_0, 0))
		self.connect((self.Transfer_function_Response_0, 0), (self.plot_sink_0_0, 0))
		self.connect((self.Transfer_function_Response_0, 0), (self.blocks_file_meta_sink_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

