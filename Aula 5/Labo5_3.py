#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Labo5 3
# Generated: Mon May 10 15:30:02 2021
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

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class Labo5_3(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Labo5 3")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 16
        self.samp_rate = samp_rate = 32000

        self.modQAM_constellationObj = modQAM_constellationObj = digital.constellation_qpsk().base()

        self.RRCrolloff = RRCrolloff = 2
        self.M = M = 2
        self.BW = BW = (samp_rate/sps)

        ##################################################
        # Blocks
        ##################################################
        _BW_sizer = wx.BoxSizer(wx.VERTICAL)
        self._BW_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_BW_sizer,
        	value=self.BW,
        	callback=self.set_BW,
        	label='BW',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._BW_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_BW_sizer,
        	value=self.BW,
        	callback=self.set_BW,
        	minimum=(samp_rate/sps)*0.25,
        	maximum=(samp_rate/sps)*2,
        	num_steps=50,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_BW_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Diagrama de olho',
        	sample_rate=samp_rate,
        	v_scale=0.1,
        	v_offset=0,
        	t_scale=(sps/samp_rate)*4,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_FREE,
        	y_axis_label='Amplitude',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0_1 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=5,
        	y_divs=10,
        	ref_level=-43,
        	ref_scale=2.0,
        	sample_rate=samp_rate/4,
        	fft_size=4096,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.40,
        	title='Espectro NRZ',
        	peak_hold=False,
        	win=window.blackmanharris,
        )
        self.GridAdd(self.wxgui_fftsink2_0_1.win, 0, 1, 1, 1)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=5,
        	y_divs=10,
        	ref_level=-38,
        	ref_scale=2.0,
        	sample_rate=samp_rate/4,
        	fft_size=4096,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.40,
        	title='Espectro Duobinary ',
        	peak_hold=False,
        	win=window.blackmanharris,
        )
        self.GridAdd(self.wxgui_fftsink2_0.win, 0, 2, 1, 1)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=sps/4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=sps/4,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0_0_0_0 = filter.interp_fir_filter_ccf(1, firdes.low_pass(
        	0.08, samp_rate, samp_rate/sps/2, (samp_rate/sps), firdes.WIN_RECTANGULAR, 100))
        self.low_pass_filter_0_0_0 = filter.interp_fir_filter_ccf(1, firdes.low_pass(
        	0.08, samp_rate, samp_rate/sps/2, (samp_rate/sps), firdes.WIN_RECTANGULAR, 100))
        self.low_pass_filter_0_0 = filter.interp_fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, BW, BW*0.05, firdes.WIN_RECTANGULAR, 1000))
        self.low_pass_filter_0 = filter.interp_fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, BW, BW*0.05, firdes.WIN_RECTANGULAR, 1000))
        self.digital_qam_mod_0 = digital.qam.qam_mod(
          constellation_points=M**2,
          mod_code="gray",
          differential=False,
          samples_per_symbol=sps,
          excess_bw=RRCrolloff,
          verbose=False,
          log=False,
          )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, sps)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((-0.2, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((0.2, ))
        self.analog_random_source_x_1 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 10000)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_1, 0), (self.digital_qam_mod_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.low_pass_filter_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.wxgui_fftsink2_0_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.wxgui_fftsink2_0, 0))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_BW((self.samp_rate/self.sps))
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(0.08, self.samp_rate, self.samp_rate/self.sps/2, (self.samp_rate/self.sps), firdes.WIN_RECTANGULAR, 100))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(0.08, self.samp_rate, self.samp_rate/self.sps/2, (self.samp_rate/self.sps), firdes.WIN_RECTANGULAR, 100))
        self.blocks_delay_0.set_dly(self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_BW((self.samp_rate/self.sps))
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_1.set_sample_rate(self.samp_rate/4)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate/4)
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(0.08, self.samp_rate, self.samp_rate/self.sps/2, (self.samp_rate/self.sps), firdes.WIN_RECTANGULAR, 100))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(0.08, self.samp_rate, self.samp_rate/self.sps/2, (self.samp_rate/self.sps), firdes.WIN_RECTANGULAR, 100))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.BW*0.05, firdes.WIN_RECTANGULAR, 1000))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.BW*0.05, firdes.WIN_RECTANGULAR, 1000))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_modQAM_constellationObj(self):
        return self.modQAM_constellationObj

    def set_modQAM_constellationObj(self, modQAM_constellationObj):
        self.modQAM_constellationObj = modQAM_constellationObj

    def get_RRCrolloff(self):
        return self.RRCrolloff

    def set_RRCrolloff(self, RRCrolloff):
        self.RRCrolloff = RRCrolloff

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self._BW_slider.set_value(self.BW)
        self._BW_text_box.set_value(self.BW)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.BW*0.05, firdes.WIN_RECTANGULAR, 1000))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.BW*0.05, firdes.WIN_RECTANGULAR, 1000))


def main(top_block_cls=Labo5_3, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
