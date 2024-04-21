const btnSign_up = document.querySelector("header > .account #sign_up");
const btnLogin = document.querySelector("header > .account #login");
const form = document.querySelector(".login-wrap");
const btnDelete = document.querySelector(".login-wrap > .delete");
const sign_in = document.querySelector(".login-wrap > .sign-in");
const sign_up = document.querySelector(".login-wrap > .sign-up");


// show form sign up 
if (btnSign_up) {
    btnSign_up.addEventListener("click", function () {
        form.style.display = "block";
        sign_up.checked = true;
        sign_in.checked = false;
    });
}
// show form sign in
if (btnLogin) {
    btnLogin.addEventListener("click", function () {
        form.style.display = "block";
        sign_in.checked = true;
        sign_up.checked = false;
    });
}

// hide content form sign up and sign in 
if (btnDelete) {
    btnDelete.addEventListener("click", function () {
        form.style.display = "none";

    });
}

// alert 
var urlParams = new URLSearchParams(window.location.search);

var value = urlParams.get('value');
var Active = urlParams.get('active');

if (value == "true") {
    alert("تمت عملية التسجيل بنجاح !");
} else if (value == "false") {
    alert("إسم المستخدم او كلمة المرور التي ادخلتها غير صحيح يرجى إعادة المحاولة من جديد !!  ");
}  else if (value == "user_exist") {
    alert("إسم المستخدم الذي ادخلته موجود من قبل يرجى إعادة المحاولة من جديد !! ");
} else if(value =="true_message"){
    alert("تم التعليق بنجاح نشكرك على مشاركة رأيك حول الموقع ");
}
if (Active == "not") {
    alert("حسابك مقيد يرجى الإتصال بمسؤول الدعم او التقرب الى المؤسسة لإستعادة حسابك!! ");
}
