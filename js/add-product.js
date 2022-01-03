// show price box when bay is checked //
const typeBay = document.querySelector(".action-type .type .input.bay input");
const typeExchange = document.querySelector(
    ".action-type .type .input.exchange input"
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

// product quality //
const qualityStars = document.querySelectorAll(
    "li.quality .input .stars .star"
);
const qualityValue = document.querySelector(
    "li.quality .input input.quality-value"
);

qualityStars.forEach((obj, index) => {
    obj.addEventListener("click", () => {
        // turn off all stars //
        qualityStars.forEach((star) => {
            star.classList.remove("active");
        });
        //  //

        // turn on //
        for (let i = 0; i <= index; i++) {
            qualityStars[i].classList.add("active");
        }
        //  //

        // set the input value //
        qualityValue.setAttribute("value", index + 1);
        //  //
    });
});
//  //

// main picture //
const main_img_set = document.querySelector(".main-picture .img input.isSet");
const main_img_delete_btn = document.querySelector(
    ".main-picture .img .delete"
);

const main_img_input = document.querySelector(".main-picture .img input.file");
const mainImg = document.querySelector(".main-picture .img img");

main_img_input.addEventListener("change", () => {
    // img steed //
    main_img_set.setAttribute("value", "true");
    //  //

    // enable the delete button //
    main_img_delete_btn.classList.add("set");
    //  //

    // load the img //
    const reader = new FileReader();

    reader.addEventListener("load", () => {
        mainImg.setAttribute("src", reader.result);
    });

    reader.readAsDataURL(main_img_input.files[0]);
    //  //
});

main_img_delete_btn.addEventListener("click", () => {
    // set the default img //
    mainImg.setAttribute("src", "../img/icon/image.png");
    //  //

    // unset the input //
    main_img_set.setAttribute("value", "false");
    //  //

    // disable the delete button //
    main_img_delete_btn.classList.remove("set");
    //  //
});
//  //

// other pictures //
let pictures;

const picturesCounter = document.querySelector(
    ".other-pictures-input input.counter"
);
let picturesInputs = document.querySelectorAll(
    ".other-pictures-input input.file"
);
let lastPicturesInput = document.querySelector(
    ".other-pictures-input input.file:last-child"
);

const picturesInputsContainer = document.querySelector(".other-pictures-input");
const picturesContainer = document.querySelector(".other-pictures .container");

let picturesImg;
let picturesDeleteBtn;

let picturesNum = 0;

function addPic() {
    let addBtn = document.querySelector(".other-pictures .container .add");

    picturesContainer.removeChild(addBtn);

    const reader = new FileReader();

    reader.addEventListener("load", () => {
        picturesNum++;
        picturesCounter.setAttribute("value", picturesNum);

        // add new input //
        picturesInputsContainer.innerHTML += `<input class="file" type="file" id="img${
            picturesNum + 1
        }" />`;
        //  //

        // add the pic //
        picturesContainer.innerHTML += `<div class="pic">
            <img src="${reader.result}" alt="" />

            <label class="change" for="img${picturesNum}">Change</label>
            <div class="delete">
                <img src="../img/icon/delete.png" alt="" />
            </div>
        </div>`;
        //  //

        // add the add button //
        picturesContainer.innerHTML += `<label class="add" for="img${
            picturesNum + 1
        }"><img src="../img/icon/add.png" alt="" /></label>`;
        //  //

        // reset the pictures inputs //
        picturesInputs = document.querySelectorAll(
            ".other-pictures-input input.file"
        );

        picturesInputs.forEach((obj, index) => {
            obj.setAttribute("onchange", `changePictureImg(${index})`);
        });
        //  //

        // reset the last input //
        lastPicturesInput = document.querySelector(
            ".other-pictures-input input.file:last-child"
        );

        lastPicturesInput.setAttribute("onchange", "addPic()");
        //  //

        // reset the pictures //
        pictures = document.querySelectorAll(".other-pictures .container .pic");
        //  //

        // reset the images //
        picturesImg = document.querySelectorAll(
            ".other-pictures .container .pic > img"
        );
        //  //

        // reset the delete buttons //
        picturesDeleteBtn = document.querySelectorAll(
            ".other-pictures .container .pic > .delete"
        );

        picturesDeleteBtn.forEach((obj, index) => {
            obj.setAttribute("onclick", `deleteImg(${index})`);
        });
        //  //
    });

    reader.readAsDataURL(lastPicturesInput.files[0]);
}
lastPicturesInput.setAttribute("onchange", "addPic()");

function changePictureImg(index) {
    if (index < picturesInputs.length - 1) {
        const reader = new FileReader();

        reader.addEventListener("load", () => {
            picturesImg[index].setAttribute("src", reader.result);
        });

        reader.readAsDataURL(picturesInputs[index].files[0]);
    }
}

let deleteButtonEvent = [];

function deleteImg(i) {
    picturesNum--;
    picturesCounter.setAttribute("value", picturesNum);

    picturesContainer.removeChild(pictures[i]); // remove the picture //
    picturesInputsContainer.removeChild(picturesInputs[i]); // remove the picture input //

    // rest the pictures inputs //
    picturesInputs = document.querySelectorAll(
        ".other-pictures-input input.file"
    );

    picturesInputs.forEach((obj, index) => {
        obj.setAttribute("id", `img${index + 1}`);
        obj.setAttribute("onchange", `changePictureImg(${index})`);
    });
    //  //

    // reset the last input //
    lastPicturesInput = document.querySelector(
        ".other-pictures-input input.file:last-child"
    );

    lastPicturesInput.setAttribute("onchange", "addPic()");
    //  //

    // rest the pictures inputs label //
    document.querySelectorAll(".pic label.change").forEach((obj, index) => {
        obj.setAttribute("id", `img${index + 1}`);
    });
    //  //

    // rest the change buttons //
    document
        .querySelectorAll(".other-pictures .container .pic .change")
        .forEach((obj, index) => {
            obj.setAttribute("for", `img${index + 1}`);
        });
    //  //

    // reset the pictures //
    pictures = document.querySelectorAll(".other-pictures .container .pic");
    //  //

    // reset the images //
    picturesImg = document.querySelectorAll(
        ".other-pictures .container .pic > img"
    );
    //  //

    // reset the delete buttons //
    picturesDeleteBtn = document.querySelectorAll(
        ".other-pictures .container .pic > .delete"
    );

    picturesDeleteBtn.forEach((obj, index) => {
        obj.setAttribute("onclick", `deleteImg(${index})`);
    });
    //  //

    // reset the add button //
    document
        .querySelector(".other-pictures .container .add")
        .setAttribute("for", `img${picturesNum + 1}`);
    //  //
}
//  //
