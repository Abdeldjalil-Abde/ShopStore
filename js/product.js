// images style //
const imagesContainer = document.querySelector(".images-container");
const imagesBar = document.querySelector(".images-container .images-bar");

// set the images //
let productType = urlPar["product_type"];
let filterType = urlPar["filter_type"];

imagesBar.innerHTML = "";
for (let i = 1; i <= 3; i++) {
    imagesBar.innerHTML += `<div class="img">
                                <img src="../img/products/${productType}/${filterType}/${filterType} (${i}).jpg" alt="" />
                            </div>`;
}
//  //

const images = document.querySelectorAll(".images-container .images-bar .img");

const leftBtn = document.querySelector(".images-container .left-btn");
const rightBtn = document.querySelector(".images-container .right-btn");

const imagesContainerStyle = window.getComputedStyle(imagesContainer);

let actionType = urlPar["action_type"];

let imagesContainerWidth = imagesContainerStyle
    .getPropertyValue("width")
    .split("px")[0];

let pointer = 0;

images.forEach((img) => {
    img.style.width = imagesContainerWidth + "px";
});

leftBtn.addEventListener("click", (e) => {
    if (pointer > 0) {
        pointer--;
    } else {
        pointer = images.length - 1;
    }

    imagesBar.style.left = -pointer * imagesContainerWidth + "px";
});

rightBtn.addEventListener("click", (e) => {
    if (pointer < images.length - 1) {
        pointer++;
    } else {
        pointer = 0;
    }

    imagesBar.style.left = -pointer * imagesContainerWidth + "px";
});
//  //

// product action button //
const bayBtn = document.querySelector(".right .action .bay");
const exchangeBtn = document.querySelector(".right .action .exchange");

if (urlPar["product_action"] == "bay") {
    bayBtn.classList.add("show");
} else if (urlPar["product_action"] == "exchange") {
    exchangeBtn.classList.add("show");
}
//  //
