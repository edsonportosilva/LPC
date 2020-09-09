#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Nov 28 18:07:39 2019
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import numpy
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.samp_rate = samp_rate = 64000
        self.noiseAmp = noiseAmp = 0.0010
        self.RRCrolloff = RRCrolloff = 0.05
        self.M = M = 4

        ##################################################
        # Blocks
        ##################################################
        self._noiseAmp_range = Range(0, 2, 0.001, 0.0010, 400)
        self._noiseAmp_win = RangeWidget(self._noiseAmp_range, self.set_noiseAmp, 'Variancia do ruido', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noiseAmp_win, 3, 0, 1, 2)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.root_raised_cosine_filter_0_0_1_1 = filter.fir_filter_ccf(sps, firdes.root_raised_cosine(
        	1, samp_rate, samp_rate/sps, RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0_1_0 = filter.fir_filter_ccf(sps, firdes.root_raised_cosine(
        	1, samp_rate, samp_rate/sps, RRCrolloff, 4001))
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=2,
                decimation=1,
                taps=(0.5, ),
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=2,
                decimation=1,
                taps=(0.5, ),
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	'Sinal modulado no tempo', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_1.set_update_time(0.10)
        self.qtgui_number_sink_1.set_title('Taxa de erro de bit [Bit error rate (BER)]')

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_1.set_min(i, -1)
            self.qtgui_number_sink_1.set_max(i, 1)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])

        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_1_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0.1,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title('SNR por bit [Eb/No] (dB)')

        labels = ['SNR per bit', '', '', '', '',
                  '', '', '', '', '']
        units = ['dB', '', '', '', '',
                 '', '', '', '', '']
        colors = [("white", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'Espectro do sinal modulado', #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-120, -20)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['Sinal + Ruido', 'Sinal ', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 1, 0, 2, 1)
        for r in range(1, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_qam_mod_0 = digital.qam.qam_mod(
          constellation_points=M,
          mod_code="gray",
          differential=False,
          samples_per_symbol=sps,
          excess_bw=RRCrolloff,
          verbose=False,
          log=False,
          )
        self.digital_qam_demod_0_0 = digital.qam.qam_demod(
          constellation_points=M,
          differential=False,
          samples_per_symbol=2,
          excess_bw=1,
          freq_bw=0,
          timing_bw=0,
          phase_bw=0,
          mod_code="gray",
          verbose=False,
          log=False,
          )
        self.digital_qam_demod_0 = digital.qam.qam_demod(
          constellation_points=M,
          differential=False,
          samples_per_symbol=2,
          excess_bw=1,
          freq_bw=0,
          timing_bw=0,
          phase_bw=0,
          mod_code="gray",
          verbose=False,
          log=False,
          )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_sub_xx_0_0 = blocks.sub_cc(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_nlog10_ff_0_1 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((numpy.log2(M)/1.2589, ))
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(20000, 1, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(20000, 1, 4000, 1)
        self.blocks_complex_to_mag_squared_2_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_2 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=50000*numpy.int(numpy.log2(M)),
        	bits_per_symbol=numpy.int(numpy.log2(M)),
        )
        self.analog_random_source_x_1 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000000)), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, numpy.sqrt(noiseAmp), numpy.int(numpy.log2(M)))
        self.Constelacoes = qtgui.const_sink_c(
        	4096, #size
        	'Diagrama de constelacoes', #name
        	2 #number of inputs
        )
        self.Constelacoes.set_update_time(0.05)
        self.Constelacoes.set_y_axis(-1.5, 1.5)
        self.Constelacoes.set_x_axis(-1.5, 1.5)
        self.Constelacoes.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.Constelacoes.enable_autoscale(False)
        self.Constelacoes.enable_grid(True)
        self.Constelacoes.enable_axis_labels(True)

        if not True:
          self.Constelacoes.disable_legend()

        labels = ['Recebida', 'Transmitida', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.Constelacoes.set_line_label(i, "Data {0}".format(i))
            else:
                self.Constelacoes.set_line_label(i, labels[i])
            self.Constelacoes.set_line_width(i, widths[i])
            self.Constelacoes.set_line_color(i, colors[i])
            self.Constelacoes.set_line_style(i, styles[i])
            self.Constelacoes.set_line_marker(i, markers[i])
            self.Constelacoes.set_line_alpha(i, alphas[i])

        self._Constelacoes_win = sip.wrapinstance(self.Constelacoes.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Constelacoes_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_source_x_1, 0), (self.digital_qam_mod_0, 0))
        self.connect((self.blks2_error_rate_0, 0), (self.qtgui_number_sink_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.root_raised_cosine_filter_0_0_1_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_2, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_2_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.blocks_nlog10_ff_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_nlog10_ff_0_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.blocks_complex_to_mag_squared_2, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_qam_demod_0, 0), (self.blks2_error_rate_0, 0))
        self.connect((self.digital_qam_demod_0_0, 0), (self.blks2_error_rate_0, 1))
        self.connect((self.digital_qam_mod_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.digital_qam_mod_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.root_raised_cosine_filter_0_0_1_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.digital_qam_demod_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.digital_qam_demod_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0_1_0, 0), (self.Constelacoes, 1))
        self.connect((self.root_raised_cosine_filter_0_0_1_0, 0), (self.blocks_complex_to_mag_squared_2_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0_1_0, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0_1_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0_1_1, 0), (self.Constelacoes, 0))
        self.connect((self.root_raised_cosine_filter_0_0_1_1, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.root_raised_cosine_filter_0_0_1_1, 0), (self.rational_resampler_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.root_raised_cosine_filter_0_0_1_1.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0_1_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.root_raised_cosine_filter_0_0_1_1.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0_1_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noiseAmp(self):
        return self.noiseAmp

    def set_noiseAmp(self, noiseAmp):
        self.noiseAmp = noiseAmp
        self.analog_noise_source_x_0.set_amplitude(numpy.sqrt(self.noiseAmp))

    def get_RRCrolloff(self):
        return self.RRCrolloff

    def set_RRCrolloff(self, RRCrolloff):
        self.RRCrolloff = RRCrolloff
        self.root_raised_cosine_filter_0_0_1_1.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))
        self.root_raised_cosine_filter_0_0_1_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/self.sps, self.RRCrolloff, 4001))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.blocks_multiply_const_vxx_0.set_k((numpy.log2(self.M)/1.2589, ))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
