//hora


const hora = document.getElementById('hora');

const interval = setInterval(() => {

  const local = new Date();


  hora.innerHTML = local.toLocaleTimeString('en-US');

}, 1000);



/*===== EXPANDER MENU  =====*/
const showMenu = (toggleId, navbarId, bodyId) => {
  const toggle = document.getElementById(toggleId),
    navbar = document.getElementById(navbarId),
    bodypadding = document.getElementById(bodyId)

  if (toggle && navbar) {
    toggle.addEventListener('click', () => {
      navbar.classList.toggle('expander')

      bodypadding.classList.toggle('body-pd')
    })
  }
}
showMenu('nav-toggle', 'navbar', 'body-pd')

/*===== LINK ACTIVE  =====*/
const linkColor = document.querySelectorAll('.nav__link')
function colorLink() {
  linkColor.forEach(l => l.classList.remove('active'))
  this.classList.add('active')
}
linkColor.forEach(l => l.addEventListener('click', colorLink))


/*===== COLLAPSE MENU  =====*/
const linkCollapse = document.getElementsByClassName('collapse__link')
var i

for (i = 0; i < linkCollapse.length; i++) {
  linkCollapse[i].addEventListener('click', function () {
    const collapseMenu = this.nextElementSibling
    collapseMenu.classList.toggle('showCollapse')

    const rotate = collapseMenu.previousElementSibling
    rotate.classList.toggle('rotate')
  })
}

const open = document.getElementById('open');
const modal_container = document.getElementById('modal_container');
const close = document.getElementById('close');

open.addEventListener('click', () => {
  modal_container.classList.add('show');
});

close.addEventListener('click', () => {
  modal_container.classList.remove('show');
});


const open2 = document.getElementById('open2');
const modal_container2 = document.getElementById('modal_container2');
const close2 = document.getElementById('close2');

open.addEventListener('click', () => {
  modal_container2.classList.add('show2');
});

close.addEventListener('click', () => {
  modal_container2.classList.remove('show2');
});


const preguntaBtn = document.querySelectorAll('.btnAns')

if(preguntaBtn) {
  const btnArray = Array.from(preguntaBtn);
  btnArray.forEach((btn) => {
      btn.addEventListener('click', (e) =>{
        if(!confirm("Esta seguro e querer eliminar el dato?, La accion es irreversible")){
          e.preventDefault();
        }
      });
  });
}
