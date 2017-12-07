var lastX = 0;
var lastY = 0;
var stabledX = 0;
var stabledY = 0;
var gui_duration = 3600;
const dur_capacity = 3600;
var idle_confirm = 0;
var idle_time = 0;
const idle_time_max = 300;
const recharge_speed = 60; //multiplier - 60 is recharge in 1hr / speed_factor
const speed_factor = 1; //1 is stand for 30min-1hr, 4 is 7.5min-15min. debug only.
const bar_length = 6;
document.onmousemove = document.onmousewheel = document.onmousedown = function(event) {
    /*
    The following code has been disabled due to:
    There are no need to support old IE.
    ---------------------------------------------------

    var dot, eventDoc, doc, body, pageX, pageY;

    event = event || window.event; // IE-ism

    // If pageX/Y aren't available and clientX/Y are,
    // calculate pageX/Y - logic taken from jQuery.
    // (This is to support old IE)
    if (event.pageX == null && event.clientX != null) {
        eventDoc = (event.target && event.target.ownerDocument) || document;
        doc = eventDoc.documentElement;
        body = eventDoc.body;

        event.pageX = event.clientX +
            (doc && doc.scrollLeft || body && body.scrollLeft || 0) -
            (doc && doc.clientLeft || body && body.clientLeft || 0);
        event.pageY = event.clientY +
            (doc && doc.scrollTop  || body && body.scrollTop  || 0) -
            (doc && doc.clientTop  || body && body.clientTop  || 0 );
    }
    */

    // Use event.pageX / event.pageY here

    idle_confirm++;

    if(Math.abs(lastY - event.pageY) > 10 || Math.abs(lastX - event.pageX) > 10){
        idle_confirm = 2147483647;
    }

    lastX = event.pageX;
    lastY = event.pageY;

    screen_console_log("" + lastX + ", " + lastY + "");
};
window.onload = function () {
    setInterval(updateMe, 33);
    setInterval(rest_timer, 100);
    setInterval(idle_count_func, 333);
};
function updateMe(){
    function make_range(value, range, percent){
        return value - range / 2 + range * percent / 100;
    }
    stabledX += (lastX - stabledX) / 5;
    stabledY += (lastY - stabledY) / 5;
//    document.getElementById("mouse-indicator").style.top = stabledY + "px";
//    document.getElementById("mouse-indicator").style.left = stabledX + 20 + "px";
    document.getElementById("left-bottom-hud-1").style.bottom = make_range(5, 1.3, stabledY/10.8) + "rem";
    document.getElementById("left-bottom-hud-1").style.left = make_range(5, 1, -stabledX/19.2) + "rem";
//    document.getElementById("left-bottom-hud-1").style.transform =
//        "rotate3d(" + make_range(0.15, 0.15, event.pageY/10.8) + ", 0, -0.015, 15deg)";
    document.getElementById("left-top-hud-1").style.top = make_range(8, 1.3, -stabledY/10.8) + "rem";
    document.getElementById("left-top-hud-1").style.left = make_range(5, 1, -stabledX/19.2) + "rem";
    document.getElementById("left-bottom-hud-1-active-monitor-timer").innerHTML = friendly_time_duration(idle_time);
}
function rest_timer() {
    idle_time += 0.1 * speed_factor;
    if(idle_time > idle_time_max){
        gui_duration += 0.1 * recharge_speed * speed_factor;
        if(gui_duration > dur_capacity){
            gui_duration = dur_capacity
        }
    }else{
        gui_duration -= (Math.random() / 10 + 0.1) * speed_factor;
    }
    var bar_factor = gui_duration / dur_capacity;
    var target_html_pre = "I".repeat(Math.floor(bar_factor * bar_length * 10)) + "<span style=\"opacity: 0.2\">" +
                    "I".repeat(Math.floor(bar_length * 10 - bar_factor * bar_length * 10)) + "</span>";
    var i_count = 0;
    var target_html = "";
    for(var i=0; i<target_html_pre.length; i++){
        if(target_html_pre[i] === "I"){
            i_count++;
        }
        if(i_count % 10 !== 0 || target_html_pre[i] !== "I"){
            target_html += target_html_pre[i];
        }else{
            target_html += " ";
        }
    }
    document.getElementById("hud-progressbar").innerHTML = target_html;
}
function idle_count_func() {
    if(idle_confirm > 3){
        idle_time = 0;
    }
    idle_confirm = 0;
}
function friendly_time_duration(seconds){
    if(seconds < 60){
        return Math.floor(seconds) + "秒前";
    }else if(seconds < 3600){
        return Math.floor(seconds / 60) + "分钟前";
    }else{
        return Math.floor(seconds / 3600) + "小时前";
    }
}
function screen_console_log(log_content){
    console.log(log_content);
    var prev_content = document.getElementById("console-content").innerHTML.split("<br>");
    prev_content = prev_content.clean("");
    prev_content.push(log_content);
    var back_content = "";
    for(var i = prev_content.length - 5; i < prev_content.length; i++) {
        if(i >= 0){
            back_content += prev_content[i] + "<br/>";
//            if(i <= prev_content.length){
//                back_content += "<br>";
//            }
        }
    }
    document.getElementById("console-content").innerHTML = back_content;
}
Array.prototype.clean = function(deleteValue) {
    for (var i = 0; i < this.length; i++) {
        if (this[i] === deleteValue) {
            this.splice(i, 1);//返回指定的元素
            i--;
        }
    }
    return this;
};