var lastX = 0;
var lastY = 0;
var stabledX = 0;
var stabledY = 0;
document.onmousemove = function(event) {
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
    lastX = event.pageX;
    lastY = event.pageY;
};
window.onload = function () {
    setInterval(updateMe, 33);
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

}