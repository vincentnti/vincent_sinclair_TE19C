var i = 0;
var f = 0;
var g = 0;
var txt = "Hej!"
var txt2 = "Jag är Vincent Sinclair";
var txt3 = "En elev som går på NTI Kronhus gymnasiet."
var speed = 100;

function typeWriter(){
    if(i < txt.length) {
        document.getElementById("writer").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
    if(f < txt2.length) {
        document.getElementById("writer2").innerHTML += txt2.charAt(f);
        f++;
        setTimeout(typeWriter, speed);
    }
    if (g < txt3.length) {
        document.getElementById("writer3").innerHTML += txt3.charAt(g);
        g++;
        setTimeout(typeWriter, speed);
    }
}

window.onload = typeWriter();