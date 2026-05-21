const botao = document.querySelector('.botaoBurguer');
const menu = document.querySelector('.ListaMenu');

botao.addEventListener('click', () => {
    menu.classList.toggle('aberto');
});