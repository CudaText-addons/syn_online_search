import os
import webbrowser
from urllib.parse import quote
from sw import *

LIST = {
    'Wikipedia': 'http://en.wikipedia.org/w/index.php?title=Special:Search&search={sel}',
    'Google': 'http://www.google.com/search?q={sel}',
    'MSDN': 'http://social.msdn.microsoft.com/Search/en-US?query={sel}',
    'HTML4': 'http://www.w3schools.com/tags/tag_{word}.asp',
    'HTML5': 'http://www.w3.org/TR/html-markup/{word}.html',
    'PHP.net': 'http://www.php.net/{word}',
    }
    

def work(name):
    if not name in LIST:
        msg_status('Cannot find name: '+name)
        return
    if not ed.get_sel_mode()==SEL_NORMAL:
        msg_status('Can use only normal selection')
        return

    #word
    _, __, s_word = ed.get_word(*ed.get_caret_xy())
         
    #sel
    s_sel = ed.get_text_sel()
    s_sel = s_sel.replace(' ', '+')
    if not s_sel:
        s_sel = s_word
        
    s_sel = quote(s_sel)
    s_word = quote(s_word)
        
    s = LIST[name]
    s = s.replace('{sel}', s_sel)
    s = s.replace('{word}', s_word)
    
    msg_status('Opening browser: '+s) 
    webbrowser.open_new_tab(s)
    

class Command:
    def do_wikipedia(self):
        work('Wikipedia')
    def do_google(self):
        work('Google')
    def do_msdn(self):
        work('MSDN')
    def do_html4(self):
        work('HTML4')
    def do_html5(self):
        work('HTML5')
    def do_php(self):
        work('PHP.net')
