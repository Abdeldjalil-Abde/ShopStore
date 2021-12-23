// show price box when bay is checked //
const typeBay = document.querySelector(
    ".action-type .type .input:nth-child(1) input"
);
const typeExchange = document.querySelector(
    ".action-type .type .input:nth-child(2) input"
);

const priceBox = document.querySelector(".action-type .price");

typeBay.addEventListener("click", (e) => {
    priceBox.classList.remove("hide");
});
typeExchange.addEventListener("click", (e) => {
    priceBox.classList.add("hide");
});

//  //
