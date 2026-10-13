const menuButton=document.querySelector('.mobile-toggle');
const mobileMenu=document.querySelector('.mobile-menu');
menuButton?.addEventListener('click',()=>{const expanded=menuButton.getAttribute('aria-expanded')==='true';menuButton.setAttribute('aria-expanded',String(!expanded));menuButton.setAttribute('aria-label',expanded?'Atidaryti meniu':'Uždaryti meniu');mobileMenu.classList.toggle('is-open',!expanded);});
mobileMenu?.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{mobileMenu.classList.remove('is-open');menuButton.setAttribute('aria-expanded','false');}));
document.getElementById('year').textContent=String(new Date().getFullYear());
const form=document.getElementById('contact-form');
form?.addEventListener('submit',(event)=>{event.preventDefault();if(!form.reportValidity())return;const name=form.querySelector('#name').value.trim();document.getElementById('form-status').textContent=`Ačiū, ${name}! Tai demonstracinė svetainė. Jūsų užklausa neužregistruota ir niekur neišsiųsta.`;form.reset();});
const navLinks=[...document.querySelectorAll('.desktop-nav a')];const sections=[...document.querySelectorAll('main section[id]')];const observer=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){navLinks.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+e.target.id));}}},{rootMargin:'-25% 0px -65% 0px'});sections.forEach(section=>observer.observe(section));
