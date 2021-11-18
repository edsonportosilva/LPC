#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Analise de distorcao de canal
# Author: Leocarlos Bezerra da Silva Lima
# Description: Experimento para Laboratório de Princípios de Comunicações. Departamento de Engenharia Elétrica - DEE da Universidade Federal de Campina Grande - UFCG.
# Generated: Fri Nov  6 14:38:52 2020
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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
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
        self.samp_rate = samp_rate = 8000
        self.atraso = atraso = 0
        self.atenuacao = atenuacao = 1

        ##################################################
        # Blocks
        ##################################################
        self.somador_0 = blocks.add_vff(1)
        self.somador = blocks.add_vff(1)
        self.harmonica_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 500, 0.2, 0)
        self.harmonica_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 300, -0.333, 0)
        self.graf_tempo = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.graf_tempo.set_update_time(0.10)
        self.graf_tempo.set_y_axis(-1, 1)

        self.graf_tempo.set_y_label('Amplitude', "")

        self.graf_tempo.enable_tags(-1, True)
        self.graf_tempo.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.graf_tempo.enable_autoscale(True)
        self.graf_tempo.enable_grid(True)
        self.graf_tempo.enable_axis_labels(True)
        self.graf_tempo.enable_control_panel(False)
        self.graf_tempo.enable_stem_plot(False)

        if not True:
          self.graf_tempo.disable_legend()

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
                self.graf_tempo.set_line_label(i, "Data {0}".format(i))
            else:
                self.graf_tempo.set_line_label(i, labels[i])
            self.graf_tempo.set_line_width(i, widths[i])
            self.graf_tempo.set_line_color(i, colors[i])
            self.graf_tempo.set_line_style(i, styles[i])
            self.graf_tempo.set_line_marker(i, markers[i])
            self.graf_tempo.set_line_alpha(i, alphas[i])

        self._graf_tempo_win = sip.wrapinstance(self.graf_tempo.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._graf_tempo_win)
        self.fundamental = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 100, 1, 0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vff((atenuacao, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((atenuacao, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((atenuacao, ))
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, atraso)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, atraso)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, atraso)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_delay_0, 0), (self.somador, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.somador, 1))
        self.connect((self.blocks_delay_0_1, 0), (self.somador, 2))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.somador_0, 0))
        self.connect((self.fundamental, 0), (self.blocks_throttle_0, 0))
        self.connect((self.harmonica_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.harmonica_1, 0), (self.somador_0, 1))
        self.connect((self.harmonica_2, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.harmonica_2, 0), (self.somador_0, 2))
        self.connect((self.somador, 0), (self.graf_tempo, 0))
        self.connect((self.somador_0, 0), (self.graf_tempo, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Labo1_3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.harmonica_2.set_sampling_freq(self.samp_rate)
        self.harmonica_1.set_sampling_freq(self.samp_rate)
        self.graf_tempo.set_samp_rate(self.samp_rate)
        self.fundamental.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_atraso(self):
        return self.atraso

    def set_atraso(self, atraso):
        self.atraso = atraso
        self.blocks_delay_0_1.set_dly(self.atraso)
        self.blocks_delay_0_0.set_dly(self.atraso)
        self.blocks_delay_0.set_dly(self.atraso)

    def get_atenuacao(self):
        return self.atenuacao

    def set_atenuacao(self, atenuacao):
        self.atenuacao = atenuacao
        self.blocks_multiply_const_vxx_0_1.set_k((self.atenuacao, ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.atenuacao, ))
        self.blocks_multiply_const_vxx_0.set_k((self.atenuacao, ))


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
