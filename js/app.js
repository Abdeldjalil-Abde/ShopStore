// top par header shadow //
let header = document.querySelector(".top-par");
const goUpArrow = document.querySelector(".top-par .go-up");

window.addEventListener("scroll", (e) => {
    if (window.scrollY > 50) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }

    if (goUpArrow != undefined) {
        if (window.scrollY > 200) {
            goUpArrow.classList.add("show");
        } else {
            goUpArrow.classList.remove("show");
        }
    } 
});
//  //

// url function //
function getUrlParameters() {
    let urlStr = window.location.search;

    if (urlStr == "") {
        urlStr += "?";
    }

    if (!urlStr.includes("product_type")) {
        urlStr += "&product_type=clothes";
    }
    if (!urlStr.includes("filter_type")) {
        urlStr += "&filter_type=all";
    }
    if (!urlStr.includes("logged")) {
        urlStr += "&logged=false";
    }

    urlStr = urlStr.split("?")[1].split("&");

    let urlPar = {};
    urlStr.forEach((obj) => {
        if (obj == "") return;

        let name = obj.split("=")[0];
        let value = obj.split("=")[1];
        value = value.replaceAll("%22", "");
        value = value.replaceAll("%27", "");
        value = value.replaceAll("%20", " ");

        urlPar[name] = value;
    });

    return urlPar;
}
//  //

// set the logged style //
let urlPar = getUrlParameters();
const allLinks = document.querySelectorAll("a");

if (urlPar["logged"] == "true") {
    header.classList.add("logged");
}

// //
