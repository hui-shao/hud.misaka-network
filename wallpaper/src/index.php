<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Misaka live wallpaper project</title>
</head>
<link rel="stylesheet" type="text/css" href="style.css?no_cache=<?php echo rand()?>">
<body>
    <div id="left-top-hud-1" class="hud">
        <div class="hud-monospace large-indicator system-green">
            connected
        </div>
        <div class="hud-monospace">
            misaka44xx 7:f.0 wlan0
            <br/>
            link up, 10.0Gbps, full-duplex
        </div>
    </div>
    <div id="left-bottom-hud-1" class="hud">
        <div id="left-bottom-hud-1-env">
            <span class="hud-monospace hud-title">ENV</span>
            <span class="hud-monospace">
                55F 42% +03atm
            </span>
        </div>
        <div id="left-bottom-hud-1-iff">
            <span class="hud-monospace hud-title system-red">IFF</span>
            <span class="hud-monospace">
                脱机 - 3小时前
            </span>
        </div>
        <div id="left-bottom-hud-1-fcs">
            <span class="hud-monospace hud-title">FCS</span>
            <span class="hud-monospace">
                状态存疑/不稳定 - 等待后续判断
            </span>
        </div>
        <div id="left-bottom-hud-1-dur">
            <span class="hud-monospace hud-title system-yellow">DUR</span>
            <span>
                IIIIIIIIII III<span style="opacity: 0.2">IIIIIII IIIIIIIIII IIIIIIIII</span>I
            </span>
        </div>
    </div>
</body>
</html>
<script src="script.js">