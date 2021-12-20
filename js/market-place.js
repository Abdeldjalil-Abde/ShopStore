// opening the filter mene //
const filterMene = document.querySelector(".filter-mene");
const filterMeneBtn = document.querySelector(".filter-mene .open");

const filterPar = document.querySelector(".filter-par");
const toolsPar = document.querySelector(".tools-par");
const market = document.querySelector("section.market");

filterMene.addEventListener("click", (e) => {
    filterMene.classList.toggle("active");
    filterPar.classList.toggle("mene-opened");
    toolsPar.classList.toggle("mene-opened");
    market.classList.toggle("mene-opened");
});

//  //

// filter par style //
const filterLeftBtn = document.querySelector(".filter-par .left button");
const filterRightBtn = document.querySelector(".filter-par .right button");

const filterFramework = document.querySelector(".filter-par .filters");
const filter = document.querySelector(".filter-par .filters .types");
const filterItems = document.querySelectorAll(".filter-par .filters .types li");

const filtersFrameworkStyle = window.getComputedStyle(filterFramework);
const filterStyle = window.getComputedStyle(filter);

let filtersAppearNum = 5;

let filtersFrameworkWidth = filtersFrameworkStyle
    .getPropertyValue("width")
    .split("px")[0];

filterItems.forEach((obj) => {
    obj.style.width = filtersFrameworkWidth / filtersAppearNum + "px";
});

let itemsPointer = 0;

filterLeftBtn.addEventListener("click", (e) => {
    if (itemsPointer > 0) {
        itemsPointer--;
        filter.style.left =
            -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) + "px";
    }
});

filterRightBtn.addEventListener("click", (e) => {
    if (itemsPointer < filterItems.length - filtersAppearNum) {
        itemsPointer++;
        filter.style.left =
            -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) + "px";
    }
});

//  //

// URL //
const filterMeneContainer = document.querySelector(".filter-mene .container");
const filterMeneBtnContent = document.querySelector(
    ".filter-mene .open .content"
);

let productTypesItems = {
    clothes: [
        { name: "none", logo: "../img/icon/none.png" },
        { name: "shirts", logo: "../img/icon/clothe/shirt.png" },
        { name: "pants", logo: "../img/icon/clothe/pant.png" },
        { name: "shoes", logo: "../img/icon/clothe/shoes.png" },
        { name: "coats", logo: "../img/icon/clothe/coat.png" },
        { name: "hats", logo: "../img/icon/clothe/hat.png" },
        { name: "dresses", logo: "../img/icon/clothe/dress.png" },
        { name: "skirts", logo: "../img/icon/clothe/skirt.png" },
        { name: "more", logo: "../img/icon/more.png" },
    ],
    tools: [
        { name: "none", logo: "../img/icon/none.png" },
        { name: "hammer", logo: "../img/icon/tool/hammer.png" },
        { name: "painting", logo: "../img/icon/tool/painting.png" },
        { name: "saw", logo: "../img/icon/tool/saw.png" },
        { name: "screw driver", logo: "../img/icon/tool/screw-driver.png" },
        { name: "shovel", logo: "../img/icon/tool/shovel.png" },
        { name: "wrench", logo: "../img/icon/tool/wrench.png" },
        { name: "more", logo: "../img/icon/more.png" },
    ],
    vehicles: [
        { name: "none", logo: "../img/icon/none.png" },
        { name: "car", logo: "../img/icon/vehicle/car.png" },
        { name: "motorcycle", logo: "../img/icon/vehicle/motorcycle.png" },
        { name: "bike", logo: "../img/icon/vehicle/bike.png" },
        { name: "more", logo: "../img/icon/more.png" },
    ],
    "car parts": [
        { name: "none", logo: "../img/icon/none.png" },
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
        { name: "more", logo: "../img/icon/more.png" },
    ],
    electrics: [
        { name: "none", logo: "../img/icon/none.png" },
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
        { name: "more", logo: "../img/icon/more.png" },
    ],
    furniture: [
        { name: "none", logo: "../img/icon/none.png" },
        { name: "bed", logo: "../img/icon/furniture/bed.png" },
        { name: "chair", logo: "../img/icon/furniture/chair.png" },
        { name: "closet", logo: "../img/icon/furniture/closet.png" },
        { name: "mattress", logo: "../img/icon/furniture/mattress.png" },
        { name: "pillow", logo: "../img/icon/furniture/pillow.png" },
        { name: "sofa", logo: "../img/icon/furniture/sofa.png" },
        { name: "table", logo: "../img/icon/furniture/table.png" },
        { name: "more", logo: "../img/icon/more.png" },
    ],
    building: [
        { name: "none", logo: "../img/icon/none.png" },
        { name: "cement", logo: "../img/icon/building/cement.png" },
        { name: "paint", logo: "../img/icon/building/paint.png" },
        { name: "electrical", logo: "../img/icon/building/electrical.png" },
        { name: "more", logo: "../img/icon/more.png" },
    ],
    books: [
        { name: "none", logo: "../img/icon/none.png" },
        { name: "student", logo: "../img/icon/book/student-book.png" },
        { name: "language", logo: "../img/icon/book/language-book.png" },
        { name: "novel", logo: "../img/icon/book/novel.png" },
        { name: "children", logo: "../img/icon/book/children-book.png" },
        { name: "religious", logo: "../img/icon/book/religious-book.png" },
        { name: "more", logo: "../img/icon/more.png" },
    ],
    phones: [
        { name: "none", logo: "../img/icon/none.png" },
        { name: "smart phone", logo: "../img/icon/phone/smart-phone.png" },
        { name: "old phone", logo: "../img/icon/phone/old-phone.png" },
        { name: "fixed phone", logo: "../img/icon/phone/fixed-phone.png" },
        { name: "more", logo: "../img/icon/more.png" },
    ],
};

function setSideFilter(type) {
    if (type == "none") {
        filterMene.style.display = "none";
        return;
    }

    let items = "";

    productTypesItems[type].forEach((obj) => {
        let linkClass = "item";

        urlPar.forEach((par) => {
            if (par["name"] == "filter_type" && par["value"] == obj["name"]) {
                linkClass += " active";
            }
        });

        items +=
            '<a href="?product_type=' +
            type +
            "&filter_type=" +
            obj["name"] +
            '" class="' +
            linkClass +
            '"><img src="' +
            obj["logo"] +
            '" alt="" class="logo" /><p class="content">' +
            obj["name"] +
            "</p></a>";
    });

    filterMeneContainer.innerHTML = items;
    filterMeneBtnContent.innerHTML = type;
}

function itemGenerator(filterType, actionType) {
    let itemContent = "";

    itemContent += '<div class="item ' + actionType + '">'; // item open //

    // item img //
    if (actionType == "exchange") {
        itemContent +=
            '<div class="img"><img src="../img/img-3.jpg" alt="" /></div>';
    } else {
        itemContent += '<div class="img-price-container">'; // img price container open //

        // img //
        itemContent +=
            '<div class="img"><img src="../img/img-3.jpg" alt="" /></div>';
        //  //

        // price //
        let price = Math.floor(Math.random() * 1000) * 10;
        itemContent +=
            '<div class="price-container"><h3>price: <br />' +
            price +
            ".00</h3></div>";
        //  //

        itemContent += "</div>"; // img price container open //
    }
    //  //

    // item name //
    itemContent += '<h3 class="product-name">Product Name</h3>';
    //  //

    // item description //
    itemContent += '<div class="description">'; // description open //

    itemContent +=
        '<p class="content">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eius beatae vitae fuga optio nihil dolore?</p>';

    itemContent += '<a href="" class="more">more</a>';

    itemContent += "</div>"; // description close //
    //  //

    // item action //
    itemContent += '<div class="actions">'; // action open //

    itemContent += '<div class="owner">'; // owner open //

    // owner logo //
    itemContent +=
        '<div class="logo"><img src="../img/img-1.jpg" alt="" /></div>';
    //  //

    // owner name //
    itemContent += '<span class="name">The Owner</span>';
    //  //

    itemContent += "</div>"; // owner close //

    itemContent += '<a href="" class="get">' + actionType + "</a>"; // action button //

    itemContent += "</div>"; // action close //
    //  //

    itemContent += "</div>"; // item close //

    return itemContent;
}

function setMarketNotFiltered(productType) {
    let marketContent = "";

    productTypesItems[productType].forEach((filterType) => {
        if (filterType["name"] == "none" || filterType["name"] == "more") {
            return;
        }

        // open the type container //
        marketContent +=
            '<div class="items"><div class="type"><h2>' +
            filterType["name"] +
            "</h2></div>";
        //  //

        // the items //
        marketContent += '<div class="container">'; // adding open //

        // add the items //
        for (let i = 0; i < 3; i++) {
            let actionType =
                Math.floor(Math.random() * 2) == 0 ? "exchange" : "bay";
            marketContent += itemGenerator(filterType, actionType);
        }
        //  //

        marketContent += "</div>"; // adding close //
        //  //

        // close the type container //
        marketContent += '<a href="" class="view-all">View All</a></div>';
        //  //
    });

    market.innerHTML = marketContent;
}

function setMarketFiltered(filterType) {}

const filterItemsLink = document.querySelectorAll(
    ".filter-par .filters .types li a"
);

let urlPar = getUrlParameters();
urlPar.forEach((obj) => {
    switch (obj["name"]) {
        case "product_type":
            {
                let productTypeIndex = 0;

                // active the product type //
                filterItemsLink.forEach((filter, index) => {
                    if (obj["value"] == filter.innerText.toLowerCase()) {
                        filter.classList.add("active");
                        productTypeIndex = index; // get the product type index ///
                    }
                });
                //  //

                // scroll the product type filter to the active type //
                if (productTypeIndex < filterItems.length - filtersAppearNum) {
                    itemsPointer = productTypeIndex;
                } else {
                    itemsPointer = filterItems.length - filtersAppearNum;
                }

                filter.style.left =
                    -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) +
                    "px";
                //  //

                // set the side mene types //
                setSideFilter(obj["value"]);
                //  //
            }

            break;

        case "filter_type":
            {
                if (obj["value"] == "none") {
                    let productType = "none";

                    // get product type //
                    urlPar.forEach((par) => {
                        if (par["name"] == "product_type") {
                            productType = par["value"];
                        }
                    });
                    //  //

                    setMarketNotFiltered(productType);
                }
            }

            break;

        default:
            break;
    }
});
//  //
