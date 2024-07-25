
"use strict";

const loginId = document.getElementById('LOGIN_ID');
const loginPw = document.getElementById('LOGIN_PW');
const loginBtn = document.getElementById('LOGIN_BTN');

function color() {
    if((loginId.value.length>0 && loginId.value.indexOf("@")!==-1) 
        && loginPw.value.length>=5){
        loginBtn.style.backgroundColor = "rgba(167, 139, 250, 1)";
        loginBtn.disabled = false;
    }else{
        loginBtn.style.backgroundColor = "rgb(212, 200, 250)";
        loginBtn.disabled = true;
    }
}

function moveToMain(){
    location.replace("main_page_login.html");
}

loginId.addEventListener('keyup', color);
loginPw.addEventListener('keyup', color);
loginBtn.addEventListener('click',moveToMain);