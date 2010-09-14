#!/usr/bin/env python
# -*- coding: UTF-8 -*-




##################################################
## DEPENDENCIES
import sys
import os
import os.path
import __builtin__
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.1'
__CHEETAH_versionTuple__ = (2, 4, 1, 'final', 0)
__CHEETAH_genTime__ = 1284450634.7130001
__CHEETAH_genTimestamp__ = 'Tue Sep 14 15:50:34 2010'
__CHEETAH_src__ = 'D:\\workspace\\python\\weather-china\\src\\home.html'
__CHEETAH_srcLastModified__ = 'Wed Jul 28 10:35:46 2010'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class CompiledTemplate(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(CompiledTemplate, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>\u5929\u6c14\u9884\u62a5</title>
<script type="text/javascript" src="/static/js/jquery.js"></script>
<script type="text/javascript">
var days=["\u661f\u671f\u65e5", "\u661f\u671f\u4e00", "\u661f\u671f\u4e8c", "\u661f\u671f\u4e09", "\u661f\u671f\u56db", "\u661f\u671f\u4e94", "\u661f\u671f\u516d"]
jQuery(document).ready(function() {
  jQuery.getJSON("/api?city=''')
        _v = VFSL([locals()]+SL+[globals(), __builtin__],"city.first_alias",True) # u'${city.first_alias}' on line 11, col 29
        if _v is not None: write(_filter(_v, rawExpr=u'${city.first_alias}')) # from line 11, col 29.
        write(u'''", function(data) {
    var today = data.forecasts[0];
\tvar tomorrow = data.forecasts[1];

    jQuery("#x-today-date").html(today.date);
    jQuery("#x-tomorrow-date").html(tomorrow.date);

    jQuery("#x-today-day").html(days[today.day]);
    jQuery("#x-tomorrow-day").html(days[tomorrow.day]);

    jQuery("#x-today-text").html(today.text);
    jQuery("#x-tomorrow-text").html(tomorrow.text);

    jQuery("#x-today-temp").html(today.low + " ~ " + today.high + "\xb0");
\tjQuery("#x-tomorrow-temp").html(tomorrow.low + " ~ " + tomorrow.high + "\xb0");

    jQuery("#x-today-icon").css("background-image", "url(" + today.image_large + ")");
\tjQuery("#x-tomorrow-icon").css("background-image", "url(" + tomorrow.image_large + ")");
\tjQuery("#x-today-icon-small").css("background-image", "url(" + today.image_small + ")");

    jQuery("#x-pub").html(data.pub);
\tif (data.wind.chill!=null)
\t  jQuery("#x-wind-chill").html(data.wind.chill);
\tif (data.wind.direction!=null)
\t  jQuery("#x-wind-direction").html(data.wind.direction);
\tif (data.wind.speed!=null)
\t  jQuery("#x-wind-speed").html(data.wind.speed);

    if (data.atmosphere.humidity!=null)
\t  jQuery("#x-atmosphere-humidity").html(data.atmosphere.humidity);
    if (data.atmosphere.visibility!=null)
\t  jQuery("#x-atmosphere-visibility").html(data.atmosphere.visibility);
    if (data.atmosphere.pressure!=null)
\t  jQuery("#x-atmosphere-pressure").html(data.atmosphere.pressure);

    if (data.astronomy.sunrise!=null)
\t  jQuery("#x-astronomy-sunrise").html(data.astronomy.sunrise);
    if (data.astronomy.sunset!=null)
\t  jQuery("#x-astronomy-sunset").html(data.astronomy.sunset);
  });
});

function change_city(key){
  if (key=="-")
    return;
  location.assign("/?city=" + key);
}
</script>
<link rel="stylesheet" href="/static/css/screen.css" type="text/css" media="screen, projection">
<link rel="stylesheet" href="/static/css/print.css" type="text/css" media="print">
<!--[if lt IE 8]>
\t<link rel="stylesheet" href="/static/css/ie.css" type="text/css" media="screen, projection">
<![endif]-->
<style type="text/css">
div.w-report span.h {
\tmargin:3px 0px;
\tfont-weight:bold;
    font-size:24px;
\tdisplay:inline;
}
div.w-report span.date {
\tmargin:3px 0px 3px 12px;
\tfont-weight:bold;
\tfont-size:16px;
}
div.weather-report {
\tbackground-image:url(static/img/w-bg.png);
\tbackground-repeat:no-repeat;
\tbackground-position:56px 70px;
\tmargin:0px;
\tpadding:0px;
\twidth:300px;
\theight:160px;
}
div.weather-icon {
\tbackground-image:url(static/w/img/d44.png);
\tbackground-repeat:no-repeat;
\tmargin:0px;
\tpadding:0px;
\twidth:300px;
\theight:160px;
}
div.weather-text {
\ttext-align:right;
\tmargin:0px;
\tpadding-top:76px;
\tpadding-right:20px;
}
div.weather-text p {
\tmargin:0px;
\tcolor:#FFF;
\tfont-size: 20px;
\tfont-weight: bold;
\ttext-shadow: #315895 0px -1px 1px;
\tline-height:28px;
}
</style>
<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push([\'_setAccount\', \'UA-251595-22\']);
  _gaq.push([\'_trackPageview\']);

  (function() {
    var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;
    ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';
    var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
</head>
<body style="font-size:13px">
  <div class="container" style="background-color:#FFF">
    <div class="span-24 last">
    </div>
    <div class="span-24 last">
      <div id="x-today-icon-small" style="background-repeat:no-repeat; height:34; padding:10px 0px 10px 60px; background-image:url(static/w/img/s44.png)"><strong>''')
        _v = VFSL([locals()]+SL+[globals(), __builtin__],"city.name",True) # u'${city.name}' on line 125, col 163
        if _v is not None: write(_filter(_v, rawExpr=u'${city.name}')) # from line 125, col 163.
        write(u'''</strong>
        <select name="change_city" id="change_city" onchange="change_city(this.value)">
          <option value="-">\u66f4\u6539\u57ce\u5e02</option>
''')
        for c in VFSL([locals()]+SL+[globals(), __builtin__],"cities",True): # generated from line 128, col 1
            write(u'''          <option value="''')
            _v = VFN(VFSL([locals()]+SL+[globals(), __builtin__],"c",True),"first_alias",False)() # u'${c.first_alias()}' on line 129, col 26
            if _v is not None: write(_filter(_v, rawExpr=u'${c.first_alias()}')) # from line 129, col 26.
            write(u'''">''')
            _v = VFSL([locals()]+SL+[globals(), __builtin__],"c.name",True) # u'${c.name}' on line 129, col 46
            if _v is not None: write(_filter(_v, rawExpr=u'${c.name}')) # from line 129, col 46.
            write(u'''</option>
''')
        write(u'''        </select>
      </div>
    </div>
\t<div class="span-16">
      <div class="span-16 last">
        <div id="weather-today" class="w-report span-8">
          <div><span class="h">\u4eca\u65e5\u5929\u6c14</span><span class="date"><span id="x-today-date"></span> <span id="x-today-day"></span></span></div>
          <div class="weather-report">
            <div id="x-today-icon" class="weather-icon">
              <div class="weather-text">
                <p id="x-today-text">Loading...</p>
                <p id="x-today-temp"></p>
              </div>
            </div>
          </div>
          <div><span class="h">\u5176\u4ed6\u4fe1\u606f\uff1a</span></div>
            <div style="padding:6px">
            <div>\u98ce\u529b\uff1a<span id="x-wind-chill">N/A</span> \u98ce\u5411\uff1a<span id="x-wind-direction">N/A</span> \u98ce\u901f\uff1a<span id="x-wind-speed">N/A</span></div>
            <div>\u80fd\u89c1\u5ea6\uff1a<span id="x-atmosphere-visibility">N/A</span> \u6e7f\u5ea6\uff1a<span id="x-atmosphere-humidity">N/A</span> \u6c14\u538b\uff1a<span id="x-atmosphere-pressure">N/A</span></div>
            <div>\u65e5\u51fa\uff1a<span id="x-astronomy-sunrise">N/A</span> \u65e5\u843d\uff1a<span id="x-astronomy-sunset">N/A</span></div>
            <div>\u53d1\u5e03\u4e8e\uff1a<span id="x-pub">N/A</span></div>
          </div>
        </div>
        <div id="weather-tomorrow" class="w-report span-8 last">
          <div><span class="h">\u660e\u65e5\u5929\u6c14</span><span class="date"><span id="x-tomorrow-date"></span> <span id="x-tomorrow-day"></span></span></div>
          <div class="weather-report">
            <div id="x-tomorrow-icon" class="weather-icon">
              <div class="weather-text">
                <p id="x-tomorrow-text">Loading...</p>
                <p id="x-tomorrow-temp"></p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="w-report span-16 last" style="margin-top:6px">
        <div><span class="h">\u5b89\u88c5Chrome\u63d2\u4ef6</span></div>
        <div style="padding:6px">
          <div>\u5982\u679c\u60a8\u4f7f\u7528\u7684\u662f\u652f\u6301HTML 5\u7684Google Chrome\u6d4f\u89c8\u5668\uff0c\u53ef\u4ee5<a href="https://chrome.google.com/extensions/detail/gbmkicglakjoppnghhiceacmbbaihoeh" target="_blank">\u5b89\u88c5\u6700\u65b0\u63d2\u4ef6</a>\u4ee5\u4fbf\u968f\u65f6\u83b7\u53d6\u5929\u6c14\u9884\u62a5\uff1a</div>
          <div><a href="https://chrome.google.com/extensions/detail/gbmkicglakjoppnghhiceacmbbaihoeh" target="_blank"><img src="static/img/snapshot-chrome-extension.png" width="291" height="99" style="margin:12px"/></a></div>
        </div>
      </div>
      <div class="w-report span-16 last" style="margin-top:6px">
        <div><span class="h">GTalk\u673a\u5668\u4eba</span></div>
        <div style="padding:6px">
          <div>\u5982\u679c\u60a8\u4f7f\u7528Google Talk\uff0c\u53ef\u4ee5\u6dfb\u52a0\u673a\u5668\u4eba<strong>weather-china@appspot.com</strong>\u4e3a\u597d\u53cb\uff0c\u968f\u65f6\u5411\u4ed6\u8be2\u95ee\u5929\u6c14\u9884\u62a5\uff1a</div>
          <div><img src="static/img/snapshot-xmpp.png" width="300" height="254" style="margin:12px"/></div>
        </div>
      </div>
    </div>
    <div class="span-8 last">
<script type="text/javascript"><!--
google_ad_client = "pub-6727358730461554";
/* 300x250 */
google_ad_slot = "8201905603";
google_ad_width = 300;
google_ad_height = 250;
//-->
</script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
<script type="text/javascript"><!--
google_ad_client = "pub-6727358730461554";
/* 300x250 */
google_ad_slot = "8201905603";
google_ad_width = 300;
google_ad_height = 250;
//-->
</script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
<script type="text/javascript"><!--
google_ad_client = "pub-6727358730461554";
/* 300x250 */
google_ad_slot = "8201905603";
google_ad_width = 300;
google_ad_height = 250;
//-->
</script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
    </div>
      <div class="span-24 last"></div>
      <div class="span-24 last"><div style="text-align:center;padding:6px"><a href="http://code.google.com/p/weather-china/wiki/API" target="_blank">API\u670d\u52a1</a> | <a href="http://code.google.com/p/weather-china/issues/list" target="_blank">\u610f\u89c1\u53cd\u9988</a> | <a id="x-contact" href="#">\u8054\u7cfb\u6211\u4eec</a> | Copyright&copy;2010</div></div>
  </div>
<script type="text/javascript">
    jQuery("#x-contact").attr("href", "mail" + "to:ask" + "xuefeng@" + "gm" + "ail.com");
</script>
</body>
</html>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_CompiledTemplate= 'respond'

## END CLASS DEFINITION

if not hasattr(CompiledTemplate, '_initCheetahAttributes'):
    templateAPIClass = getattr(CompiledTemplate, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(CompiledTemplate)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=CompiledTemplate()).run()


