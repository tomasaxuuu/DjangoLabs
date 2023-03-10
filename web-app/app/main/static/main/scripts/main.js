const burger = document.querySelector('.burger-menu');
const nav = document.querySelector('.nav');
const nav_item = document.querySelectorAll('.nav-item');
const body = document.body;
burger.addEventListener('click', function() {
    burger.classList.toggle('burger__active');
    nav.classList.toggle('nav__active');
    body.classList.toggle('body__active');
});
nav_item.forEach(el => el.addEventListener('click', function() {
    nav.classList.toggle('nav__active');
}));