// Content writer //
let content =
    "if you want anything for sheep prices, or treading products with other peoples, this platform will help you to reach them . . .";

const contentContainer = document.querySelector(".log-in .right > .content");

let writingDelay = 100;
let endWritingDelay = 17000;
let lettersPointer = 0;

function writeLetter() {
    contentContainer.innerHTML += content[lettersPointer];
    lettersPointer++;

    if (lettersPointer == content.length) {
        setTimeout(() => {
            contentContainer.innerHTML = "";
            lettersPointer = 0;

            writeLetter();
        }, endWritingDelay);
    } else {
        let delay =
            content[lettersPointer] == " " ? writingDelay * 4 : writingDelay;

        setTimeout(() => {
            writeLetter();
        }, delay);
    }
}
writeLetter();
//  //
