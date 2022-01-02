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

// product type window //
const productTypeWindow = document.querySelector(".product-type-window");

const productTypes = document.querySelectorAll(
    ".product-type-window .product-type .type"
);
const productTypesContent = document.querySelectorAll(
    ".product-type-window .product-type .type .content"
);
let productTypeSelected = "clothes";

let filterTypes;
let filterTypesContent;

const filterTypesContainer = document.querySelector(
    ".product-type-window .filter-type"
);

const productTypeField = document.querySelector("li.product-type .input .type");
const productTypeInput = document.querySelector(
    "li.product-type .input input.product-type-input"
);
const filterTypeInput = document.querySelector(
    "li.product-type .input input.filter-type-input"
);

const productTypeOpenBtn = document.querySelector(
    "li.product-type .input .change"
);
const productTypeCloseBtn = document.querySelector(
    ".product-type-window .close"
);

let productTypesItems = {
    clothes: [
        { name: "shirts", logo: "../img/icon/clothe/shirt.png" },
        { name: "pants", logo: "../img/icon/clothe/pant.png" },
        { name: "shoes", logo: "../img/icon/clothe/shoes.png" },
        { name: "coats", logo: "../img/icon/clothe/coat.png" },
        { name: "hats", logo: "../img/icon/clothe/hat.png" },
        { name: "dresses", logo: "../img/icon/clothe/dress.png" },
        { name: "skirts", logo: "../img/icon/clothe/skirt.png" },
    ],
    tools: [
        { name: "hammer", logo: "../img/icon/tool/hammer.png" },
        { name: "painting", logo: "../img/icon/tool/painting.png" },
        { name: "saw", logo: "../img/icon/tool/saw.png" },
        { name: "screw driver", logo: "../img/icon/tool/screw-driver.png" },
        { name: "shovel", logo: "../img/icon/tool/shovel.png" },
        { name: "wrench", logo: "../img/icon/tool/wrench.png" },
    ],
    vehicles: [
        { name: "car", logo: "../img/icon/vehicle/car.png" },
        { name: "motorcycle", logo: "../img/icon/vehicle/motorcycle.png" },
        { name: "bike", logo: "../img/icon/vehicle/bike.png" },
    ],
    "car parts": [
        {
            name: "car engine",
            logo: "../img/icon/car parts/car-engine.png",
        },
        { name: "car wheel", logo: "../img/icon/car parts/car-wheel.png" },
        {
            name: "car battery",
            logo: "../img/icon/car parts/car-battery.png",
        },
        { name: "car chair", logo: "../img/icon/car parts/car-chair.png" },
        {
            name: "steering wheel",
            logo: "../img/icon/car parts/steering-wheel.png",
        },
        {
            name: "spare parts",
            logo: "../img/icon/car parts/spare-parts.png",
        },
        {
            name: "car electrics",
            logo: "../img/icon/car parts/car-electrics.png",
        },
        {
            name: "car structure",
            logo: "../img/icon/car parts/car-structure.png",
        },
    ],
    electrics: [
        { name: "tv", logo: "../img/icon/electric/tv.png" },
        {
            name: "air-conditioner",
            logo: "../img/icon/electric/air-conditioner.png",
        },
        { name: "fridge", logo: "../img/icon/electric/fridge.png" },
        { name: "freezer", logo: "../img/icon/electric/freezer.png" },
        { name: "heater", logo: "../img/icon/electric/heater.png" },
        { name: "light", logo: "../img/icon/electric/light.png" },
        { name: "oven", logo: "../img/icon/electric/oven.png" },
        { name: "stove", logo: "../img/icon/electric/stove.png" },
    ],
    furniture: [
        { name: "bed", logo: "../img/icon/furniture/bed.png" },
        { name: "chair", logo: "../img/icon/furniture/chair.png" },
        { name: "closet", logo: "../img/icon/furniture/closet.png" },
        { name: "mattress", logo: "../img/icon/furniture/mattress.png" },
        { name: "pillow", logo: "../img/icon/furniture/pillow.png" },
        { name: "sofa", logo: "../img/icon/furniture/sofa.png" },
        { name: "table", logo: "../img/icon/furniture/table.png" },
    ],
    building: [
        { name: "cement", logo: "../img/icon/building/cement.png" },
        { name: "paint", logo: "../img/icon/building/paint.png" },
        { name: "electrical", logo: "../img/icon/building/electrical.png" },
    ],
    books: [
        { name: "student", logo: "../img/icon/book/student-book.png" },
        { name: "language", logo: "../img/icon/book/language-book.png" },
        { name: "novel", logo: "../img/icon/book/novel.png" },
        { name: "children", logo: "../img/icon/book/children-book.png" },
        { name: "religious", logo: "../img/icon/book/religious-book.png" },
    ],
    phones: [
        { name: "smart phone", logo: "../img/icon/phone/smart-phone.png" },
        { name: "old phone", logo: "../img/icon/phone/old-phone.png" },
        { name: "fixed phone", logo: "../img/icon/phone/fixed-phone.png" },
    ],
};

function setFilterTypes(obj) {
    let content = "";

    productTypesItems[obj].forEach((type) => {
        content += `<button class="type"><img src="${type["logo"]}" alt="" class="logo" /><span class="content">${type["name"]}</span></button>`;
    });
    content += `<button class="type active"><img src="../img/icon/other.png" alt="" class="logo" /><span class="content">other</span></button>`;

    filterTypesContainer.innerHTML = content;
}

function activeType(list, index) {
    list.forEach((obj) => {
        obj.classList.remove("active");
    });

    list[index].classList.add("active");
}

function setProductTypeInput(action, type) {
    if (action == "product type") {
        productTypeField.innerHTML = `<img src="../img/icon/product type/${type}.png" alt="" /><span>${type}</span>`;

        productTypeInput.setAttribute("value", type);
        filterTypeInput.setAttribute("value", "other");
    } else if (action == "filter type") {
        if (type == "other") {
            productTypeField.innerHTML = `<img src="../img/icon/product type/${productTypeSelected}.png" alt="" /><span>${productTypeSelected}</span>`;
        } else {
            let logo = "";

            productTypesItems[productTypeSelected].forEach((obj) => {
                if (obj["name"] == type) {
                    logo = obj["logo"];
                }
            });

            productTypeField.innerHTML = `<img src="${logo}" alt="" /><span>${type}</span>`;
        }

        filterTypeInput.setAttribute("value", type);
    }
}

function setFilterTypesEvent(list) {
    list.forEach((obj, index) => {
        obj.addEventListener("click", () => {
            activeType(list, index);

            // set inputs value //
            // productTypeField.innerHTML = `<img src="../img/icon/${productTypeSelected}/${filterTypesContent[index].innerHTML}.png" alt="" /><span>${filterTypesContent[index].innerHTML}</span>`;

            // filterTypeInput.setAttribute(
            //     "value",
            //     productTypesContent[index].innerHTML
            // );

            setProductTypeInput(
                (action = "filter type"),
                filterTypesContent[index].innerHTML
            );
            //  //
        });
    });
}

productTypes.forEach((obj, index) => {
    obj.addEventListener("click", () => {
        // active product type //
        productTypeSelected = productTypesContent[index].innerHTML;

        setFilterTypes(productTypeSelected);
        activeType(productTypes, index);
        //  //

        // reset the filter types var //
        filterTypes = document.querySelectorAll(
            ".product-type-window .filter-type .type"
        );
        filterTypesContent = document.querySelectorAll(
            ".product-type-window .filter-type .type .content"
        );

        setFilterTypesEvent(filterTypes);
        //  //

        setProductTypeInput(
            (action = "product type"),
            productTypesContent[index].innerHTML
        );
    });
});

// default //
setFilterTypes("clothes");

filterTypes = document.querySelectorAll(
    ".product-type-window .filter-type .type"
);
filterTypesContent = document.querySelectorAll(
    ".product-type-window .filter-type .type .content"
);

setFilterTypesEvent(filterTypes);
//  //

// open and close the product type window //
productTypeOpenBtn.addEventListener("click", () => {
    productTypeWindow.classList.add("active");
});
productTypeCloseBtn.addEventListener("click", () => {
    productTypeWindow.classList.remove("active");
});
//  //

//  //
