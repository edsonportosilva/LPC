#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Receptor AM super-heterodino
# Generated: Fri Oct 30 11:51:06 2020
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
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class Labo3_4(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Receptor AM super-heterodino")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Receptor AM super-heterodino")
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

        self.settings = Qt.QSettings("GNU Radio", "Labo3_4")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sintonia = sintonia = 100e3
        self.samp_rate = samp_rate = 400e3
        self.portadora = portadora = 100e3
        self.fi = fi = 25e3
        self.audio_rate = audio_rate = 44100
        self.amplitude = amplitude = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._sintonia_range = Range(50e3, 150e3, 1000, 100e3, 200)
        self._sintonia_win = RangeWidget(self._sintonia_range, self.set_sintonia, 'Sintonia', "counter_slider", float)
        self.top_grid_layout.addWidget(self._sintonia_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._portadora_range = Range(75e3, 150e3, 25e3, 100e3, 200)
        self._portadora_win = RangeWidget(self._portadora_range, self.set_portadora, 'Freq. Portadora', "counter_slider", float)
        self.top_grid_layout.addWidget(self._portadora_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._amplitude_range = Range(0, 1, 0.01, 0.5, 200)
        self._amplitude_win = RangeWidget(self._amplitude_range, self.set_amplitude, 'Amp.  Portadora', "counter_slider", float)
        self.top_grid_layout.addWidget(self._amplitude_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024*2, #size
        	samp_rate, #samp_rate
        	"Sinais de Voz de Entrada e Modulado", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Entrada', 'Modulado', '', '', '',
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
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_5 = qtgui.freq_sink_f(
        	2**13, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'Espectro do Sinal Modulante e Modulado', #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_5.set_update_time(0.10)
        self.qtgui_freq_sink_x_5.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_5.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_5.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_5.enable_autoscale(True)
        self.qtgui_freq_sink_x_5.enable_grid(True)
        self.qtgui_freq_sink_x_5.set_fft_average(1.0)
        self.qtgui_freq_sink_x_5.enable_axis_labels(True)
        self.qtgui_freq_sink_x_5.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_5.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_5.set_plot_pos_half(not True)

        labels = ['Modulante', 'Modulado', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_5.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_5.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_5.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_5.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_5.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_5_win = sip.wrapinstance(self.qtgui_freq_sink_x_5.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_5_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_3 = qtgui.freq_sink_f(
        	2**13, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'Espectro de FI e Desmodulado', #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_3.set_update_time(0.10)
        self.qtgui_freq_sink_x_3.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_3.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_3.enable_autoscale(True)
        self.qtgui_freq_sink_x_3.enable_grid(True)
        self.qtgui_freq_sink_x_3.set_fft_average(1.0)
        self.qtgui_freq_sink_x_3.enable_axis_labels(True)
        self.qtgui_freq_sink_x_3.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_3.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_3.set_plot_pos_half(not True)

        labels = ['FI', 'Desmodulado', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_3_win = sip.wrapinstance(self.qtgui_freq_sink_x_3.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_3_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.oscilador_local = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sintonia+fi, 1, 0)
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	10, samp_rate, 5e3, 1e3, firdes.WIN_RECTANGULAR, 6.76))
        self.dc_blocker_xx_0_0 = filter.dc_blocker_ff(600, True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('C:\\Users\\edson\\Google Drive\\Experimentos GRC\\Aula 3\\Labo3-4_fs44100.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate, fi-10e3, fi+10e3, 1000, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(44100, '', True)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=samp_rate,
        	audio_decim=1,
        	audio_pass=10e3,
        	audio_stop=10500,
        )
        self.analog_agc_xx_0_0 = analog.agc_ff(1e-3, 0.05, 1.0)
        self.analog_agc_xx_0_0.set_max_gain(65536)
        self.analog_agc_xx_0 = analog.agc_ff(1e-3, 0.05, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)
        self.Portadora = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, portadora, 1, 0)
        self.Amplitude_Portadora = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, amplitude)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.Amplitude_Portadora, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.Portadora, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_agc_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_agc_xx_0, 0), (self.qtgui_freq_sink_x_5, 0))
        self.connect((self.analog_agc_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.analog_agc_xx_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_am_demod_cf_0, 0), (self.dc_blocker_xx_0_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_freq_sink_x_3, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.analog_am_demod_cf_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_5, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_wavfile_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.dc_blocker_xx_0_0, 0), (self.analog_agc_xx_0_0, 0))
        self.connect((self.dc_blocker_xx_0_0, 0), (self.qtgui_freq_sink_x_3, 1))
        self.connect((self.low_pass_filter_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.oscilador_local, 0), (self.blocks_multiply_xx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Labo3_4")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sintonia(self):
        return self.sintonia

    def set_sintonia(self, sintonia):
        self.sintonia = sintonia
        self.oscilador_local.set_frequency(self.sintonia+self.fi)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_5.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_3.set_frequency_range(0, self.samp_rate)
        self.oscilador_local.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(10, self.samp_rate, 5e3, 1e3, firdes.WIN_RECTANGULAR, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.fi-10e3, self.fi+10e3, 1000, firdes.WIN_HAMMING, 6.76))
        self.Portadora.set_sampling_freq(self.samp_rate)

    def get_portadora(self):
        return self.portadora

    def set_portadora(self, portadora):
        self.portadora = portadora
        self.Portadora.set_frequency(self.portadora)

    def get_fi(self):
        return self.fi

    def set_fi(self, fi):
        self.fi = fi
        self.oscilador_local.set_frequency(self.sintonia+self.fi)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.fi-10e3, self.fi+10e3, 1000, firdes.WIN_HAMMING, 6.76))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.Amplitude_Portadora.set_offset(self.amplitude)


def main(top_block_cls=Labo3_4, options=None):

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
