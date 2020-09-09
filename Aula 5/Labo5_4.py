#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Labo5 4
# Generated: Fri May 24 09:31:08 2019
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
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class Labo5_4(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Labo5 4")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 16
        self.samp_rate = samp_rate = 32000
        self.noiseAmp = noiseAmp = 0.1

        self.modQAM_constellationObj = modQAM_constellationObj = digital.constellation_16qam().base()

        self.bitsPerSymbol = bitsPerSymbol = 2
        self.RRCrolloff = RRCrolloff = 1

        ##################################################
        # Blocks
        ##################################################
        _noiseAmp_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noiseAmp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noiseAmp_sizer,
        	value=self.noiseAmp,
        	callback=self.set_noiseAmp,
        	label='noiseAmp',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noiseAmp_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noiseAmp_sizer,
        	value=self.noiseAmp,
        	callback=self.set_noiseAmp,
        	minimum=0,
        	maximum=2,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_noiseAmp_sizer)
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title='Constelacao recebida',
        	sample_rate=samp_rate,
        	v_scale=0.5,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=True,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_FREE,
        	y_axis_label='',
        )
        self.GridAdd(self.wxgui_scopesink2_1.win, 0, 0, 2, 2)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Diagrama de olho',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=(sps/samp_rate)*4,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_FREE,
        	y_axis_label='Amplitude',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_numbersink2_0_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit='',
        	minval=0,
        	maxval=1,
        	factor=1.0,
        	decimal_places=2,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label='SNR por bit [EbNo] (dB)',
        	peak_hold=False,
        	show_gauge=True,
        )
        self.GridAdd(self.wxgui_numbersink2_0_0.win, 0, 4, 1, 1)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit='',
        	minval=0,
        	maxval=1,
        	factor=1.0,
        	decimal_places=6,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label='Bit error rate (BER)',
        	peak_hold=False,
        	show_gauge=True,
        )
        self.GridAdd(self.wxgui_numbersink2_0.win, 0, 3, 1, 1)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=4096,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Espectro',
        	peak_hold=False,
        	win=window.blackmanharris,
        )
        self.GridAdd(self.wxgui_fftsink2_0.win, 1, 3, 2, 2)
        self.single_pole_iir_filter_xx_0_0 = filter.single_pole_iir_filter_ff(0.001, 1)
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(0.001, 1)
        self.root_raised_cosine_filter_0_0_1_0 = filter.interp_fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, samp_rate, samp_rate/sps, RRCrolloff*4, 4001))
        self.root_raised_cosine_filter_0_0_1 = filter.interp_fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, samp_rate, samp_rate/sps, RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0_0 = filter.fir_filter_ccf(sps, firdes.root_raised_cosine(
        	1, samp_rate, samp_rate/sps, RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_ccf(sps, firdes.root_raised_cosine(
        	1, samp_rate, samp_rate/sps, RRCrolloff, 4001))
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
          constellation=modQAM_constellationObj,
          differential=False,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=RRCrolloff,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=modQAM_constellationObj,
          differential=False,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=RRCrolloff,
          verbose=False,
          log=False,
          )
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(modQAM_constellationObj)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(modQAM_constellationObj)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_nlog10_ff_0_1 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((bitsPerSymbol, ))
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_squared_2_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_2 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=10000,
        	bits_per_symbol=bitsPerSymbol,
        )
        self.analog_random_source_x_1 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 10000)), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noiseAmp, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.root_raised_cosine_filter_0_0_1, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.blks2_error_rate_0, 0), (self.wxgui_numbersink2_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.root_raised_cosine_filter_0_0_1_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_2, 0), (self.single_pole_iir_filter_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_2_0, 0), (self.single_pole_iir_filter_xx_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_nlog10_ff_0_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.wxgui_numbersink2_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blks2_error_rate_0, 1))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blks2_error_rate_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_complex_to_mag_squared_2_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.root_raised_cosine_filter_0_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.wxgui_scopesink2_1, 0))
        self.connect((self.root_raised_cosine_filter_0_0_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0_1, 0), (self.blocks_complex_to_mag_squared_2, 0))
        self.connect((self.root_raised_cosine_filter_0_0_1_0, 0), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0, 0), (self.blocks_nlog10_ff_0_1, 0))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.root_raised_cosine_filter_0_0_1_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff*4, 4001))
        self.root_raised_cosine_filter_0_0_1.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.root_raised_cosine_filter_0_0_1_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff*4, 4001))
        self.root_raised_cosine_filter_0_0_1.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noiseAmp(self):
        return self.noiseAmp

    def set_noiseAmp(self, noiseAmp):
        self.noiseAmp = noiseAmp
        self._noiseAmp_slider.set_value(self.noiseAmp)
        self._noiseAmp_text_box.set_value(self.noiseAmp)
        self.analog_noise_source_x_0.set_amplitude(self.noiseAmp)

    def get_modQAM_constellationObj(self):
        return self.modQAM_constellationObj

    def set_modQAM_constellationObj(self, modQAM_constellationObj):
        self.modQAM_constellationObj = modQAM_constellationObj

    def get_bitsPerSymbol(self):
        return self.bitsPerSymbol

    def set_bitsPerSymbol(self, bitsPerSymbol):
        self.bitsPerSymbol = bitsPerSymbol
        self.blocks_multiply_const_vxx_0.set_k((self.bitsPerSymbol, ))

    def get_RRCrolloff(self):
        return self.RRCrolloff

    def set_RRCrolloff(self, RRCrolloff):
        self.RRCrolloff = RRCrolloff
        self.root_raised_cosine_filter_0_0_1_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff*4, 4001))
        self.root_raised_cosine_filter_0_0_1.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))


def main(top_block_cls=Labo5_4, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
