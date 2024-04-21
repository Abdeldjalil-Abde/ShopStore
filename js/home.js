// sticky par style //
const sectionsLinksContainer = document.querySelector("main .titles-par");
const sectionsLinks = document.querySelectorAll(".titles-par .title span");
const sections = document.querySelectorAll("main .container section");

window.scrollTo(0, 0); // reset the scroll //

let sectionsBounds = [];
let topSpace = 200;
function sectionsEffect() {
    document.querySelector("html").style.scrollBehavior = "smooth"; // make the scroll smooth //
}

setTimeout(() => {
    sectionsEffect();
}, 1000);
//  //
