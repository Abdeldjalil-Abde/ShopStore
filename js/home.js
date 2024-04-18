// sticky par style //
const sectionsLinksContainer = document.querySelector("main .titles-par");
const sectionsLinks = document.querySelectorAll(".titles-par .title span");
const sections = document.querySelectorAll("main .container section");

window.scrollTo(0, 0); // reset the scroll //

let sectionsBounds = [];
let topSpace = 200;
function sectionsEffect() {
    document.querySelector("html").style.scrollBehavior = "smooth"; // make the scroll smooth //

    // get sections bounds //
    sections.forEach((obj) => {
        sectionsBounds.push(obj.getBoundingClientRect());
    });
    //  //

    // sections links activation style //
    window.addEventListener("scroll", () => {
        sectionsBounds.forEach((bound, index) => {
            if (
                window.scrollY + topSpace >= bound.top &&
                window.scrollY + topSpace <= bound.top + bound.height
            ) {
                sectionsLinks[index].classList.add("active");
            } else {
                sectionsLinks[index].classList.remove("active");
            }
        });
    });
    //  //

    // sections links click effect //
    sectionsLinks.forEach((obj, index) => {
        obj.addEventListener("click", () => {
            window.scrollTo(0, sectionsBounds[index].top - topSpace + 20); // scroll to section //
        });
    });
    //  //
}

setTimeout(() => {
    sectionsEffect();
}, 1000);
//  //
