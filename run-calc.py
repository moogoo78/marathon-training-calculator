#!/usr/bin/env python
# -.- coding: utf-8 -.-

import sys
import math
    
def main(d=0, t=''):
    """
    marathon training calculator
    """
 
    t_list = t.split(':')
    hh = 0 if len(t_list) == 2 else int(t_list[0])
    mm = int(t_list[-2])
    ss = int(t_list[-1])
    secs = (hh * 3600) + (mm * 60) + ss

    print '\nrun-calc'
    print '---------'
    print '%.01fkm in %s' % (d, t)
    # seconds per km    
    m, s = divmod(secs/d, 60)
    print '=> %.2f min/km (%02d:%02d)' % (secs/(d*60), m, s)
    #seconds per round
    spr = secs/d/2.5
    m, s = divmod(spr, 60)
    print '=> %d sec/round (%02d:%02d)' % (spr, m, s)
    m, s = divmod((secs/d)*52.5, 60) # 5(k) * 10.5
    h, m = divmod(m, 60)
    # predict a full marathon    
    print '=> ~ %02d:%02d:%02d' % (h, m, s)


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        d = float(sys.argv[1])
        t = sys.argv[2]
    else:
        d = float(raw_input('running distance? (km) '))
        t = raw_input('running time? (hh:mm:ss) ')
    main(d, t)
