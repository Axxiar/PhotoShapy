const milow = document.querySelector('#milow');
const axxiar = document.querySelector('#axxiar');

const at_milow = document.querySelector('#mi');
const at_axxiar = document.querySelector('#ax');

milow.addEventListener('mouseover', () => {
	at_milow.innerHTML = "@"
	at_milow.style.opacity = 1
})

axxiar.addEventListener('mouseover', () => {
	at_axxiar.innerHTML = "@"
	at_axxiar.style.opacity = 1
})


milow.addEventListener('mouseout', () => {
	at_milow.innerHTML = ""
	at_milow.style.opacity = 0
})

axxiar.addEventListener('mouseout', () => {
	at_axxiar.innerHTML = ""
	at_axxiar.style.opacity = 0
})
