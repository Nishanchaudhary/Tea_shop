let menu = document.querySelector('.bx-menu');
let navbar = document.querySelector('.navbar');

menu.addEventListener('click', function(){
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('nav-toggle');
})

window.addEventListener('scroll', ()=>{
    menu.classList.remove('bx-x');
    navbar.classList.remove('nav-toggle');
})

const header = document.querySelector('header');
window.onscroll = function(){
    if(document.documentElement.scrollTop > 5){
        header.style.height = '100px';
        header.style.backgroundColor = '#fff'
    }else{
        header.style.height = '100px';
        header.style.backgroundColor = '#fff'
    }
}





//home slider
const imgBox = document.querySelector('.slider-container');
const slides = document.getElementsByClassName('slideBox');
var i = 0;

function nextSlide(){
    slides[i].classList.remove('active');
    i = (i + 1) % slides.length;
    slides[i].classList.add('active');
}

function prevSlide(){
    slides[i].classList.remove('active');
    i = (i - 1 + slides.length) % slides.length;
    slides[i].classList.add('active');
}