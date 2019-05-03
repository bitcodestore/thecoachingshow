# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Sourced From Online Templates And Guides
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Thanks To: Google Search For This Template
# Modified: Pulse
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.thecoachingshow'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_1 = "PLBW_HK0I-OKIMOS1PEB_OIuMhoJubOwxp"
YOUTUBE_CHANNEL_ID_2 = "PLBW_HK0I-OKIj2LBDGM7Kglp5hkMvHdHd"
YOUTUBE_CHANNEL_ID_3 = "PLw6p6PA8M2miu0w4K1g6vQ1BHUBeyM4_-"
YOUTUBE_CHANNEL_ID_4 = "PLy8LfIp6j3aK2vtj-Xjhk8j5sAzGGrn0c"
YOUTUBE_CHANNEL_ID_5 = "PL4997816004E33B57"
YOUTUBE_CHANNEL_ID_6 = "PLKX9ut-1fNpg0VULPOAytjAgMG7uMDPvx"
YOUTUBE_CHANNEL_ID_7 = "LLHm_D4kNQaRshalYoB1qtbw"
YOUTUBE_CHANNEL_ID_8 = "PL2DADA850ADEEEAFC"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))
	
    plugintools.add_item( 
        #action="", 
        title="Antonio Lara",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://www.thecoachingshow.net/images/speakers/speaker1.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Eduardo Sánchez",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://www.thecoachingshow.net/images/speakers/speaker2.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Luis Font",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://www.thecoachingshow.net/images/speakers/speaker3.jpg",
        folder=True )
	

    plugintools.add_item( 
        #action="", 
        title="Ana Merlino",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://www.thecoachingshow.net/images/speakers/speaker5.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Ester Vega",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://www.thecoachingshow.net/images/speakers/speaker7.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Edu Arjona",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://www.thecoachingshow.net/images/speakers/speaker6.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Vanessa Martínez",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://www.thecoachingshow.net/images/speakers/speaker8.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Otikko Cardona",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://www.thecoachingshow.net/images/speakers/speaker9.jpg",
        folder=True )


run()