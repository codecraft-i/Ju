// Main Carousel JS

const images = document.querySelectorAll(".carousel img");
const carouselImages = document.querySelector(".carousel-images");
const indicatorsContainer = document.querySelector(".indicators");
let index = 0;
let interval;

images.forEach((_, i) => {
    // Create a dot
    const indicator = document.createElement("div");
    indicator.classList.add("indicator");
    if (i === 0) indicator.classList.add("active"); // Add active class to the first dot
    indicator.addEventListener("click", () => moveTo(i)); // Add click event to the dot
    indicatorsContainer.appendChild(indicator); // Append the dot to the container
});

function updateIndicators() {
    // Loop through all the dots
    document.querySelectorAll(".indicator").forEach((dot, i) => { // Get all the dots
        dot.classList.toggle("active", i === index); // Toggle the active class based on the index
    });
}
        
function moveTo(newIndex) {
    // Move the carousel to the new index
    index = newIndex;
    let slideWidth = window.innerWidth < 1000 ? 300 : 380; // Slide width for mobile and desktop
    carouselImages.style.transform = `translateX(${-index * slideWidth}px)`; // Move the carousel
    updateIndicators(); // Update the dots
}

function nextSlide() {
    // Move to the next slide
    index = (index + 1) % images.length; // Increment the index
    moveTo(index); // Move to the new index
}

function startAutoSlide() {
    // Start the auto slide
    interval = setInterval(nextSlide, 4000); // Slide every 4 seconds
}

// Event listeners
document.querySelector(".right").addEventListener("click", () => {
    nextSlide(); // Move to the next slide
});

document.querySelector(".left").addEventListener("click", () => {
    // Move to the previous slide
    index = (index - 1 + images.length) % images.length; // Decrement the index
    moveTo(index); // Move to the new index
});

startAutoSlide(); // Start the auto slide

// Mobile Responsive Carousel JS
const topImages = document.querySelectorAll(".top-carousel img");
const topCarouselImages = document.querySelector(".top-carousel-images");
const topIndicatorsContainer = document.querySelector(".top-indicators");
let topIndex = 0;

topImages.forEach((_, i) => {
    const topIndicator = document.createElement("div");
    topIndicator.classList.add("top-indicator");
    if (i === 0) topIndicator.classList.add("top-active");
    topIndicator.addEventListener("click", () => topMoveTo(i));
    topIndicatorsContainer.appendChild(topIndicator);
});

function topUpdateIndicators() {
    document.querySelectorAll(".top-indicator").forEach((dot, i) => {
        dot.classList.toggle("top-active", i === topIndex);
    });
}

function topMoveTo(newIndex) {
    topIndex = newIndex;
    topCarouselImages.style.transform = `translateX(${-topIndex * 330}px)`;
    topUpdateIndicators();
}

function topNextSlide() {
    topIndex = (topIndex + 1) % topImages.length;
    topMoveTo(topIndex);
}

function topStartAutoSlide() {
    interval = setInterval(topNextSlide, 4000);
}

document.querySelector(".top-right").addEventListener("click", () => {
    topStartAutoSlide();
});

document.querySelector(".top-left").addEventListener("click", () => {
    topIndex = (topIndex - 1 + topImages.length) % topImages.length;
    topMoveTo(topIndex);
});

topStartAutoSlide()

// author: Davronbek Yakubov
// author: Dorik
// Created: 4.03.2025

// By Dorik
// By Code Craft