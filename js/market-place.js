
const filterPar = document.querySelector(".filter-par");
const toolsPar = document.querySelector(".tools-par");
const market = document.querySelector("section.market");


// filter par style //
const filterLeftBtn = document.querySelector(".filter-par .left");//*************
const filterRightBtn = document.querySelector(".filter-par .right");//**********************

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
        // move to left //
        itemsPointer--;
        filter.style.left =
            -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) + "px";
        //  //

        // enable the right button //
        filterRightBtn.classList.remove("disable");
        //  //

        // disable the left button if hit the edge //
        if (!(itemsPointer > 0)) {
            filterLeftBtn.classList.add("disable");
        }
        //  //
    }
});

filterRightBtn.addEventListener("click", (e) => {
    if (itemsPointer < filterItems.length - filtersAppearNum) {
        // move to right //
        itemsPointer++;
        filter.style.left =
            -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) + "px";
        //  //

        // enable the left button //
        filterLeftBtn.classList.remove("disable");
        //  //

        // disable the right button if hit the edge //
        if (!(itemsPointer < filterItems.length - filtersAppearNum)) {
            filterRightBtn.classList.add("disable");
        }
        //  //
    }
});
//  //

let productTypesItems = {

    "car parts": [
        {
            name: "car engine",
            logo: "../img/icon/car parts/car-engine.png",
        },
        {
            name: "car wheel",
            logo: "../img/icon/car parts/car-wheel.png"
        },
        {
            name: "car battery",
            logo: "../img/icon/car parts/car-battery.png",
        },
        {
            name: "car chair",
            logo: "../img/icon/car parts/car-chair.png"
        },
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
    ]
};

function getProductIconLocation(productType, filterType) {
    let location = "";

    productTypesItems[productType].forEach((obj) => {
        if (obj["name"] == filterType) {
            location = obj["logo"];
        }
    });

    return location;
}

function setSideFilter(type) {

    let items = "";

    // the all filter //
    items +=
        '<a href="?product_type=' + type + '&filter_type=all" class="item' +
        (urlPar["filter_type"] == "all" ? " active" : "") + // light the selected element //
        '"><img src="../img/icon/all.png" alt="" class="logo" /><p class="content">all</p></a>';
    //  //

    // the rest filters //
    productTypesItems[type].forEach((obj) => {
        items +=
            '<a href="?product_type=' +
            type +
            "&filter_type=" +
            obj["name"] +
            '" class="' +
            "item" +
            (urlPar["filter_type"] == obj["name"] ? " active" : "") + // light the selected element //
            '"><img src="' +
            obj["logo"] +
            '" alt="" class="logo" /><p class="content">' +
            obj["name"] +
            "</p></a>";
    });
    //  //

    // the all filter //
    items +=
        '<a href="?product_type=' +
        type +
        '&filter_type=other" class="item' +
        (urlPar["filter_type"] == "other" ? " active" : "") + // light the selected element //
        '"><img src="../img/icon/other.png" alt="" class="logo" /><p class="content">other</p></a>';
    //  //
}

function itemGenerator(filterType, index) {
    let itemContent = "";

    itemContent += '<div class="item exchange">'; // item open //

    // item img //
    itemContent += `<div class="img">
        <img src="../img/products/${urlPar["product_type"]}/${filterType}/${filterType} (${index}).jpg" alt="" />
        </div>`;

    //  //
    let price = Math.floor(Math.random() * 1000) * 10;
    // item name //
    itemContent += `<div class='product' dir='rtl'>
                        <h3 class='product-name'>اسم المنتج</h3>
                        <h3 class='product-name'>`+ price + ` دج</h3>
                    </div>`;
    //  //
    // item description //
    itemContent += '<div class="description">'; // description open //

    itemContent +=
        '<p class="content">رح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح شرح </p>';

    itemContent += `<a href="product.htm?product_type=${urlPar["product_type"]}&filter_type=${filterType}" class="more">...المزيد</a>`; // show more //

    itemContent += "</div>"; // description close //
    //  //
    // item action //
    itemContent += '<div class="actions">'; // action open //
    //  //
    itemContent += "</a>"; // owner close //

    itemContent += `<a href="product.htm?product_type=${urlPar["product_type"]}&filter_type=${filterType}" class="get">شراء</a>`; // action button //

    itemContent += "</div>"; // action close //
    //  //

    itemContent += "</div>"; // item close //

    return itemContent;
}

function setMarketNotFiltered(productType) {
    let marketContent = "";

    productTypesItems[productType].forEach((filterType) => {
        if (filterType["name"] == "all" || filterType["name"] == "more") {
            return;
        }

        // open the type container //
        marketContent +=
            '<div class="items">' +
            '<div class="type">' +
            `<img src="${filterType["logo"]}" alt="" />` +
            `<h2> ${filterType["name"]}</h2>` +
            "</div>";
        //  //

        // the items //
        marketContent += '<div class="container">'; // adding open //

        // add the items //
        for (let i = 0; i < 3; i++) {
            marketContent += itemGenerator(
                filterType["name"],
                i + 1
            );
        }
        //  //

        marketContent += "</div>"; // adding close //
        //  //

        // close the type container //
        marketContent += `<a href="?product_type=${productType}&&filter_type=${filterType["name"]}" class="view-all">إظهار المزيد</a></div>`;
        //  //
    });

    market.innerHTML = marketContent;
}

function setMarketFiltered(filterType) {
    let marketContent = "";

    if (filterType == "all" || filterType == "more") {
        return;
    }

    // open the type container //
    marketContent +=
        '<div class="items">' +
        '<div class="type">' +
        `<img src="${getProductIconLocation(
            urlPar["product_type"],
            filterType
        )}" alt="" />` +
        `<h2> ${filterType}</h2>` +
        "</div>";
    //  //

    // the items //
    marketContent += '<div class="container">'; // adding open //

    // add the items //
    for (let i = 1; i <= 30; i++) {
        marketContent += itemGenerator(filterType, (i % 3) + 1);
    }
    //  //

    marketContent += "</div>"; // adding close //
    //  //

    // close the type container //
    marketContent += "</div>";
    //  //

    market.innerHTML = marketContent;
    market.classList.add("filtered");
}

const filterItemsLink = document.querySelectorAll(
    ".filter-par .filters .types li a"
);
function productTypeFilterStyle(product_type) {
    let productTypeIndex = 0;

    // active the product type //
    filterItemsLink.forEach((filter, index) => {
        if (product_type == filter.innerText.toLowerCase()) {
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
        -itemsPointer * (filtersFrameworkWidth / filtersAppearNum) + "px";
    //  //

    // disable the left button if hit the edge //
    if (!(itemsPointer > 0)) {
        filterLeftBtn.classList.add("disable");
    }
    //  //

    // disable the right button if hit the edge //
    if (!(itemsPointer < filterItems.length - filtersAppearNum)) {
        filterRightBtn.classList.add("disable");
    }
    //  //
}

productTypeFilterStyle(urlPar["product_type"]);
setSideFilter(urlPar["product_type"]);

if (urlPar["filter_type"] == "all") {
    setMarketNotFiltered(urlPar["product_type"]);
} else {
    setMarketFiltered(urlPar["filter_type"]);
}
//  //
