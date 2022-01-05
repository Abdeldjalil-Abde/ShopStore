// profile img //
const img_input = document.querySelector(".edit .avatar .img input");
const profileImg = document.querySelector(".edit .avatar .img img");

img_input.addEventListener("change", () => {
    const reader = new FileReader();

    reader.addEventListener("load", () => {
        profileImg.setAttribute("src", reader.result);
    });

    reader.readAsDataURL(img_input.files[0]);
});
//  //
