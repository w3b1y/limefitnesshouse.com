const navMenu = document.querySelector('.nav__menu'),
      navToggle = document.querySelector('.nav__toggle'),
      navClose = document.querySelector('.nav__close'),
      navLink = document.querySelectorAll('.nav__item');

if (navToggle) {
  navToggle.addEventListener('click', () => {
    navMenu.classList.add('show-menu');
  });
}

if (navClose) {
  navClose.addEventListener('click', () => {
    navMenu.classList.remove('show-menu');
  });
}

const linkAction = () => {
  const navMenu = document.querySelector('.nav__menu');
  navMenu.classList.remove('show-menu');
}
navLink.forEach(l => l.addEventListener('click', linkAction));