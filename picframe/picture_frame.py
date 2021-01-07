import logging
import sys


from picframe import model, viewer_display, controller



def main(): 
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)  # set up logging to stdout
    logger = logging.getLogger("picture_frame.py") # defines logger for picture_fram module
    logger.info('starting %s', sys.argv) # INFO:picture_frame.py:starting ['/usr/local/bin/picture_frame']
    if len(sys.argv) > 1: #if there is more than one CL arguments (a config file) pass it to Model
        m = model.Model(sys.argv[1])
    else:
        m = model.Model() # else call model with default configuration
    v = viewer_display.ViewerDisplay(m.get_viewer_config()) #initialize view_diplay with config data
    c = controller.Controller(m, v) #initialize controller with config from model and viewer
    c.start() #start picture display
    c.loop()
    c.stop()
    
    

if __name__=="__main__": 
    main() 