
// top par header shadow //
let header = document.querySelector(".top-par");

window.addEventListener("scroll", (e) => {
    if (window.scrollY > 50) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
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
        urlStr += "&product_type=none";
    }
    if (!urlStr.includes("filter_type")) {
        urlStr += "&filter_type=none";
    }

    urlStr = urlStr.split("?")[1].split("&");

    let urlPar = [];
    urlStr.forEach((obj) => {
        if (obj == "") return;

        let name = obj.split("=")[0];
        let value = obj.split("=")[1];
        value = value.replaceAll("%22", "");
        value = value.replaceAll("%27", "");
        value = value.replaceAll("%20", " ");

        urlPar.push({ name, value });
    });

    return urlPar;
}
//  //