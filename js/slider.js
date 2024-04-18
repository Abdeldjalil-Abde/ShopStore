
const slides = document.querySelectorAll(".slide");
const slider = document.querySelector(".slider");
// select next slide button
const nextSlide = document.querySelector(".btn-next");

// select prev slide button
const prevSlide = document.querySelector(".btn-prev");

const dots = document.querySelectorAll(".dot");


// maximum number of slides
let maxSlide = slides.length - 1;
let curSlide = 0;

// delete class  

function deleteClass() {
    dots.forEach((dot) => {
        dot.classList.remove("active");
    });
}
deleteClass();

// loop through slides and set each slides translateX property to index * 100% 
slides.forEach((slide, index) => {
  slide.style.transform = `translateX(${index * 100}%)`;
  dots[dots.length -  curSlide - 1].classList.add("active");
});
slides.forEach((obj)=>{
    obj.addEventListener("click", function () {
        if (curSlide === maxSlide) {
            curSlide = 0;
          } else {
            curSlide++;
          }
      //   move slide by 100%
      slides.forEach((slide, index) => {
        slide.style.transform = `translateX(${100 * (index - curSlide)}%)`;
        deleteClass();
      });
      dots[dots.length -  curSlide - 1].classList.add("active");
    });     
});
// add event listener and next slide functionality
nextSlide.addEventListener("click", function () {
    if (curSlide === maxSlide) {
        curSlide = 0;
      } else {
        curSlide++;
      }
  //   move slide by 100%
  slides.forEach((slide, index) => {
    slide.style.transform = `translateX(${100 * (index - curSlide)}%)`;
  });
  deleteClass();
  dots[dots.length -  curSlide - 1].classList.add("active");
});

// add event listener and navigation functionality
prevSlide.addEventListener("click", function () {
  // check if current slide is the first and reset current slide to last
  if (curSlide === 0) {
    curSlide = maxSlide;
  } else {
    curSlide--;
  }
  
  slides.forEach((slide, index) => {
    slide.style.transform = `translateX(${100 * (index - curSlide)}%)`;
  });
  deleteClass();
  dots[dots.length -  curSlide - 1].classList.add("active");
});
