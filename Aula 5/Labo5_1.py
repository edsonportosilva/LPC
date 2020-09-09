#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Labo5 1
# GNU Radio version: 3.7.13.5
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class Labo5_1(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Labo5 1")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 32
        self.samp_rate = samp_rate = 256000
        self.noisePower = noisePower = 0.0255
        self.RRCrolloff = RRCrolloff = 2
        self.M = M = 2

        ##################################################
        # Blocks
        ##################################################
        _noisePower_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noisePower_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noisePower_sizer,
        	value=self.noisePower,
        	callback=self.set_noisePower,
        	label='Noise power',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noisePower_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noisePower_sizer,
        	value=self.noisePower,
        	callback=self.set_noisePower,
        	minimum=0,
        	maximum=1,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_noisePower_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Diagrama de olho',
        	sample_rate=samp_rate,
        	v_scale=0.50,
        	v_offset=0,
        	t_scale=(sps/samp_rate)*4,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_FREE,
        	y_axis_label='Amplitude',
        )
        self.GridAdd(self.wxgui_scopesink2_0.win, 0, 0, 4, 10)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit='dB',
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=2,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=True,
        	avg_alpha=0.02,
        	label='SNR (dB)',
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0.win)
        self.single_pole_iir_filter_xx_0_0 = filter.single_pole_iir_filter_ff(0.001, 1)
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(0.001, 1)
        self.low_pass_filter_0_0_0_0_0 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, samp_rate/sps/2, (samp_rate/sps)*0.83, firdes.WIN_RECTANGULAR, 1000))
        self.low_pass_filter_0_0_0_0 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, samp_rate/sps/2, (samp_rate/sps)*0.83, firdes.WIN_RECTANGULAR, 1000))
        self.digital_qam_mod_0 = digital.qam.qam_mod(
          constellation_points=M**2,
          mod_code="gray",
          differential=False,
          samples_per_symbol=sps,
          excess_bw=RRCrolloff,
          verbose=False,
          log=False,
          )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_nlog10_ff_0_1 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_complex_to_real_0_1 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_random_source_x_1 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 100000)), True)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, numpy.sqrt(noisePower), 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.low_pass_filter_0_0_0_0_0, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.digital_qam_mod_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.low_pass_filter_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_real_0_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_complex_to_real_0_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_real_0_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.single_pole_iir_filter_xx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.single_pole_iir_filter_xx_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_nlog10_ff_0_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.wxgui_numbersink2_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.blocks_complex_to_real_0_1, 0))
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0, 0), (self.blocks_nlog10_ff_0_1, 0))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.low_pass_filter_0_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.sps/2, (self.samp_rate/self.sps)*0.83, firdes.WIN_RECTANGULAR, 1000))
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.sps/2, (self.samp_rate/self.sps)*0.83, firdes.WIN_RECTANGULAR, 1000))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.sps/2, (self.samp_rate/self.sps)*0.83, firdes.WIN_RECTANGULAR, 1000))
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.sps/2, (self.samp_rate/self.sps)*0.83, firdes.WIN_RECTANGULAR, 1000))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noisePower(self):
        return self.noisePower

    def set_noisePower(self, noisePower):
        self.noisePower = noisePower
        self._noisePower_slider.set_value(self.noisePower)
        self._noisePower_text_box.set_value(self.noisePower)
        self.analog_noise_source_x_0.set_amplitude(numpy.sqrt(self.noisePower))

    def get_RRCrolloff(self):
        return self.RRCrolloff

    def set_RRCrolloff(self, RRCrolloff):
        self.RRCrolloff = RRCrolloff

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M


def main(top_block_cls=Labo5_1, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
