let check1 = document.getElementById("check1");
let check2 = document.getElementById("check2");
let check3 = document.getElementById("check3");

function color_change1(){
    if (check1.style.color == "rgb(255, 255, 255)"){
        check1.style.color = "rgba(167, 139, 250, 1)"
        return true;
    }
    else{
        check1.style.color = "fff"
        return false;
    }
} 
function color_change2(){
    if (check2.style.color == "rgb(255, 255, 255)"){
        check2.style.color = "rgba(167, 139, 250, 1)"
        return true;
    }
    else{
        check2.style.color = "fff"
        return false;
    }}
function color_change3() {
    if (check3.style.color == "rgb(255, 255, 255)"){
        check3.style.color = "rgba(167, 139, 250, 1)"
        return true;
    }
    else{
        check3.style.color = "fff"
        return false;
}}

function start(){
    location.href('http://172.18.212.211:8000/test3.py')
}
