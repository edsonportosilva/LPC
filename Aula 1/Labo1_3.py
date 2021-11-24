#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Analise de distorcao de canal
# Author: Leocarlos Bezerra da Silva Lima
# Description: Experimento para Laboratório de Princípios de Comunicações. Departamento de Engenharia Elétrica - DEE da Universidade Federal de Campina Grande - UFCG.
# Generated: Wed Nov 24 13:12:00 2021
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


class Labo1_3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Analise de distorcao de canal")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Analise de distorcao de canal")
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

        self.settings = Qt.QSettings("GNU Radio", "Labo1_3")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.theta3 = theta3 = 0
        self.theta2 = theta2 = 0
        self.theta1 = theta1 = 0
        self.samp_rate = samp_rate = 8000
        self.a3 = a3 = 1
        self.a2 = a2 = 1
        self.a1 = a1 = 1

        ##################################################
        # Blocks
        ##################################################
        self.Tab = Qt.QTabWidget()
        self.Tab_widget_0 = Qt.QWidget()
        self.Tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_widget_0)
        self.Tab_grid_layout_0 = Qt.QGridLayout()
        self.Tab_layout_0.addLayout(self.Tab_grid_layout_0)
        self.Tab.addTab(self.Tab_widget_0, 'Deslocamento de fase ')
        self.Tab_widget_1 = Qt.QWidget()
        self.Tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tab_widget_1)
        self.Tab_grid_layout_1 = Qt.QGridLayout()
        self.Tab_layout_1.addLayout(self.Tab_grid_layout_1)
        self.Tab.addTab(self.Tab_widget_1, 'Ganho/Atenuacao ')
        self.top_grid_layout.addWidget(self.Tab, 4, 0, 2, 4)
        for r in range(4, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._theta3_range = Range(0, 20000, 500, 0, 200)
        self._theta3_win = RangeWidget(self._theta3_range, self.set_theta3, 'Fase da senoide de 500 Hz', "counter_slider", float)
        self.Tab_grid_layout_0.addWidget(self._theta3_win, 3, 0, 1, 2)
        for r in range(3, 4):
            self.Tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.Tab_grid_layout_0.setColumnStretch(c, 1)
        self._theta2_range = Range(0, 20000, 500, 0, 200)
        self._theta2_win = RangeWidget(self._theta2_range, self.set_theta2, 'Fase da senoide de 300 Hz', "counter_slider", float)
        self.Tab_grid_layout_0.addWidget(self._theta2_win, 2, 0, 1, 2)
        for r in range(2, 3):
            self.Tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.Tab_grid_layout_0.setColumnStretch(c, 1)
        self._theta1_range = Range(0, 20000, 500, 0, 100)
        self._theta1_win = RangeWidget(self._theta1_range, self.set_theta1, 'Fase da senoide de 100 Hz', "counter_slider", float)
        self.Tab_grid_layout_0.addWidget(self._theta1_win, 0, 0, 1, 2)
        for r in range(0, 1):
            self.Tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.Tab_grid_layout_0.setColumnStretch(c, 1)
        self._a3_range = Range(0, 2, 0.1, 1, 200)
        self._a3_win = RangeWidget(self._a3_range, self.set_a3, 'Amplitude da senoide de 500 Hz', "counter_slider", float)
        self.Tab_grid_layout_1.addWidget(self._a3_win, 2, 0, 1, 2)
        for r in range(2, 3):
            self.Tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.Tab_grid_layout_1.setColumnStretch(c, 1)
        self._a2_range = Range(0, 2, 0.1, 1, 200)
        self._a2_win = RangeWidget(self._a2_range, self.set_a2, 'Amplitude da senoide de 300 Hz', "counter_slider", float)
        self.Tab_grid_layout_1.addWidget(self._a2_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.Tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.Tab_grid_layout_1.setColumnStretch(c, 1)
        self._a1_range = Range(0, 2, 0.1, 1, 200)
        self._a1_win = RangeWidget(self._a1_range, self.set_a1, 'Amplitude da senoide de 100 Hz', "counter_slider", float)
        self.Tab_grid_layout_1.addWidget(self._a1_win, 0, 0, 1, 2)
        for r in range(0, 1):
            self.Tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.Tab_grid_layout_1.setColumnStretch(c, 1)
        self.somador_0 = blocks.add_vff(1)
        self.somador = blocks.add_vff(1)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	2048, #size
        	firdes.WIN_RECTANGULAR, #wintype
        	0, #fc
        	samp_rate/4, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-60, 0)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not False)

        labels = ['Entrada', 'Saida', '', '', '',
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0, 2, 2, 2)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.harmonica_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 500, 0.2, 0)
        self.harmonica_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 300, -0.333, 0)
        self.graf_tempo = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.graf_tempo.set_update_time(0.1)
        self.graf_tempo.set_y_axis(-1.5, 1.5)

        self.graf_tempo.set_y_label('Amplitude', "")

        self.graf_tempo.enable_tags(-1, True)
        self.graf_tempo.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.graf_tempo.enable_autoscale(False)
        self.graf_tempo.enable_grid(True)
        self.graf_tempo.enable_axis_labels(True)
        self.graf_tempo.enable_control_panel(False)
        self.graf_tempo.enable_stem_plot(False)

        if not True:
          self.graf_tempo.disable_legend()

        labels = ['Entrada', 'Saida', '', '', '',
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
                self.graf_tempo.set_line_label(i, "Data {0}".format(i))
            else:
                self.graf_tempo.set_line_label(i, labels[i])
            self.graf_tempo.set_line_width(i, widths[i])
            self.graf_tempo.set_line_color(i, colors[i])
            self.graf_tempo.set_line_style(i, styles[i])
            self.graf_tempo.set_line_marker(i, markers[i])
            self.graf_tempo.set_line_alpha(i, alphas[i])

        self._graf_tempo_win = sip.wrapinstance(self.graf_tempo.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._graf_tempo_win, 0, 0, 2, 2)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fundamental = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 100, 1, 0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vff((a3, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((a2, ))
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, int(theta3/(2*3.14*500)))
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, int(theta2/(2*3.14*300)))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, int(theta1/(2*3.14*100)))
        self.A1 = blocks.multiply_const_vff((a1, ))
        (self.A1).set_block_alias("A1")



        ##################################################
        # Connections
        ##################################################
        self.connect((self.A1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.somador, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.somador, 1))
        self.connect((self.blocks_delay_0_1, 0), (self.somador, 2))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.A1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.somador_0, 0))
        self.connect((self.fundamental, 0), (self.blocks_throttle_0, 0))
        self.connect((self.harmonica_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.harmonica_1, 0), (self.somador_0, 1))
        self.connect((self.harmonica_2, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.harmonica_2, 0), (self.somador_0, 2))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.somador, 0), (self.graf_tempo, 0))
        self.connect((self.somador, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.somador_0, 0), (self.graf_tempo, 1))
        self.connect((self.somador_0, 0), (self.rational_resampler_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Labo1_3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_theta3(self):
        return self.theta3

    def set_theta3(self, theta3):
        self.theta3 = theta3
        self.blocks_delay_0_1.set_dly(int(self.theta3/(2*3.14*500)))

    def get_theta2(self):
        return self.theta2

    def set_theta2(self, theta2):
        self.theta2 = theta2
        self.blocks_delay_0_0.set_dly(int(self.theta2/(2*3.14*300)))

    def get_theta1(self):
        return self.theta1

    def set_theta1(self, theta1):
        self.theta1 = theta1
        self.blocks_delay_0.set_dly(int(self.theta1/(2*3.14*100)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/4)
        self.harmonica_2.set_sampling_freq(self.samp_rate)
        self.harmonica_1.set_sampling_freq(self.samp_rate)
        self.graf_tempo.set_samp_rate(self.samp_rate)
        self.fundamental.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_a3(self):
        return self.a3

    def set_a3(self, a3):
        self.a3 = a3
        self.blocks_multiply_const_vxx_0_1.set_k((self.a3, ))

    def get_a2(self):
        return self.a2

    def set_a2(self, a2):
        self.a2 = a2
        self.blocks_multiply_const_vxx_0_0.set_k((self.a2, ))

    def get_a1(self):
        return self.a1

    def set_a1(self, a1):
        self.a1 = a1
        self.A1.set_k((self.a1, ))


def main(top_block_cls=Labo1_3, options=None):

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
