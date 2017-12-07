<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Misaka live wallpaper project</title>
</head>
<link rel="stylesheet" type="text/css" href="style.css?no_cache=<?php echo rand()?>">
<body>
<!--
    <div id="mouse-indicator">
        <div id="mouse-indicator-int">

        </div>
        recognized
    </div>
-->
    <div id="left-top-hud-1" class="hud border-me">
        <span class="hud small-indicator">
            link up
        </span>
        <span class="hud small-indicator">
            44xx, 10.0Gbps, full-duplex
        </span>
        <br/>
        <!--
        <span class="hud">
            <span class="hud small-indicator">当前任务目标：</span>回收
        </span>
        <br/>
        <span class="hud small-indicator">
            - 回收Misaka_0x272E
            <br/>
            - 上传黑盒数据
        </span>
        -->
    </div>
    <div id="left-bottom-hud-1" class="hud">
        <div id="console" class="hud-title">
            CONSOLE
        </div>
        <div id="console-content" class="border-me small-indicator">
            ---HUD START---
        </div>
        <div id="left-bottom-hud-1-pass" style="background: transparent;">
            <span class="hud-title" style="border: 0;"> </span>
        </div>
        <div id="left-bottom-hud-1-active-monitor" class="border-me small-indicator">
            最后活动
            <span id="left-bottom-hud-1-active-monitor-timer">
                  0秒前
            </span>
        </div>
        <div id="left-bottom-hud-1-pass" style="background: transparent;">
            <span class="hud-title" style="border: 0;"> </span>
        </div>
        <div id="left-bottom-hud-1-env">
            <span class="hud-title system-yellow">ENV</span>
            传感器脱机
        </div>
        <div id="left-bottom-hud-1-iff">
            <span id="left-bottom-hud-1-iff-title" class="hud-title">IFF</span>
            <span id="left-bottom-hud-1-iff-content">联机</span>
        </div>
        <div id="left-bottom-hud-1-fcs">
            <span class="hud-title">FCS</span>
            联机
        </div>
        <div id="left-bottom-hud-1-dur">
            <span class="hud-title" id="left-bottom-hud-1-dur-title">CAP</span>
            <span id="hud-progressbar" class="hud-progressbar">状态存疑/不确定 - 等待后续判断</span>
        </div>
    </div>
</body>
</html>
<script src="script.js?no_cache=<?php echo rand()?>"></script>