# -*- coding: UTF-8 -*-
from gi.repository import Gtk

class Main:
    def __init__(self):
        builder=Gtk.Builder()
        builder.add_from_file('interfaz.glade')
        builder.connect_signals(self)
        self.wprincipal=builder.get_object('wprincipal')
        self.tvtexto=builder.get_object('tvtexto')
        self.wprincipal.show_all()
    
    def aplicar(self, widget):
        bf = self.tvtexto.get_buffer()
        print "fue presionado el botón. Texto:",bf.get_text(bf.get_start_iter(),bf.get_end_iter(),False)
    
    def cerrarApp(self,*args):
        Gtk.main_quit(*args)
        
if __name__ == "__main__":
	hwg = Main()
	Gtk.main()


