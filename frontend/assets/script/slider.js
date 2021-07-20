const basePath = "assets/images/slideshow/"
const images = ["1.jpg", "2.jpg", "3.jpg"];

var currIndex = 0
showSlides(currIndex);

// Next/previous controls
function plusSlides(n) {
  currIndex += n 
  currIndex = currIndex % images.length
  if(currIndex<0)
    currIndex = images.length - 1

  document.getElementById("imageslider").style.backgroundImage =  "url("+basePath + images[currIndex] + ")";
}

async function showSlides(n) {
  n = n % images.length;
  currIndex = n

  document.getElementById("imageslider").style.backgroundImage =  "url("+basePath + images[currIndex] + ")";

  await sleep(10000);
  showSlides(n+1)
} 

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
