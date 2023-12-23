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

const form = document.querySelector('form');
if (form) {
  const submitBtn = document.querySelector('#contact__form-submit');
  submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    let user = form.elements['firstname'].value;
    let message = form.elements['message'].value;

    if (user && message) {
      let whatsappURL = `https://wa.me/393500020002?text=Salve%20sono%20${user}%20${message}`;
      console.log('WhatsApp URL:', whatsappURL);

      window.location.replace(whatsappURL);
    } else {
      console.error('Please fill in both the user and message fields.');
    }
  });
} else {
  console.error('Form or submit button not found.');
}