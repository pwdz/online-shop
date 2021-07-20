const base_path = "../images/slideshow/"
const images = ["1.jpg", "2.jpg", "3.jpg"];

var currIndex = 0
// showSlides(currIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(currIndex + n);
}

function showSlides(n) {

  document.getElementById('imageslider').style.backgroundImage="url(../images/slideshow/3.jpg)"; // specify the image path here
  n = n % images.length;
  currIndex = n

  var sliderComponent = document.getElementById("imageslider");

  console.log(base_path + images[n]);
  // sliderComponent.style.backgroundImage = "url("+base_path + images[n] + ")";
  sliderComponent.style.backgroundImage = "url(../images/slideshow/1.jpg)";
  console.log(sliderComponent)

  // await sleep(10000);
} 

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
